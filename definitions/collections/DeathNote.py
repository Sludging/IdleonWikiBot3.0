from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class DeathNoteMob(IdleonModel):
	sourceId: str
	world: Integer
	order: Integer
