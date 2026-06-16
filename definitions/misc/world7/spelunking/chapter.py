from pydantic import BaseModel
from typing import List

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric

class ChapterBonus(IdleonModel):
    bonus: str
    x1: Integer
    x2: Integer
    func: str
    x3: Integer
    requiredPages: Integer
    x4: Integer
    x5: Integer

class SpelunkingChapter(IdleonModel):
    name: str
    bonuses: List[ChapterBonus]
