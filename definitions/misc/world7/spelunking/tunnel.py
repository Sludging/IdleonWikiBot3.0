from typing import List

from definitions.master.IdleonModel import IdleonModel
from definitions.misc.world7.spelunking.discovery import SpelunkingDiscovery
from helpers.CustomTypes import Integer


class SpelunkingTunnel(IdleonModel):
    index: Integer
    name: str
    loreBonus: str
    bossDepth: Integer
    discoveries: List[SpelunkingDiscovery]
    
    
