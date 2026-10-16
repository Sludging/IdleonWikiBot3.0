from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class RoyalStatue(IdleonModel):
    index: Integer
    description: str
    baseBonus: Numeric
    bonusPerLevel: Numeric
    unlockItem: str
    unlockChanceDenominator: Integer
    upgradeItem: str
    attemptCost: Integer
