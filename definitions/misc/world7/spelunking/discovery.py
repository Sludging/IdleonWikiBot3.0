from pydantic import BaseModel

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class SpelunkingDiscovery(IdleonModel):
    tunnelIndex: Integer
    name: str
    x1: Numeric
    x2: Integer
    x3: Numeric
    x4: Integer
    x5: Integer
    x6: Integer
    x7: Numeric | str
    
    
