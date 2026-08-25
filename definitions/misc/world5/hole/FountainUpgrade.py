from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Boolean, Integer, Numeric


class FountainUpgrade(IdleonModel):
	waterIndex: Integer
	index: Integer
	name: str
	prerequisiteIndex: Integer
	uiPosition: str
	costCurrencyIndex: Integer
	baseCost: Numeric
	costMultiplier: Numeric
	bonusPerLevel: Numeric
	description: str
	marbleizeEligible: Boolean
