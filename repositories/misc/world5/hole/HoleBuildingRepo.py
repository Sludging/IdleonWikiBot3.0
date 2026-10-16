from typing import List

from definitions.misc.world5.hole.HoleBuilding import HoleBuilding
from definitions.misc.world5.hole.HoleOrder import HoleOrder
from helpers.HelperFunctions import getFromSplitArray, getFromMixedArray
from repositories.master.Repository import Repository
from repositories.misc.world5.hole.HoleCurrencyRepo import HoleCurrencyRepo


class HoleBuildingRepo(Repository[HoleBuilding]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/5/Hole"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["HoleBuilding", "HoleInfo"]

	@classmethod
	def initDependencies(cls, log = True) -> None:
		HoleCurrencyRepo.initialise(cls.codeReader, log)

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		holeInfo = getFromMixedArray(cls.getSection(1))
		order = holeInfo[HoleOrder.BuildingOrder.value]

		for line, o in zip(data, order):
			rawID = int(line[2])
			currency = HoleCurrencyRepo.get(str(rawID))
			if currency is None:
				raise ValueError(f"Unknown Hole currency ID {rawID} for building {line[0]}")
			line[2] = currency.name
			building = HoleBuilding.fromList(line + [o, rawID])
			cls.addList(building)
			if cls.contains(line[0]): continue
			cls.add(line[0], building)
