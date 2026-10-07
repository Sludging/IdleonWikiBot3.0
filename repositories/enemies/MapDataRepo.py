from typing import List

from definitions.enemy.MapData import MapData
from helpers.Constants import Constants
from helpers.HelperFunctions import getFromSplit
from repositories.master.Repository import Repository
from repositories.misc.MapNameRepo import MapNameRepo
from repositories.misc.MapPortalsRepo import MapPortalsRepo


class MapDataRepo(Repository[MapData]):
	"""
	Requires: MapNameRepo
	"""

	@classmethod
	def getCategory(cls) -> str:
		return "Enemy"

	@classmethod
	def initDependencies(cls, log = True) -> None:
		MapNameRepo.initialise(cls.codeReader, log)
		MapPortalsRepo.initialise(cls.codeReader, log)

	@classmethod
	def getSections(cls) -> List[str]:
		return ["MapEnemies"]

	@classmethod
	def generateRepo(cls) -> None:
		mapEnemies = getFromSplit(cls.getSection())
		for n, v in enumerate(mapEnemies):
			worldIndex = n // 50
			if worldIndex >= len(Constants.worldNames):
				continue
			if n >= MapPortalsRepo.lengthList():
				break
			mapPortals = MapPortalsRepo.getList(n)
			toAdd = MapData(
				enemy = v,
				map = MapNameRepo.getList(n),
				world = Constants.worlds[worldIndex],
				portalRequirements = mapPortals.portalRequirements,
				x = mapPortals.x,
				y = mapPortals.y
			)
			cls.addList(toAdd)
			if cls.contains(v):
				continue
			cls.add(v, toAdd)
