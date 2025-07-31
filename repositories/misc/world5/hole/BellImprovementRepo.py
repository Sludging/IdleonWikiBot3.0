from typing import List

from definitions.misc.world5.hole.BellImprovement import BellImprovement
from definitions.misc.world5.hole.HoleOrder import HoleOrder
from helpers.HelperFunctions import getFromMixedArray, replaceUnderscores
from repositories.master.Repository import Repository


class BellImprovementRepo(Repository[BellImprovement]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/5/Hole"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["HoleInfo"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromMixedArray(cls.getSection())
		
		# Get bell improvement data from holesInfo array
		baseValues = data[HoleOrder.BellImprovementCosts.value]
		bonuses = data[HoleOrder.BellImprovementCharges.value]
		
		# Define the 6 resources required for improvements
		resources = [
			"Coins",
			"Mythril", 
			"Bits",
			"Eighth Note",
			"Atoms",
			"Turquoise Rupie"
		]
		
		# Create bell improvement entries
		for i in range(len(resources)):
			bellImprovement = BellImprovement(
				index=i,
				baseValue=baseValues[i] if i < len(baseValues) else "0",
				bonus=replaceUnderscores(bonuses[i]) if i < len(bonuses) else "",
				resource=resources[i]
			)
			cls.addList(bellImprovement)
			cls.add(bellImprovement.index, bellImprovement)
		
