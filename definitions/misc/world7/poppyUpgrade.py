from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric


class PoppyUpgrade(IdleonModel):
    name: str
    x0: Numeric
    x1: Numeric
    unlock: Numeric
    desc: str
    x2: Numeric
