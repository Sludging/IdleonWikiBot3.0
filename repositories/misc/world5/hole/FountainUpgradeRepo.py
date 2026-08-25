from typing import List

from definitions.misc.world5.hole.FountainUpgrade import FountainUpgrade
from definitions.misc.world5.hole.HoleOrder import HoleOrder
from helpers.HelperFunctions import getFromMixedArray, getFromNestedSplitArray
from repositories.master.Repository import Repository


class FountainUpgradeRepo(Repository[FountainUpgrade]):
	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/5/Hole"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["FountainUpgrade", "HoleInfo"]

	@classmethod
	def generateRepo(cls) -> None:
		groups = getFromNestedSplitArray(cls.getSection(0))
		holeInfo = getFromMixedArray(cls.getSection(1), replaceUnderscores = False)
		restrictionIndex = HoleOrder.FountainMarbleizationRestrictions.value
		if len(holeInfo) <= restrictionIndex:
			raise ValueError("HoleInfo does not contain Fountain marbleization restrictions")

		marbleizeRestrictions = set(holeInfo[restrictionIndex])
		for waterIndex, group in enumerate(groups):
			for index, row in enumerate(group):
				if len(row) != 8:
					raise ValueError(f"Fountain upgrade {waterIndex}_{index} has {len(row)} fields, expected 8")

				key = f"{waterIndex}_{index}"
				upgrade = FountainUpgrade(
					waterIndex = waterIndex,
					index = index,
					name = row[0],
					prerequisiteIndex = row[1],
					uiPosition = row[2],
					costCurrencyIndex = row[3],
					baseCost = row[4],
					costMultiplier = row[5],
					bonusPerLevel = row[6],
					description = row[7],
					marbleizeEligible = key not in marbleizeRestrictions,
				)
				cls.addList(upgrade)
				cls.add(key, upgrade)
