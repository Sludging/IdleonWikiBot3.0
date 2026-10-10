from typing import List

from definitions.misc.world6.FarmingMetadata import CropScientistBonus, FarmingMetadata
from helpers.HelperFunctions import getFromMixedArray
from repositories.master.Repository import Repository


class FarmingMetadataRepo(Repository[FarmingMetadata]):
	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/6"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["NinjaInfo"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromMixedArray(cls.getSection(), respectDelimiter = True)
		# CropSCbonus gates display indices 0..9 on these Jade Emporium upgrades.
		# idleon1.22.txt:236464-236485; NinjaInfo[31] supplies the templates.
		unlockUpgradeIndices = [27, 24, 25, 26, 23, 28, 29, 38, 40, 44]
		metadata = FarmingMetadata(
			cropScientistBonuses = [
				CropScientistBonus(
					index = index,
					description = description,
					unlockUpgradeIndex = unlockUpgradeIndices[index],
				)
				for index, description in enumerate(data[31])
			],
		)
		cls.addList(metadata)
		cls.add("farming", metadata)
