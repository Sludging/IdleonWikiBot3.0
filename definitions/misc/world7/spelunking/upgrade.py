from pydantic import BaseModel

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class SpelunkingUpgrade(IdleonModel):
    name: str
    costBase: Integer
    costIncrement: Numeric
    maxLevel: Integer
    bonusPerLevel: Integer
    x1: Integer
    requiredUpgrades: Integer
    column: Integer
    x2: Integer
    x3: Integer
    dash1: str
    dash2: str
    description: str
    dash3: str
    
    
