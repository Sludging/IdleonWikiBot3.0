from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class HoleBuilding(IdleonModel):
	name: str
	squareImageType: Integer
	costType: str
	baseCost: Integer
	costCalcType: bool
	desc: str
	order: Integer
	costCurrencyId: Integer
