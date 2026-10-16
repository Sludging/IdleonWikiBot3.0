from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class MineheadOpponent(IdleonModel):
    progressionIndex: Integer
    displayId: Integer
    name: str
    ordinalLabel: str
    titleLabel: str
    bonusDescription: str
    bonusValue: Integer
