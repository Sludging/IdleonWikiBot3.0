from typing import List

from definitions.misc.world5.GamingPalette import GamingPalette
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class GamingPaletteRepo(Repository[GamingPalette]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/5"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["GamingPalette"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for line in data:
			cls.addList(GamingPalette.fromList(line))
			if cls.contains(line[3]): continue
			cls.add(line[3], GamingPalette.fromList(line))
