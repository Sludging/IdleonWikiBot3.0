from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class OrbletMarketBonus(IdleonModel):
    index: Integer
    name: str
    costBase: Numeric
    costMultiplier: Numeric
    maxLevel: Integer
    bonusPerLevel: Numeric
    x1: Integer
    description: str
