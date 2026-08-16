from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class MineheadButtonBonus(IdleonModel):
    index: Integer
    bonusPerCycle: Numeric
