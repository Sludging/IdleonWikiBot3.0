from typing import Dict

from definitions.common.Note import Note
from repositories.master.FileRepository import FileRepository


class ItemNoteRepo(FileRepository[Note]):

	@classmethod
	def getCategory(cls) -> str:
		return "Item/Sources"

	@classmethod
	def parse(cls, value: Dict[str, any]) -> Note:
		return Note.parse_obj(value)

	@classmethod
	def generateRepo(cls) -> None:
		raise NotImplementedError(
			"ItemNoteRepo cannot regenerate from wiki. The cached JSON is the source of truth."
		)
