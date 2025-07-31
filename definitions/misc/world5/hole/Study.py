from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class Study(IdleonModel):
	index: Integer
	name: str
	description: str
	multiplier: Numeric 
