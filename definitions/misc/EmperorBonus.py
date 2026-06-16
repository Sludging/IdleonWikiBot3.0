from typing import List

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class EmperorBonus(IdleonModel):
	"""
	Represents emperor bonus data from the EmperorBon function.
	Contains 12 bonuses with their names, values, and level mappings.
	"""
	bonusId: Integer  # Index of the bonus (0-11)
	bonusName: str  # Display name/description of the bonus
	bonusValue: Integer  # Base value of the bonus
	levelMappings: List[Integer]  # List of emperor levels that provide this bonus 
