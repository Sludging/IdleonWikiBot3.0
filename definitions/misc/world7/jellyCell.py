from typing import List, Optional

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class JellyCell(IdleonModel):
    index: Integer
    name: str
    tileCount: Integer
    footprintOffsets: List[Integer]
    passiveDescription: Optional[str] = None
    damageCoefficient: Numeric
    attackCooldownCoefficient: Integer
