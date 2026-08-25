from typing import List

from definitions.misc.world5.hole.FountainCurrency import FountainCurrency
from definitions.misc.world5.hole.HoleOrder import HoleOrder
from helpers.HelperFunctions import getFromLiteralArrayEntry, getFromNestedSplitArray
from repositories.master.Repository import Repository


class FountainCurrencyRepo(Repository[FountainCurrency]):
	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/5/Hole"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["FountainUpgrade", "HoleInfo"]

	@classmethod
	def generateRepo(cls) -> None:
		groups = getFromNestedSplitArray(cls.getSection(0))
		currencyIndices = sorted({int(row[3]) for group in groups for row in group if len(row) > 3})
		currencyNames = [
			"Bronze Coins",
			"Silver Coins",
			"Golden Coins",
			"Dollar Bills",
			"Credit Bills",
			"Treasury Bills",
			"Moolah Stacks",
			"Shilling Stacks",
			"Greane Stacks",
		]
		if not currencyIndices:
			raise ValueError("Fountain upgrades do not contain currency indices")
		if max(currencyIndices) >= len(currencyNames):
			raise ValueError("Fountain currency names do not cover all source indices")

		iconEntries = getFromLiteralArrayEntry(
			cls.getSection(1),
			HoleOrder.FountainCurrencyIcons.value,
		)
		if len(iconEntries) != 1:
			raise ValueError("HoleInfo Fountain currency icon map must contain one string")
		iconMap = iconEntries[0]

		for index in currencyIndices:
			holesResourceIndex = 30 + index
			if holesResourceIndex >= len(iconMap):
				raise ValueError(f"Fountain currency icon map is missing index {holesResourceIndex}")
			currency = FountainCurrency(
				index = index,
				name = currencyNames[index],
				holesResourceIndex = holesResourceIndex,
				icon = iconMap[holesResourceIndex],
			)
			cls.addList(currency)
			cls.add(str(index), currency)
