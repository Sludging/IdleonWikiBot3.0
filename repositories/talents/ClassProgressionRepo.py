from typing import List

from definitions.talents.ClassProgression import (
	ClassAccountBonus,
	ClassFamilyBonus,
	ClassProgression,
	ClassPromotionChoice,
	ClassSpecializeSkill,
)
from helpers.HelperFunctions import getFromArrayArray, getFromMixedArray, getFromSplit
from repositories.master.Repository import Repository


class ClassProgressionRepo(Repository[ClassProgression]):
	@classmethod
	def getCategory(cls) -> str:
		return "Talents"

	@classmethod
	def getSections(cls) -> List[str]:
		return [
			"ClassNames",
			"ClassFamilyBonuses",
			"ClassFamilyBonusDISPorder",
			"ClassSpecializeSkills",
			"ClassAccountBonus",
			"ClassPromotionChoices",
		]

	@classmethod
	def generateRepo(cls) -> None:
		classNames = getFromSplit(cls.getSection(0))
		familyRows = getFromMixedArray(cls.getSection(1), replaceUnderscores = False)
		displayRows = getFromArrayArray(cls.getSection(2), repU = False)
		specializeRows = getFromSplit(cls.getSection(3))
		accountRows = getFromMixedArray(cls.getSection(4), replaceUnderscores = False)
		promotionRows = getFromMixedArray(cls.getSection(5), replaceUnderscores = False)

		def valueAt(row: List[str], index: int, default = "_"):
			return row[index] if index < len(row) else default

		familyBonuses = [
			ClassFamilyBonus(
				index = index,
				bonus = valueAt(row, 0, ""),
				x1 = valueAt(row, 1),
				x2 = valueAt(row, 2),
				func = valueAt(row, 3, ""),
				y1 = valueAt(row, 4),
				y2 = valueAt(row, 5),
				funcY = valueAt(row, 6, ""),
			)
			for index, row in enumerate(familyRows)
		]
		specializeSkills = [
			ClassSpecializeSkill(index = index, skill = skill)
			for index, skill in enumerate(specializeRows)
		]
		accountBonuses = [
			ClassAccountBonus(
				index = index,
				bonus = valueAt(row, 0, ""),
				x1 = valueAt(row, 1, "0"),
			)
			for index, row in enumerate(accountRows)
		]
		promotionChoices = [
			ClassPromotionChoice(
				index = index,
				choices = [value for value in row if value not in {"", "Na"}],
			)
			for index, row in enumerate(promotionRows)
		]

		toAdd = ClassProgression(
			classNames = classNames,
			familyBonuses = familyBonuses,
			familyBonusDisplayOrder = displayRows[0] if displayRows else [],
			specializeSkills = specializeSkills,
			accountBonuses = accountBonuses,
			promotionChoices = promotionChoices,
		)
		cls.add("0", toAdd)
		cls.addList(toAdd)
