from typing import Optional

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class SpelunkingToolUnlock(IdleonModel):
    kind: str
    upgradeIndex: Optional[Integer] = None
    minimumBonus: Optional[Integer] = None


class SpelunkingTool(IdleonModel):
    index: Integer
    name: str
    baseStaminaCost: Integer
    hitRadius: Integer
    damageMultiplier: Integer
    unlock: SpelunkingToolUnlock
