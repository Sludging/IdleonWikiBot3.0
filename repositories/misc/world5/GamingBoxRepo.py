from typing import List

from definitions.misc.world5.GamingBox import GamingBox
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class GamingBoxRepo(Repository[GamingBox]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/5"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["GamingBoxes"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for index, line in enumerate(data):
			box = GamingBox.fromList(line + [index])
			cls.addList(box)
			cls.add(str(box.boxId), box)
