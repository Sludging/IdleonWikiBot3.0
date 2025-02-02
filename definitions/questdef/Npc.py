from typing import List, Dict

from definitions.master.IdleonModel import IdleonModel
from definitions.questdef.DialogueLine import DialogueLine
from definitions.questdef.NpcHead import NpcHead
from definitions.questdef.Quest import Quest


class Npc(IdleonModel):
	head: NpcHead
	quests: Dict[str, Quest]
	dialogue: List[DialogueLine]
