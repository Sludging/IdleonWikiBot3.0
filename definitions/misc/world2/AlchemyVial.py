from typing import List

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class AlchemyVial(IdleonModel):
	qtyRequirements: List[Integer]
	items: List[str]
	percentages: List[Numeric]
