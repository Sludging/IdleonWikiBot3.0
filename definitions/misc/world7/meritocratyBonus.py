from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class MeritocratyBonus(IdleonModel):
    text: str
    bonus: Numeric
    value: Integer
