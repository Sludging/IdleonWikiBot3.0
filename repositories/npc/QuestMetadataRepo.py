import ast
import json
import re
from typing import Dict, List, Optional, Tuple

from definitions.questdef.QuestMetadata import AccountWideQuest, MainQuest, QuestMetadata
from helpers.Constants import Constants
from helpers.HelperFunctions import replaceUnderscores
from repositories.master.Repository import Repository


class QuestMetadataRepo(Repository[QuestMetadata]):
	@classmethod
	def getCategory(cls) -> str:
		return "Npc"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["MainQuests", "AccountWideQuests"]

	@classmethod
	def generateRepo(cls) -> None:
		mainQuests = []
		for key, values in cls._extractAssignedArrays(cls.getSection(0)):
			if len(values) < 3 or not all(isinstance(values[index], list) for index in range(3)):
				continue
			npcName = cls._normaliseNpcName(key)
			mainQuests.append(MainQuest(
				npc = npcName,
				map = values[0],
				scene = values[1],
				index = values[2],
			))

		accountWideQuests = []
		for key, values in cls._extractAssignedArrays(cls.getSection(1)):
			if len(values) < 3 or not isinstance(values[0], str):
				continue
			npcName = cls._normaliseNpcName(values[0])
			accountWideQuests.append(AccountWideQuest(
				key = key,
				npc = npcName,
				index = values[1],
				accountWide = str(values[2]) == "1",
			))

		metadata = QuestMetadata(
			mainQuests = mainQuests,
			accountWideQuests = accountWideQuests,
		)
		cls.add("metadata", metadata)
		cls.addList(metadata)

	@classmethod
	def _normaliseNpcName(cls, name: str) -> str:
		name = replaceUnderscores(name)
		return Constants.nameConflicts.get(name, name)

	@classmethod
	def _extractAssignedArrays(cls, section: str) -> List[Tuple[str, list]]:
		"""Extract assigned arrays in source order from a quest metadata section.

		The game writes each entry as a variable array followed by both a
		``setReserved`` call and an ``h`` property fallback.  Processing those
		assignments in order lets us resolve reused variables without flattening
		nested arrays, while de-duplicating the two writes for each entry.
		"""
		if not section:
			return []

		variableAssignment = re.compile(
			r'(?<![\w$.])(?:var\s+)?([A-Za-z_$][\w$]*)\s*=\s*(?=\s*\[)'
		)
		directAssignment = re.compile(
			r'\b[A-Za-z_$][\w$]*\s*\.\s*h\s*'
			r'(?:\.\s*([A-Za-z_$][\w$]*)|\[\s*["\']([^"\']+)["\']\s*\])\s*='
		)
		reservedAssignment = re.compile(
			r'\b[A-Za-z_$][\w$]*\s*\.\s*setReserved\s*'
			r'\(\s*["\']([^"\']+)["\']\s*,'
		)

		events = []
		events.extend((match.start(), "variable", match) for match in variableAssignment.finditer(section))
		events.extend((match.start(), "direct", match) for match in directAssignment.finditer(section))
		events.extend((match.start(), "reserved", match) for match in reservedAssignment.finditer(section))
		events.sort(key = lambda event: event[0])

		variables: Dict[str, list] = {}
		entries: List[Tuple[str, list]] = []
		seenKeys = set()
		for _, eventType, match in events:
			if eventType == "variable":
				value = cls._readArray(section, match.end())
				if value is not None:
					variables[match.group(1)] = value
				continue

			if eventType == "direct":
				key = match.group(1) or match.group(2)
			else:
				key = match.group(1)
			value = cls._readValue(section, match.end(), variables)
			if value is None or key in seenKeys:
				continue
			seenKeys.add(key)
			entries.append((key, value))
		return entries

	@classmethod
	def _readValue(cls, section: str, offset: int, variables: Dict[str, list]) -> Optional[list]:
		start = offset
		while start < len(section) and section[start].isspace():
			start += 1
		if start < len(section) and section[start] == "[":
			return cls._readArray(section, start)
		match = re.match(r'([A-Za-z_$][\w$]*)', section[start:])
		if not match:
			return None
		return variables.get(match.group(1))

	@classmethod
	def _readArray(cls, section: str, offset: int) -> Optional[list]:
		start = offset
		while start < len(section) and section[start].isspace():
			start += 1
		if start >= len(section) or section[start] != "[":
			return None

		end = cls._findArrayEnd(section, start)
		if end is None:
			return None
		literal = section[start:end + 1]
		try:
			value = json.loads(literal)
		except json.JSONDecodeError:
			try:
				value = ast.literal_eval(literal)
			except (ValueError, SyntaxError):
				return None
		return value if isinstance(value, list) else None

	@staticmethod
	def _findArrayEnd(section: str, start: int) -> Optional[int]:
		depth = 0
		quote = ""
		escaped = False
		lineComment = False
		blockComment = False
		index = start
		while index < len(section):
			char = section[index]
			if lineComment:
				if char == "\n":
					lineComment = False
				index += 1
				continue
			if blockComment:
				if char == "*" and index + 1 < len(section) and section[index + 1] == "/":
					blockComment = False
					index += 2
					continue
				index += 1
				continue
			if quote:
				if escaped:
					escaped = False
				elif char == "\\":
					escaped = True
				elif char == quote:
					quote = ""
				index += 1
				continue
			if char in {'"', "'", "`"}:
				quote = char
			elif char == "/" and index + 1 < len(section):
				nextChar = section[index + 1]
				if nextChar == "/":
					lineComment = True
					index += 2
					continue
				if nextChar == "*":
					blockComment = True
					index += 2
					continue
			elif char == "[":
				depth += 1
			elif char == "]":
				depth -= 1
				if depth == 0:
					return index
			index += 1
		return None
