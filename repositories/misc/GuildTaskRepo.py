from typing import List

from definitions.misc.GuildTask import GuildTask
from helpers.HelperFunctions import getFromArrayArray
from repositories.master.Repository import Repository


class GuildTaskRepo(Repository[GuildTask]):
	@classmethod
	def getCategory(cls) -> str:
		return "Misc"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["GuildGPtasks"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromArrayArray(cls.getSection())
		for index, task in enumerate(data):
			toAdd = GuildTask.fromList(task)
			cls.add(str(index), toAdd)
			cls.addList(toAdd)
