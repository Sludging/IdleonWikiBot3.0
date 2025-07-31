from typing import List

from definitions.misc.world5.hole.Sediment import Sediment
from helpers.HelperFunctions import getFromMixedArray, replaceUnderscores
from repositories.master.Repository import Repository


class SedimentRepo(Repository[Sediment]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/5/Hole"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["HoleInfo"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromMixedArray(cls.getSection())
		
		# Get sediment unlock requirements from holesInfo[21]
		unlockRequirements = data[21]
		
		# Define sediment names in order
		sedimentNames = [
			"Gravel",
			"Goldust", 
			"Redstone",
			"Mythril",
			"Cobaltine",
			"Bruntine",
			"Freezium",
			"Sweetium",
			"Rad Coral",
			"Hyper Coral"
		]
		
		# Process each sediment
		for i in range(len(sedimentNames)):
			sediment = Sediment(
				index=i,
				name=sedimentNames[i],
				unlockRequirement=replaceUnderscores(unlockRequirements[i]) if i < len(unlockRequirements) else ""
			)
			cls.addList(sediment)
			cls.add(f"{i}", sediment) 
