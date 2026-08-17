from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class ResearchGridBonus(IdleonModel):
    index: Integer
    name: str
    maxLevel: Integer
    bonusPerLevel: Numeric
    x3: Integer
    x4: Integer
    description: str
