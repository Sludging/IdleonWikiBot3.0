import re
from decimal import Decimal
from typing import List

from definitions.misc.MapMetadata import MapMetadata
from repositories.master.Repository import Repository


class MapMetadataRepo(Repository[MapMetadata]):
	@classmethod
	def getCategory(cls) -> str:
		return "Misc"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["NonAFKscreens"]

	@classmethod
	def generateRepo(cls) -> None:
		assignments = re.findall(
			r"\.h\[\s*(\d+)\s*\]\s*=\s*([+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?)(?=\s*[,);])",
			cls.getSection(),
		)
		metadata = MapMetadata(
			nonAfkScreenDestinations = {
				mapId: int(Decimal(destination)) for mapId, destination in assignments
			},
		)
		cls.add("metadata", metadata)
		cls.addList(metadata)
