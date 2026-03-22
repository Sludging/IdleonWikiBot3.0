from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class ZenithMarket(IdleonModel):
    name: str
    unlockCost: Numeric
    costExponent: Numeric
    maxLevel: Integer
    bonusPerLevel: Numeric
    x1: Integer
    description: str
