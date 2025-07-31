from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class BellImprovement(IdleonModel):
	index: Integer
	baseValue: str
	bonus: str
	resource: str 
