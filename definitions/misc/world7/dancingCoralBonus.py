from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class DancingCoralBonus(IdleonModel):
    name: str
    itemSource: str
    desc: str
    cost: Integer
    bonus: Integer
