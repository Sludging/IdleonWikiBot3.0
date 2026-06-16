from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric
from helpers.HelperFunctions import replaceUnderscores


class CompassUpgrade(IdleonModel):
	name: str
	baseCost: Integer
	costMult: Numeric
	dustType: Integer
	maxLevel: Integer
	bonusValue: Numeric
	x2: Integer
	x3: Integer
	x4: Integer
	x5: Integer
	x6: Integer
	description: str
	# Computed
	upgradeType: str
	