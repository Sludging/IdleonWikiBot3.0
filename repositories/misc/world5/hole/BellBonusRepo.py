from typing import List

from definitions.misc.world5.hole.BellBonus import BellBonus
from definitions.misc.world5.hole.HoleOrder import HoleOrder
from helpers.HelperFunctions import getFromMixedArray, replaceUnderscores
from repositories.master.Repository import Repository


class BellBonusRepo(Repository[BellBonus]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/5/Hole"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["HoleInfo"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromMixedArray(cls.getSection())
		
		# Get bell bonus data from holesInfo array
		bellBonuses = data[HoleOrder.BellBonusTypes.value]
		
		# Process bell bonuses in pairs (description, value)
		for i in range(0, len(bellBonuses), 2):
			if i + 1 < len(bellBonuses):
				bellBonus = BellBonus(
					index=i // 2,
					description=replaceUnderscores(bellBonuses[i]),
					value=replaceUnderscores(bellBonuses[i + 1])
				)
				cls.addList(bellBonus)
				cls.add(bellBonus.index, bellBonus)
		
		
