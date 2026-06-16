from typing import Dict, List

from definitions.common.Note import Note
from definitions.questdef.NpcNote import NpcNote
from repositories.master.FileRepository import FileRepository


class NpcNoteRepo(FileRepository[NpcNote]):
	@classmethod
	def getCategory(cls) -> str:
		return "Npc"

	@classmethod
	def parse(cls, value: Dict[str, any]) -> NpcNote:
		return NpcNote.parse_obj(value)

	@classmethod
	def getSections(cls) -> List[str]:
		return ["Quests", "Quests2"]

	@classmethod
	def generateRepo(cls) -> None:
		raise NotImplementedError(
			"NpcNoteRepo cannot regenerate from wiki. The cached JSON is the source of truth."
		)

	@classmethod
	def getNote(cls, npc: str, qName: str) -> Note:
		if not cls.contains(npc):
			return Note(note = " ")
		npcNotes = cls.get(npc).notes
		if qName not in npcNotes:
			return Note(note = " ")
		return npcNotes[qName]
