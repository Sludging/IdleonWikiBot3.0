from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class JellyOperatorUpgrade(IdleonModel):
    index: Integer
    displayIndex: Integer
    name: str
    maxLevel: Integer
    costExponent: Numeric
    bonusPerLevel: Numeric
    costMultiplier: Numeric
    description: str
