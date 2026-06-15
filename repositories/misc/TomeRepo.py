from typing import List

from definitions.misc.Tome import Tome
from helpers.HelperFunctions import getFromMixedArray, getFromSplitArray, replaceUnderscores
from repositories.master.Repository import Repository


class TomeRepo(Repository[Tome]):

	@classmethod
	def getCategory(cls) -> str:
		return "Misc"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["TomeInfo", "NinjaInfo"]

	@classmethod
	def generateRepo(cls) -> None:
		tomeData = getFromSplitArray(cls.getSection(0))
		ninjaInfo = getFromMixedArray(cls.getSection(1))
		uiOrder = [int(x) for x in ninjaInfo[32]]
		uiOrderMap = {lineId: pos for pos, lineId in enumerate(uiOrder)}

		for n, bonus in enumerate(tomeData):
			tome = Tome.fromList([*bonus, uiOrderMap.get(n, len(uiOrder) + n)], {"filler"})
			cls.add(replaceUnderscores(bonus[0]), tome)
			cls.addList(tome)
