import os.path
import re
from abc import ABC, abstractmethod
from typing import Dict, Generic, Optional, TypeVar, List, Any

from definitions.master.IdleonEnum import IdleonEnum
from definitions.master.IdleonModel import IdleonModel
from helpers.CodeReader import CodeReader
from helpers.ColourPrinter import printGreen, printRed
from helpers.HelperFunctions import extractImportsClass
from helpers.JsonEncoder import CompactJSONEncoder

T = TypeVar("T", bound = IdleonModel)


class Repository(Generic[T], ABC):
	sections: List[str]
	codeReader: CodeReader
	repository: Dict[str, T]
	listRepository: List[T]

	@classmethod
	def initialise(cls, codeReader: CodeReader, log: bool = True, export: bool = True) -> None:
		if cls.__dict__.get("codeReader"):
			if cls.codeReader.version == codeReader.version:
				return
		cls.log = log
		cls.repository = {}
		cls.listRepository = []
		cls.codeReader = codeReader
		cls.sections = cls.getSections()
		if cls.sections and not cls.getSection():
			printRed(f"Could not find {cls.__name__}'s Section")
			return None
		cls.initDependencies(log)
		cls.generateRepo()
		cls.generateTSRepo()
		if log:
			printGreen(f"Generated {cls.__name__}'s repo with {len(cls.repository)} Items")

		if export:
			cls._export()

	@classmethod
	def getSections(cls) -> List[str]:
		return []

	@classmethod
	def initDependencies(cls, log = True) -> None:
		pass

	@classmethod
	def generateRepo(cls) -> None:
		raise NotImplementedError

	@classmethod
	def getSection(cls, index: int = 0) -> str:
		currentSection = cls.codeReader.getSection(cls.sections[index])
		assert currentSection is not None
		return currentSection

	@classmethod
	def get(cls, key: str) -> Optional[T]:
		return cls.repository.get(key)

	@classmethod
	def getList(cls, index: int) -> Optional[T]:
		return cls.listRepository[index]

	@classmethod
	def add(cls, key: str, value: T) -> None:
		cls.repository[key] = value

	@classmethod
	def addList(cls, value: T) -> None:
		cls.listRepository.append(value)

	@classmethod
	def lengthList(cls) -> int:
		return len(cls.listRepository)

	@classmethod
	def contains(cls, key: str) -> bool:
		return key in cls.repository

	@classmethod
	def items(cls):
		return cls.repository.items()

	@classmethod
	def itemsList(cls):
		return cls.listRepository

	@classmethod
	@abstractmethod
	def getCategory(cls) -> str:
		raise NotImplementedError

	@classmethod
	def getFilePath(cls) -> str:
		return f"{cls.getCategory()}/{cls.__name__}"

	@classmethod
	def _getPath(cls, location: str, fileExtension: str, nameOveride = "", noCat = False) -> str:
		"""

		Args:
			location: the base file location
			fileExtension: the extension of the file
			nameOveride: what to call the file, defaults to class name
			noCat: whether to include a category or not

		Returns:
			the created file path
		"""
		if noCat:
			path = fr"./exported/{location}/"
		else:
			path = fr"./exported/{location}/{cls.getCategory()}/"
		if not os.path.isdir(path):
			os.makedirs(path, exist_ok = True)
		if not nameOveride:
			return f"{path}{cls.__name__}.{fileExtension}"
		return f"{path}{nameOveride}.{fileExtension}"

	@classmethod
	def _export(cls) -> None:
		with open(cls._getPath("repo", "json"), mode = "w", encoding = "utf-8") as outfile:
			outfile.write(CompactJSONEncoder(indent = 4).encode(cls.repository))
		if not cls.listRepository:
			return
		with open(cls._getPath("list", "json"), mode = "w", encoding = "utf-8") as outfile:
			outfile.write(CompactJSONEncoder(indent = 4).encode(cls.listRepository))

	@classmethod
	def excludeDefaults(cls) -> bool:
		return True

	@classmethod
	def getFirstKey(cls) -> str:
		return list(cls.repository.keys())[0]

	@classmethod
	def getFirstElement(cls) -> T:
		return cls.get(cls.getFirstKey())

	@classmethod
	def generateTSRepo(cls):
		def all_subclasses(cls):
			return set(cls.__subclasses__()).union(
				[s for c in cls.__subclasses__() for s in all_subclasses(c)])

		for subclass in all_subclasses(IdleonModel):
			tsRepr = subclass.toTsInterface()
			name = subclass.__name__[0].lower() + subclass.__name__[1:] + "Model"
			path = cls._getPath("ts/model", "ts", noCat = True, nameOveride = name)
			with open(path, "w") as infile:
				infile.write(tsRepr)

		for enum in all_subclasses(IdleonEnum):
			name = enum.__name__[0].lower() + enum.__name__[1:] + "Enum"
			path = cls._getPath("ts/enum", "ts", noCat = True, nameOveride = name)
			tsEnum = f"export enum {enum.__name__}Enum ""{\n"
			out = []
			for e in enum:
				out.append(f"    {e.name} = \"{e.name}\"")
			tsEnum += ",\n".join(out)
			tsEnum += "\n}\n"
			with open(path, "w") as infile:
				infile.write(tsEnum)

		path = cls._getPath("ts/data", "ts", noCat = True)
		tsData = ""
		imports = set()

		if not cls.listRepository:
			tsData += cls.getFirstElement().toTsClass(False)
			className = cls.getFirstElement().getHighestClass().__name__
			imports.add(f"{className}Model")
			tsData += "\n\n\n\n"
			tsData += f"export const init{cls.__name__} = () => ""{\n    return [    \n"
			for n, (atr, val) in enumerate(cls.items()):
				tsObj, toImport = val.toTs()
				[imports.add(x) for x in toImport]
				tsData += f"        new {className}Base(\"{atr}\", {tsObj})"
				if n != len(cls.items()) - 1:
					tsData += ",\n"
			tsData += "    \n]\n}\n"
		else:
			tsData += cls.getList(0).toTsClass(True)
			className = cls.getFirstElement().getHighestClass().__name__
			imports.add(f"{className}Model")
			tsData += "\n\n\n\n"
			tsData += f"export const init{cls.__name__} = () => ""{\n    return [    \n"
			for n, val in enumerate(cls.listRepository):
				tsObj, toImport = val.toTs()
				[imports.add(x) for x in toImport]
				tsData += f"        new {className}Base({n}, {tsObj})"
				if n != len(cls.listRepository) - 1:
					tsData += ",\n"
			tsData += "    \n]\n}\n"
		tsData = extractImportsClass(imports) + tsData
		with open(path, "w", encoding = "utf-8") as infile:
			infile.write(tsData)
