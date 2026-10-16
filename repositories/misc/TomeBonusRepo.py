from typing import List

from definitions.misc.TomeBonus import TomeBonus
from helpers.HelperFunctions import getFromMixedArray
from repositories.master.Repository import Repository


class TomeBonusRepo(Repository[TomeBonus]):
	@classmethod
	def getCategory(cls) -> str:
		return "Misc"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["NinjaInfo"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromMixedArray(cls.getSection())
		# NinjaInfo[33] contains the six Tome bonus descriptions.
		for index, description in enumerate(data[33]):
			toAdd = TomeBonus(index=index, description=description)
			cls.addList(toAdd)
			cls.add(f"{index}", toAdd)
