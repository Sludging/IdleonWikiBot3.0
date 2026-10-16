from typing import List

from definitions.misc.Companion import Companion
from helpers.HelperFunctions import getFromSplitArray
from repositories.enemies.EnemyDetailsRepo import EnemyDetailsRepo
from repositories.master.Repository import Repository


class CompanionRepo(Repository[Companion]):
	@classmethod
	def getCategory(cls) -> str:
		return "Misc"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["Companion"]


	@classmethod
	def generateRepo(cls) -> None:
		for bonus in getFromSplitArray(cls.getSection()):
			toAdd = Companion.fromList(bonus)
			cls.add(toAdd.id, toAdd)
			cls.addList(toAdd)

	@classmethod
	def getWikiName(cls, name: str) -> str:
		return EnemyDetailsRepo.getWikiName(name)

