from typing import Optional

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class Sushi(IdleonModel):
    index: Integer
    name: str
    unlockDescription: str
    unlockBonus: Numeric
    knowledgeBonusCategory: Optional[str]
    knowledgeBonusBase: Optional[Numeric]
