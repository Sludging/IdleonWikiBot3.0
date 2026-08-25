from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class FountainCurrency(IdleonModel):
	index: Integer
	name: str
	holesResourceIndex: Integer
	icon: str
