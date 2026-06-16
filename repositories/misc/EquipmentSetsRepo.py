import re
from typing import List

from definitions.misc.EquipmentSets import EquipmentSets
from helpers.HelperFunctions import formatStr, getFromSplitArray, getFromMixedArray
from repositories.misc.RandoListRepo import RandoListRepo, RandoListDescriptions
from repositories.master.Repository import Repository


class EquipmentSetsRepo(Repository[EquipmentSets]):

	@classmethod
	def initDependencies(cls, log=True) -> None:
		RandoListRepo.initialise(cls.codeReader, False)

	@classmethod
	def getCategory(cls) -> str:
		return "Misc"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["EquipmentSets"]

	@classmethod
	def generateRepo(cls) -> None:
		# Updated regex to capture complete equipment set data including nested arrays
		reDropTables = r'e\.h\.(\w+) = \[(.*?)\]\),'
		equipmentSetsData = formatStr(cls.getSection(), ["\n", "  "])
		setOrder = RandoListRepo.get(RandoListDescriptions.EquipmentSetsDisplayOrder).elements
		
		# Use DOTALL flag to match across newlines and make the regex non-greedy but more comprehensive
		matches = re.findall(reDropTables, equipmentSetsData, re.DOTALL)
		
		for name, equipmentSet in matches:
			parsedSet = getFromMixedArray(equipmentSet)
			metadata = parsedSet[3]

			toAdd = EquipmentSets(
				name=name,
				armors=parsedSet[0],
				tools=parsedSet[1],
				weapons=parsedSet[2],
				toolsRequired=metadata[0],
				weaponRequired=metadata[1],
				bonusValue=metadata[2],
				description=formatStr(metadata[3], replaceUnderscores=True),
				displayOrder=setOrder.index(name))
			cls.addList(toAdd)
			cls.add(name, toAdd)
