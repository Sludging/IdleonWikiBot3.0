from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class BigFishBonus(IdleonModel):
    name: str
    desc: str
    x0: Numeric
    x1: Numeric
    filler: str
