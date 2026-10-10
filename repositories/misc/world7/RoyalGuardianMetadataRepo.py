import re
from decimal import Decimal
from typing import List

from definitions.misc.world7.royalGuardianMetadata import RoyalGuardianMetadata
from repositories.master.Repository import Repository


class RoyalGuardianMetadataRepo(Repository[RoyalGuardianMetadata]):
	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/7"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["RG_KillReq"]

	@classmethod
	def generateRepo(cls) -> None:
		assignments = re.findall(
			r"\.h\[(\d+)\]\s*=\s*([+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?)(?=\s*[,;)])",
			cls.getSection(),
		)
		metadata = RoyalGuardianMetadata(
			outpostKillRequirementOverrides = {
				mapId: int(Decimal(value)) for mapId, value in assignments
			},
		)
		cls.add("metadata", metadata)
		cls.addList(metadata)
