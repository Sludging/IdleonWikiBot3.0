from typing import List

from definitions.master.IdleonModel import IdleonModel
from definitions.misc.world4.TerritoryEnemy import TerritoryEnemy
from helpers.CustomTypes import Numeric


class TerritoryFight(IdleonModel):
	img: str
	spiceForage: Numeric
	fightPower: Numeric
	forCostUP: Numeric
	battleName: str
	filler1: str
	filler2: str
	filler3: str
	enemies: List[TerritoryEnemy]

