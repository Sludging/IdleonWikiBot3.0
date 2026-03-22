from typing import Dict

from definitions.common.Source import Source
from definitions.itemdef.Sources import Sources
from repositories.master.FileRepository import FileRepository


class WikiSourceRepo(FileRepository[Sources]):

	@classmethod
	def getCategory(cls) -> str:
		return "Item/Sources"

	@classmethod
	def parse(cls, value: Dict[str, any]) -> Sources:
		return Sources.parse_obj(value)

	@classmethod
	def generateRepo(cls) -> None:
		raise NotImplementedError(
			"WikiSourceRepo cannot regenerate from wiki. The cached JSON is the source of truth."
		)

	@classmethod
	def addToSource(cls, item: str, source: Source):
		if not cls.contains(item):
			cls.add(item, Sources())
		cls.get(item).sources.append(source)
