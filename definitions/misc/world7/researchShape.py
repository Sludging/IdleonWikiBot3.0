from typing import List

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class ResearchPoint(IdleonModel):
    x: Integer
    y: Integer


class ResearchShape(IdleonModel):
    index: Integer
    name: str
    vertices: List[ResearchPoint]
    width: Integer
    height: Integer
    bonusPercent: Numeric
    descriptionTemplate: str
