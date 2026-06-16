from typing import List
from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class MonumentUnlock(IdleonModel):
	index: Integer
	description: str
	hours_required: Numeric


class MonumentBonus(IdleonModel):
	index: Integer
	description: str
	multiplier: Numeric


class Monument(IdleonModel):
	index: Integer
	name: str
	unlocks: List[MonumentUnlock]
	bonuses: List[MonumentBonus] 
