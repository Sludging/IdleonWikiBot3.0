from typing import List

from definitions.misc.AchievementMetadata import AchievementGoldBallBonus, AchievementMetadata
from helpers.Constants import Constants
from helpers.HelperFunctions import getFromArrayArray
from repositories.master.Repository import Repository


class AchievementMetadataRepo(Repository[AchievementMetadata]):
	@classmethod
	def getCategory(cls) -> str:
		return "Misc"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["AchieveOrderingz", "AchSteam2Reg", "AchBallzBonuses"]

	@classmethod
	def generateRepo(cls) -> None:
		orderingData = getFromArrayArray(cls.getSection())
		steam2Registration = [int(value) for value in getFromArrayArray(cls.getSection(1))[0]]
		goldBallSection = cls.codeReader.getSection("AchBallzBonuses")
		goldBallData = getFromArrayArray(goldBallSection) if goldBallSection else []

		metadata = AchievementMetadata(
			worldToAchievementOrdering = {
				world: ordering
				for world, ordering in zip(Constants.worlds[:len(orderingData)], orderingData)
			},
			steam2Registration = steam2Registration,
			goldBallBonuses = [
				AchievementGoldBallBonus(achievementIndex = pair[0], bonus = pair[1])
				for pair in goldBallData
			]
		)
		cls.add("metadata", metadata)
		cls.addList(metadata)
