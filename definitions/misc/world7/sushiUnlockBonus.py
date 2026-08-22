from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class SushiUnlockBonus(IdleonModel):
    index: Integer
    bonus: Numeric
