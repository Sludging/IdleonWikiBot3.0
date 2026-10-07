from typing import Dict, Union, Callable, List

from definitions.master.IdleonModel import IdleonModel
from definitions.misc.MapName import MapName
from helpers.CustomTypes import Integer


class MapData(IdleonModel):
	"""MapDetails map coordinates retain the game's raw sentinel values."""
	enemy: str
	world: str
	map: MapName
	portalRequirements: List[Integer]
	x: Integer
	y: Integer

	def getMapName(self) -> str:
		return self.map.name

	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		return {"area": self.getMapName, "world": "world"}
