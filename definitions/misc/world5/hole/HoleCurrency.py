from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class HoleCurrency(IdleonModel):
	index: Integer
	kind: str
	localIndex: Integer
	name: str
	icon: str
