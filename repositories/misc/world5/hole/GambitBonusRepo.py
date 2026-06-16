from typing import List
import re

from definitions.misc.world5.hole.GambitBonus import GambitBonus
from definitions.misc.world5.hole.HoleOrder import HoleOrder
from helpers.HelperFunctions import getFromMixedArray, replaceUnderscores
from repositories.master.Repository import Repository


class GambitBonusRepo(Repository[GambitBonus]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/5/Hole"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["HoleInfo"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromMixedArray(cls.getSection(), formatSubSection=False)
		
		# Get gambit bonus data from holesInfo array
		gambitConfigs = data[HoleOrder.GambitConfig.value]
		
		# Process each gambit bonus configuration
		for i in range(len(gambitConfigs)):
			config = gambitConfigs[i]
			
			parts = config.split('|') 

			if len(parts) < 4:
				raise ValueError(f"Gambit bonus config {i} has less than 4 parts: {parts}")
			
			
			x0 = float(parts[0])
			x1 = float(parts[1])
			description = replaceUnderscores(parts[2])
			name = replaceUnderscores(parts[3])
			
			# Clean up unwanted characters
			name = re.sub(r'[梦而]', '', name)
			name = name.replace("(TAP ME)", "")
			name = name.strip()
			
			gambitBonus = GambitBonus(
				index=i,
				x0=x0,
				x1=x1,
				description=description,
				name=name
			)
			cls.addList(gambitBonus)
			cls.add(f"{i}", gambitBonus) 
