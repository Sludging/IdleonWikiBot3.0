from typing import Dict

from definitions.common.Note import Note
from repositories.enemies.EnemyDetailsRepo import EnemyDetailsRepo
from repositories.master.FileRepository import FileRepository


class EnemyNoteRepo(FileRepository[Note]):

	@classmethod
	def initDependencies(cls, log = True) -> None:
		EnemyDetailsRepo.initialise(cls.codeReader, log)

	@classmethod
	def getCategory(cls) -> str:
		return "Enemy"

	@classmethod
	def parse(cls, value: Dict[str, any]) -> Note:
		return Note.parse_obj(value)

	@classmethod
	def generateRepo(cls) -> None:
		raise NotImplementedError(
			"EnemyNoteRepo cannot regenerate from wiki. The cached JSON is the source of truth."
		)
