from typing import List

from definitions.enemy.Titan import Titan
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class TitanRepo(Repository[Titan]):
	@classmethod
	def getCategory(cls) -> str:
		return "Enemy"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["Titans"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection(), replaceUnderscores = False)
		for index, row in enumerate(data):
			# The wrapped function's default CodeReader delimiter can run into
			# CompanionDB. Titan rows are the contiguous 13-field prefix.
			if len(row) != 13:
				break
			toAdd = Titan.fromList(row)
			# Titan names are source labels; the source-order index is the stable
			# key so roster order and any repeated labels are never lost.
			cls.add(str(index), toAdd)
			cls.addList(toAdd)
