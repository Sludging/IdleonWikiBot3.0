from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class Sediment(IdleonModel):
	index: Integer
	name: str
	unlockRequirement: Numeric 
