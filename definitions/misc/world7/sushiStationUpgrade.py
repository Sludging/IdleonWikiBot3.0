from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class SushiStationUpgrade(IdleonModel):
    index: Integer
    displayOrder: Integer
    name: str
    maxLevel: Integer
    costExponent: Numeric
    bonusPerLevel: Numeric
    costMultiplier: Numeric
    description: str
