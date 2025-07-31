from typing import List

from definitions.misc.world5.hole.HarpString import HarpString
from definitions.misc.world5.hole.HoleOrder import HoleOrder
from helpers.HelperFunctions import getFromMixedArray, replaceUnderscores
from repositories.master.Repository import Repository


class HarpStringsRepo(Repository[HarpString]):
	"""
	Repository for extracting Harp Strings data
	"""
	
	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/5/Hole"
	
	@classmethod
	def getSections(cls) -> List[str]:
		return ["HoleInfo"]
	
	@classmethod
	def generateRepo(cls) -> None:
		data = getFromMixedArray(cls.getSection())
		
		# Get harp chord descriptions from index 45
		chordDescriptionsData = data[HoleOrder.HarpStringDescriptions.value]
		
		# String letters
		stringLetters = ["C", "D", "E", "F", "G", "A", "B"]
		
		# Extract string configuration data
		for i in range(7):
			description = replaceUnderscores(chordDescriptionsData[i]) if i < len(chordDescriptionsData) else ""
			
			harpString = HarpString(
				stringId=i,
				stringLetter=stringLetters[i],
				description=description
			)
			
			cls.addList(harpString)
			cls.add(harpString.stringId, harpString) 
