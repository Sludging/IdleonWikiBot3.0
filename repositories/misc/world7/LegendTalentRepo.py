from typing import List

from definitions.misc.world7.legendTalent import LegendTalent
from helpers.HelperFunctions import getFromSplitArray, replaceUnderscores
from repositories.master.Repository import Repository


class LegendTalentRepo(Repository[LegendTalent]):
	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/7"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["LegendTalents"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for line in data:
			toAdd = LegendTalent(
				name=replaceUnderscores(line[0]),
				maxLevel=line[1],
				bonusValue=line[2],
				x3=line[3],
				bonus=replaceUnderscores(line[4]),
				description=replaceUnderscores(line[5]),
			)
			cls.addList(toAdd)
			cls.add(toAdd.name, toAdd)
