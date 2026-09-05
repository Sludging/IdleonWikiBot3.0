from typing import Optional

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class RoyalArmoryUpgrade(IdleonModel):
    index: Integer
    displayOrder: Optional[Integer]
    name: str
    costBase: Numeric
    costExponent: Numeric
    resourceType: Integer
    maxLevel: Integer
    bonusPerLevel: Numeric
    requiredUpgrades: Optional[Integer]
    x1: Integer
    x2: Integer
    description: str
