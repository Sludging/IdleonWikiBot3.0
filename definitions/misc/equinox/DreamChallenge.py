from typing import Optional

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class DreamChallenge(IdleonModel):
	challenge: str
	req: Integer
	reward: str
	filler: str
	# Numeric value associated with the reward, when one exists. Formula-based
	# percentage rewards use their additive percentage-point value.
	bonusValue: Optional[Numeric] = None
