from typing import List

from definitions.misc.world6.FarmingLandRankUpgrade import FarmingLandRankUpgrade
from helpers.HelperFunctions import getFromMixedArray
from repositories.master.Repository import Repository


class FarmingLandRankUpgradeRepo(Repository[FarmingLandRankUpgrade]):
	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/6"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["NinjaInfo"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromMixedArray(cls.getSection())
		# NinjaInfo[34..37]: names, descriptions, base bonuses, total-rank requirements.
		names = data[34]
		descriptions = data[35]
		baseBonuses = data[36]
		totalRankRequirements = data[37]

		for index, name in enumerate(names):
			toAdd = FarmingLandRankUpgrade(
				index=index,
				name=name,
				description=descriptions[index],
				baseBonus=baseBonuses[index],
				totalRankRequirement=totalRankRequirements[index],
			)
			cls.addList(toAdd)
			cls.add(f"{index}", toAdd)
