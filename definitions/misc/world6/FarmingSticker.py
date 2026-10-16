from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class FarmingSticker(IdleonModel):
	index: Integer
	name: str
	description: str
	bonusPerSticker: Numeric
