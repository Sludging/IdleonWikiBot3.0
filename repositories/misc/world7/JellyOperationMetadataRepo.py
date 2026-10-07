import re
from typing import Dict, List, Tuple

from definitions.misc.world7.jellyOperationMetadata import (
	JellyBoard,
	JellyObstructionSlotGrant,
	JellyOperationMetadata,
	JellyPlot,
)
from helpers.HelperFunctions import getFromMixedArray, getFromSplit, javascriptParser
from repositories.master.Repository import Repository


class JellyOperationMetadataRepo(Repository[JellyOperationMetadata]):
	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/7"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["Research", "JellyBoardUnlocks", "JellyInitialObstructionHp", "JellyBoardPlacement"]

	@classmethod
	def generateRepo(cls) -> None:
		# Research[50] contains plot triplets: starting slot, width, height.
		research = getFromMixedArray(cls.getSection(), respectDelimiter = True)
		plots = []
		for index, entry in enumerate(research[50]):
			startSlot, width, height = entry.split(",")
			plots.append(JellyPlot(index = index, startSlot = startSlot, width = width, height = height))

		initialSlots, grants = cls._extractBoardUnlocks(cls.getSection(1))
		placement = cls.getSection(3)
		columnMatch = re.search(r"%\s*(\d+)", placement)
		lastSlotMatch = re.search(r"\|\|\s*(\d+)\s*<\s*Math\.round\(", placement)
		if columnMatch is None or lastSlotMatch is None:
			raise ValueError("Jelly placement source is missing board dimensions")
		columns = int(columnMatch.group(1))
		rows, remainder = divmod(int(lastSlotMatch.group(1)) + 1, columns)
		if remainder:
			raise ValueError("Jelly board slot bounds do not form complete rows")

		metadata = JellyOperationMetadata(
			initialObstructionHp = {
				str(index): value for index, value in enumerate(getFromSplit(cls.getSection(2)))
			},
			board = JellyBoard(
				columns = columns,
				rows = rows,
				initialSlots = initialSlots,
				blockedSlots = getFromSplit(placement),
				obstructionSlotGrants = grants,
				plots = plots,
			),
		)
		cls.add("metadata", metadata)
		cls.addList(metadata)

	@classmethod
	def _extractBoardUnlocks(cls, section: str) -> Tuple[List[int], List[JellyObstructionSlotGrant]]:
		"""Keep literal starting slots separate from obstruction-completion grants.

		Purchased plots are expanded from account state in this same source block;
		their computed pushes are not static slots. Literal pushes beneath a
		``current obstruction > index`` predicate belong to that obstruction.
		"""
		source = section.encode("utf-8")
		root = javascriptParser.parse(source).root_node
		initialSlots = []
		grantSlots: Dict[int, List[int]] = {}
		nodes = [root]
		while nodes:
			node = nodes.pop()
			nodes.extend(reversed(node.named_children))
			if node.type != "call_expression":
				continue
			function = node.child_by_field_name("function")
			arguments = node.child_by_field_name("arguments")
			if function is None or arguments is None:
				continue
			functionText = source[function.start_byte:function.end_byte].decode("utf-8")
			if not functionText.endswith(".h.JellySlotz.push"):
				continue
			values = arguments.named_children
			if len(values) != 1 or values[0].type != "number":
				continue
			slot = int(source[values[0].start_byte:values[0].end_byte])
			obstructionIndex = None
			ancestor = node.parent
			while ancestor is not None:
				if ancestor.type == "binary_expression":
					operator = ancestor.child_by_field_name("operator")
					if operator is not None and source[operator.start_byte:operator.end_byte] == b"&&":
						predicate = ancestor.child_by_field_name("left")
						predicateText = source[predicate.start_byte:predicate.end_byte].decode("utf-8")
						match = re.fullmatch(
							r'(\d+)\s*<\s*[\w$.]+\.asNumber\(.*\.getGameAttribute\("Research"\)\[7\]\[9\]\)',
							predicateText,
							re.DOTALL,
						)
						if match is None:
							raise ValueError("Unrecognised Jelly static-slot grant predicate")
						obstructionIndex = int(match.group(1))
						break
				ancestor = ancestor.parent
			if obstructionIndex is None:
				initialSlots.append(slot)
			else:
				grantSlots.setdefault(obstructionIndex, []).append(slot)
		return initialSlots, [
			JellyObstructionSlotGrant(obstructionIndex = index, slots = slots)
			for index, slots in grantSlots.items()
		]
