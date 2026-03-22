from typing import Dict

from definitions.itemdef.ItemSet import ItemSet
from repositories.master.FileRepository import FileRepository


class WikiSetRepo(FileRepository[ItemSet]):

	@classmethod
	def getCategory(cls) -> str:
		return "Item/Sources"

	@classmethod
	def parse(cls, value: Dict[str, any]) -> ItemSet:
		return ItemSet.parse_obj(value)

	@classmethod
	def generateRepo(cls) -> None:
		raise NotImplementedError(
			"WikiSetRepo cannot regenerate from wiki. The cached JSON is the source of truth."
		)
