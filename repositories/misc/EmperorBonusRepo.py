from typing import List

from definitions.misc.EmperorBonus import EmperorBonus
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class EmperorBonusRepo(Repository[EmperorBonus]):

	@classmethod
	def getCategory(cls) -> str:
		return "Misc"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["EmperorBon"]

	@classmethod
	def generateRepo(cls) -> None:
		# EmperorBon function returns 3 arrays:
		# Array 1: Bonus names/descriptions (12 items)
		# Array 2: Bonus values (12 items)
		# Array 3: Level mappings (48 items) - which bonus applies to each level 0-47
		data = getFromSplitArray(cls.getSection())
		
		bonusNames = data[0]  # Array 1: 12 bonus names
		bonusValues = data[1]  # Array 2: 12 bonus values
		levelMappings = data[2]  # Array 3: 48 level mappings
		
		# Create 12 EmperorBonus objects, one for each bonus
		for i in range(12):
			# Find all levels that use this bonus
			levels_for_bonus = []
			for level, bonus_index in enumerate(levelMappings):
				if int(bonus_index) == i:
					levels_for_bonus.append(level)
			
			toAdd = EmperorBonus(
				bonusId = i,
				bonusName = bonusNames[i],
				bonusValue = int(bonusValues[i]),
				levelMappings = levels_for_bonus
			)
			cls.add(f"{i}", toAdd)
			cls.addList(toAdd) 
