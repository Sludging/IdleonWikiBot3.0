from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class JellyObstruction(IdleonModel):
    index: Integer
    name: str
    description: str
    bonusValue: Numeric
