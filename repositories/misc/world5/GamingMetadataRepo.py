import json
from typing import List

from definitions.misc.world5.GamingMetadata import (
	GamingMetadata,
	LogMinigameRank,
	PlantStagePaletteLuck,
	RatShopUpgrade,
)
from helpers.HelperFunctions import getFromSplit, getFromSplitArray, replaceUnderscores
from repositories.master.Repository import Repository


class GamingMetadataRepo(Repository[GamingMetadata]):
	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/5"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["GamingMetadata", "GamingPlantStagePaletteLuck", "GamingRatShopUpgrades"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		# The split-array helper retains .split("") as one string; read its digits locally.
		deathCardCounts = list("".join(data[6]))
		progressHours = data[7]
		# ExtraLuckFromEvo clamps the stored plant stage to this table's indices 0..7.
		plantLuck = getFromSplit(cls.getSection(1))

		# CodeReader excludes the opening semantic literal prefix and closing quote.
		ratSection = next(section for section in cls.codeReader.sections if section.sectionName == cls.sections[2])
		ratText = json.loads(ratSection.start + cls.getSection(2) + '"')
		ratUpgrades = []
		for upgradeId, row in enumerate(ratText.split("|")):
			ratUpgrades.append(RatShopUpgrade(
				upgradeId = upgradeId,
				label = replaceUnderscores(row.replace(",", " ", 1)),
			))

		metadata = GamingMetadata(
			plantStagePaletteLuck = [
				PlantStagePaletteLuck(plantStage = stage, multiplier = multiplier)
				for stage, multiplier in enumerate(plantLuck)
			],
			# Bog Log clamps death cards at rank 9 and time rewards at rank 12.
			# Rank 12 also represents every higher rank, despite longer source arrays.
			logMinigameRanks = [
				LogMinigameRank(
					rank = rank,
					deathCardCount = deathCardCounts[min(rank, 9)],
					progressHours = progressHours[min(rank, 12)],
				)
				for rank in range(13)
			],
			ratShopUpgrades = ratUpgrades,
		)
		cls.addList(metadata)
		cls.add("gaming", metadata)
