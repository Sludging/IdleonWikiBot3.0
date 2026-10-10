from typing import Dict

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class RoyalGuardianMetadata(IdleonModel):
	outpostKillRequirementOverrides: Dict[str, Integer]
