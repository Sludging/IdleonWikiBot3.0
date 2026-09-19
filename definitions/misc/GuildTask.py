from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class GuildTask(IdleonModel):
	task: str
	requirement: Integer
	guildPoints: Integer
