from typing import List

from definitions.collections.DeathNote import DeathNoteMob
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class DeathNoteRepo(Repository[DeathNoteMob]):
	@classmethod
	def getCategory(cls) -> str:
		return "Enemy"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["DeathNoteMobs"]

	@classmethod
	def generateRepo(cls) -> None:
		worlds = getFromSplitArray(cls.getSection(), replaceUnderscores = False)[:7]
		index = 0
		for world, mobs in enumerate(worlds):
			for order, sourceId in enumerate(mobs):
				toAdd = DeathNoteMob(sourceId = sourceId, world = world, order = order)
				# Source IDs are intentionally not keys: some event/duplicate IDs
				# can recur, while the flattened list must retain source order.
				cls.add(str(index), toAdd)
				cls.addList(toAdd)
				index += 1
