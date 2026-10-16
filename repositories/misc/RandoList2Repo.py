from typing import List

from definitions.misc.RandoList import RandoList
from helpers.HelperFunctions import getFromMixedArray
from repositories.master.Repository import Repository


class RandoList2Repo(Repository[RandoList]):
	@classmethod
	def getCategory(cls) -> str:
		return "Misc"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["GamingMetadata"]

	@classmethod
	def generateRepo(cls) -> None:
		for index, elements in enumerate(getFromMixedArray(
			cls.getSection(), replaceUnderscores=False, formatSubSection=False, respectDelimiter=True
		)):
			item = RandoList(elements=elements)
			cls.addList(item)
			cls.add(str(index), item)
