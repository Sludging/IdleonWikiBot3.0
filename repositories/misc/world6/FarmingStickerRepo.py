from typing import List

from definitions.misc.world6.FarmingSticker import FarmingSticker
from helpers.HelperFunctions import getFromMixedArray
from repositories.master.Repository import Repository


class FarmingStickerRepo(Repository[FarmingSticker]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/6"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["Research"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromMixedArray(cls.getSection(), respectDelimiter = True)
		# Research[23-25] stores sticker names, description templates, and base coefficients.
		names, descriptions, bonuses = data[23], data[24], data[25]
		# Original table indices also identify the associated seed types.
		for index, name in enumerate(names):
			if name == "Nonexistent Sticker":
				continue
			toAdd = FarmingSticker(
				index = index,
				name = name,
				description = descriptions[index],
				bonusPerSticker = bonuses[index],
			)
			cls.addList(toAdd)
			cls.add(str(index), toAdd)
