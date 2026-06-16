from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class GambitBonus(IdleonModel):
	index: Integer
	x0: Numeric
	x1: Numeric
	description: str
	name: str 
