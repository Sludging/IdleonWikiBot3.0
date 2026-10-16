from typing import List

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Boolean, Integer


class MainQuest(IdleonModel):
	npc: str
	map: List[Integer]
	scene: List[Integer]
	index: List[Integer]


class AccountWideQuest(IdleonModel):
	key: str
	npc: str
	index: Integer
	accountWide: Boolean


class QuestMetadata(IdleonModel):
	mainQuests: List[MainQuest]
	accountWideQuests: List[AccountWideQuest]
