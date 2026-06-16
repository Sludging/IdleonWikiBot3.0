from typing import List

from definitions.misc.world5.hole.BellAction import BellAction
from definitions.misc.world5.hole.HoleOrder import HoleOrder
from helpers.HelperFunctions import getFromMixedArray, replaceUnderscores
from repositories.master.Repository import Repository


class BellActionRepo(Repository[BellAction]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/5/Hole"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["HoleInfo"]

	@classmethod
	def generateRepo(cls) -> None:
		# Define the 4 bell action types
		actionTypes = [
			"Ring",
			"Ping", 
			"Clean",
			"Renew"
		]
		
		descriptions = [
			"Ring the bell to get +1 LV of a random bonus",
			"Ping the bell to find an Opal instantly",
			"Clean the bell for a % chance to unlock a new improvement method", 
			"Renew the bell to reset all bonuses but keep improvement methods and opals"
		]
		
		# Create bell action entries
		for i in range(len(actionTypes)):
			bellAction = BellAction(
				index=i,
				actionType=actionTypes[i],
				description=descriptions[i]
			)
			cls.addList(bellAction)
			cls.add(bellAction.index, bellAction)
		
		
