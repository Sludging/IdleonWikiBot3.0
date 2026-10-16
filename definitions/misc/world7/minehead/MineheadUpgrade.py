from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class MineheadUpgrade(IdleonModel):
    index: Integer
    name: str
    maxLevel: Integer
    costExponent: Numeric
    quantityPerLevel: Numeric
    rawField4: Integer
    description: str
