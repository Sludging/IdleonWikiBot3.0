from typing import List

from definitions.misc.world5.GamingSuperbit import GamingSuperbit
from helpers.HelperFunctions import getFromArrayArray
from repositories.master.Repository import Repository


class GamingSuperbitsRepo(Repository[GamingSuperbit]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/5"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["GamingSuperbits"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromArrayArray(cls.getSection())
		for index, line in enumerate(data):
			superbit = GamingSuperbit.fromList(line + [index])
			cls.addList(superbit)
			cls.add(str(superbit.superbitId), superbit)
