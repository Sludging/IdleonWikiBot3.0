from typing import Dict, List

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class AchievementGoldBallBonus(IdleonModel):
	achievementIndex: Integer
	bonus: Integer


class AchievementMetadata(IdleonModel):
	worldToAchievementOrdering: Dict[str, List[Integer]]
	steam2Registration: List[Integer]
	goldBallBonuses: List[AchievementGoldBallBonus]
