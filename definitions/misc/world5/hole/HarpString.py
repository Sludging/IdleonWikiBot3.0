from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class HarpString(IdleonModel):
	stringId: Integer
	stringLetter: str
	description: str
	multiplier: Integer
