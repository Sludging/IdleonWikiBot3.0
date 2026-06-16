from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric


class OrionUpgrade(IdleonModel):
    name: str
    x0: Numeric
    x1: Numeric
    unlock: Numeric
    desc: str
    x2: Numeric
