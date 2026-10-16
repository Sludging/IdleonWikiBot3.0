from typing import List

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class PlantStagePaletteLuck(IdleonModel):
	# Zero-based evolution index stored on a plant.
	plantStage: Integer
	multiplier: Numeric


class LogMinigameRank(IdleonModel):
	rank: Integer
	deathCardCount: Integer
	# Garden time advanced by a successful Bog Log pick, not a cooldown.
	progressHours: Integer


class RatShopUpgrade(IdleonModel):
	upgradeId: Integer
	label: str


class GamingMetadata(IdleonModel):
	plantStagePaletteLuck: List[PlantStagePaletteLuck]
	logMinigameRanks: List[LogMinigameRank]
	ratShopUpgrades: List[RatShopUpgrade]
