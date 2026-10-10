from typing import Dict

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class MapMetadata(IdleonModel):
	nonAfkScreenDestinations: Dict[str, Integer]
