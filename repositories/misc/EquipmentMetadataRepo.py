from typing import List

from definitions.misc.EquipmentMetadata import EquipmentMetadata
from helpers.HelperFunctions import getFromSplit, getFromSplitArray
from repositories.master.Repository import Repository


class EquipmentMetadataRepo(Repository[EquipmentMetadata]):
	@classmethod
	def getCategory(cls) -> str:
		return "Misc"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["PowerSuffixes", "EquipmentTypeReq", "EquiptypeGens", "SpeedNames"]

	@classmethod
	def generateRepo(cls) -> None:
		metadata = EquipmentMetadata(
			powerSuffixes = getFromSplit(cls.getSection(0)),
			equipmentTypeRequirements = getFromSplitArray(cls.getSection(1), replaceUnderscores = False),
			equipmentTypeGroups = getFromSplitArray(cls.getSection(2), replaceUnderscores = False),
			speedNames = getFromSplit(cls.getSection(3)),
		)
		cls.add("metadata", metadata)
		cls.addList(metadata)
