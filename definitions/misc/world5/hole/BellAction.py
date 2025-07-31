from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class BellAction(IdleonModel):
	index: Integer
	actionType: str
	description: str 
