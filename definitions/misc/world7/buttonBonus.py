from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class ButtonBonus(IdleonModel):
    index: Integer
    name: str
    bonusPerPress: Numeric
