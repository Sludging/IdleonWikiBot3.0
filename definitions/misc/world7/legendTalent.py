from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class LegendTalent(IdleonModel):
	name: str
	maxLevel: Integer
	bonusValue: Numeric
	x3: str
	bonus: str
	description: str
