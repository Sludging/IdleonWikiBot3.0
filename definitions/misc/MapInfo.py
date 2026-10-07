from typing import List

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class MapInfo(IdleonModel):
	id: Integer
	portalRequirements: List[Integer]
	maxOnScreen: Integer
	# MapDetails coordinates, retaining raw sentinel values.
	x: Integer
	y: Integer
