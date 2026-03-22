from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class BubbaUpgrade(IdleonModel):
    name: str
    x0: Numeric
    costExponent: Numeric
    bonus: Integer
    maxLevel: Integer
    x2: Integer
    x3: Integer
    description: str
