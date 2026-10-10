from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class FarmingLandRankUpgrade(IdleonModel):
	index: Integer
	name: str
	description: str
	baseBonus: Numeric
	totalRankRequirement: Integer
