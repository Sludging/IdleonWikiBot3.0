from typing import List

from definitions.misc.world2.AlchemyVial import AlchemyVial
from helpers.HelperFunctions import getFromArrayArray, getFromSplit
from repositories.master.Repository import Repository


class AlchemyVialRepo(Repository[AlchemyVial]):
	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/2"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["AlchemyVialQTYreq", "AlchemyVialItems", "AlchemyVialItemsPCT"]

	@classmethod
	def generateRepo(cls) -> None:
		qtyRows = getFromArrayArray(cls.getSection(0), repU = False)
		toAdd = AlchemyVial(
			qtyRequirements = qtyRows[0] if qtyRows else [],
			items = getFromSplit(cls.getSection(1)),
			percentages = getFromSplit(cls.getSection(2)),
		)
		cls.add("0", toAdd)
		cls.addList(toAdd)
