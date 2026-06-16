from typing import List

from definitions.misc.world5.hole.HoleOrder import HoleOrder
from definitions.misc.world5.hole.CosmoUpgrade import CosmoUpgrade
from helpers.HelperFunctions import getFrom4dArray, getFromMixedArray
from repositories.master.Repository import Repository


class CosmoUpgradeRepo(Repository[CosmoUpgrade]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/5/Hole"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["CosmoUpgrades", "HoleInfo"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFrom4dArray(cls.getSection())
		holeInfo = getFromMixedArray(cls.getSection(1))

		for n, colour in enumerate(data[0]):
			enhanceForColour = holeInfo[HoleOrder.CosmoUpgradeEnhance.value + n][0]
			for upgradeIndex, upgrade in enumerate(colour):
				upgrade.append(n + 1)

				maxEnhance = enhanceForColour[upgradeIndex]
				upgrade.append(maxEnhance)

				cls.addList(CosmoUpgrade.fromList(upgrade))
				if cls.contains(upgrade[2]): continue
				cls.add(upgrade[2], CosmoUpgrade.fromList(upgrade))
