from typing import List

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class CropScientistBonus(IdleonModel):
	index: Integer
	description: str
	unlockUpgradeIndex: Integer


class FarmingMetadata(IdleonModel):
	cropScientistBonuses: List[CropScientistBonus]
