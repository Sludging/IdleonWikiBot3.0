from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class ClamworksBonus(IdleonModel):
    description: str
    value: Integer
    cost: Numeric
