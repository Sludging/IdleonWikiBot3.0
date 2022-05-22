from __future__ import annotations

import enum
import re
from typing import List, Dict, Union, Callable, Set

from pydantic import BaseModel

from helpers.CustomTypes import Integer, Numeric
from helpers.HelperFunctions import strToArray


class IdleonModel(BaseModel):
	@classmethod
	def toTS(cls):
		def getType(typ: type | str):
			reGetTypeName = re.compile(r"\.(\w*)(?:$|')")
			reGetTypeEnum = re.compile(r"enum '(\w*)'")
			baseType = typeMap.get(typ)
			print("GET TYPE", typ, baseType)
			if baseType:
				return baseType
			if "enum" in str(typ):
				enumName = reGetTypeEnum.findall(str(typ))[0]
				toImport.add(enumName)
				return enumName
			if "Union" in str(typ):
				innerTypes = strToArray(str(typ).replace("typing.Union", ""))
				innerTypes = [getType(x) for x in innerTypes]
				[toImport.add(x) for x in innerTypes]
				return "(" + " | ".join(innerTypes) + ")"
			typeName = reGetTypeName.findall(str(typ))[0]
			toImport.add(typeName)
			return typeName

		def toLowerCamel(imp: str) -> str:
			return imp[0].lower() + imp[1:]

		typeMap = {
			str: "string",
			Integer: "number",
			Numeric: "number",
			int: "number",
			float: "number",
			"helpers.CustomTypes.Integer": "number",
			bool: "bool",
			Union[Integer, float]: "number"
		}

		res = f"interface {cls.__name__} ""{\n"
		fields = cls.__fields__

		toImport = set()
		for name, field in fields.items():
			print(f"{name}")
			res += f"    {name}: "
			print(field.outer_type_, field.type_)
			if not isinstance(field.outer_type_, type) and field.outer_type_ not in typeMap:
				outer = str(field.outer_type_)
				if "Dict" in outer:
					typ = getType(field.type_)
					res += f"Record<string, {typ}>"
				elif "List" in outer:
					typ = getType(field.type_)
					res += typ + "[]"
				elif "Tuple" in outer:
					types = strToArray(outer.replace("typing.Tuple", ""))
					tupleTypes = []
					for typ in types:
						typ = getType(typ)
						tupleTypes.append(typ)
					res += "[" + ", ".join(tupleTypes) + "]"
				res += ",\n"
				continue
			typ = getType(field.type_)
			res += typ + ",\n"
		res = res[:-2] + "\n"
		res += "}"

		for imp in toImport:
			res = "import { "f"{imp}"" } from "f"'./{toLowerCamel(imp)}';\n" + res
		print(res)

	@classmethod
	def fromList(cls, data: List[any]) -> IdleonModel:
		keys = cls.__fields__.keys()
		if len(keys) != len(data):
			raise ValueError(f"Error in creating {cls.__name__}:\n"
			                 f" Length of object keys ({len(keys)}) does not match length of input data "
			                 f"({len(data)})")
		return cls.parse_obj({key: val for key, val in zip(keys, data)})

	def shouldCompare(self) -> bool:
		return True

	def compareKey(self) -> str:
		"""

		Returns: in lists of items what key to create compare dicts from
		Examples: eg item name in rewards from quests

		"""
		return ""

	def sortKey(self) -> str:
		"""

		Returns: the element to sort the changelogs by
		Examples:sort items by type, bubbles by cauldron

		"""
		return ""

	def isFiller(self) -> bool:
		"""
		Returns: True if the element was in the code but was filler
		Examples: item name being FILLER

		"""
		return False

	def writeWiki(self, newLine = True, ignoreZero = True) -> str:
		res = ""
		for wiki, atr in self.intToWiki().items():
			if isinstance(atr, str):
				cVal = self.dict()[atr]
				if (not cVal or cVal in {"00"}) and ignoreZero:
					continue
				res += f"|{wiki}={self.dict()[atr]}"
				if newLine:
					res += "\n"
			else:
				if atr():
					res += f"|{wiki}={atr()}"
					if newLine:
						res += "\n"
		self.dict()

		return res

	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		return {}

	def writeAfter(self) -> List[IdleonModel]:
		return []

	def toDict(self, ignored: Set[str] = set()) -> Dict[str, any]:
		firstIter = {}
		for atr, val in self:
			if isinstance(val, IdleonModel) and val.shouldCompare():
				subDict = val.toDict(ignored)
				if not subDict:
					firstIter[atr] = subDict
					continue
				if len(subDict.keys()) > 1:
					firstIter[atr] = subDict
					continue
				key = list(subDict.keys())[0]
				firstIter[atr] = subDict[key]
				continue
			if isinstance(val, list) and val:
				if not val:
					continue
				if isinstance(val[0], IdleonModel) and val[0].shouldCompare():
					firstIter[atr] = [x.toDict(ignored) for x in val]
					continue
			if isinstance(val, dict) and val:
				key = list(val.keys())[0]
				if isinstance(val[key], IdleonModel) and val[key].shouldCompare():
					firstIter[atr] = {k: v.toDict(ignored) for k, v in val.items()}
					continue
			if isinstance(val, enum.Enum):
				firstIter[atr] = val.name
				continue
			firstIter[atr] = val

		for ignore in ignored:
			firstIter.pop(ignore, None)
		return firstIter

	def compare(self, other: IdleonModel, ignored: Set[str] = set()):
		diffs = {}
		d1 = self.__dict__
		d2 = other.__dict__
		keys = d1.keys()
		for key in keys:
			if d1[key] == d2[key]:
				continue
			if key in ignored:
				continue
			if isinstance(d1[key], IdleonModel) and d1[key].shouldCompare():
				if len(d1[key].__fields__) > 1:
					diffs[key] = d1[key].compare(d2[key], ignored)
					continue
				firstKey = list(dict(d1[key]).keys())[0]
				if isinstance(dict(d1[key])[firstKey], list):  # Remove the Drop: Drop: [] iteration
					diffs[key] = self._getDifList(dict(d1[key])[firstKey], dict(d2[key])[firstKey], ignored)
					continue
				diffs[key] = d1[key].compare(d2[key], ignored)
				continue
			if isinstance(d1[key], list):
				diffs[key] = self._getDifList(d1[key], d2[key], ignored)
				continue
			if isinstance(d1[key], dict):
				diffs[key] = self._getDifDict(d1[key], d2[key], ignored)
				continue
			if isinstance(d1[key], enum.Enum):
				diffs[key] = (d1[key].name, d2[key].name)
				continue
			diffs[key] = (d1[key], d2[key])
		if not any(diffs.values()):
			return {}
		return diffs

	def _getDifList(self, me, other, ignored: Set[str] = set()) -> Dict[str, any]:
		if isinstance(me[0], IdleonModel) and me[0].compareKey():
			return self._getDifListIdleon(me, other, ignored)
		res = {}
		len1 = len(me)
		len2 = len(other)

		if len1 == len2:
			for i in range(len1):
				if me[i] == other[i]:
					continue
				if isinstance(me[i], IdleonModel) and me[i].shouldCompare():
					res[str(i)] = (me[i].compare(other[i], ignored))
					continue
				res[str(i)] = (me[i], other[i])
		elif len1 < len2:

			for i in range(len1):
				if me[i] == other[i]:
					continue
				if isinstance(me[i], IdleonModel) and me[i].shouldCompare():
					res[str(i)] = (me[i].compare(other[i], ignored))
					continue
				res[str(i)] = (me[i], other[i])
			for n, i in enumerate(other[len1:len2]):
				res[str(n)] = (" ", i)
		else:
			for i in range(len2):
				if me[i] == other[i]:
					continue
				if isinstance(me[i], IdleonModel) and me[i].shouldCompare():
					res[str(i)] = (me[i].compare(other[i], ignored))
					continue
				res[str(i)] = (me[i], other[i])
			for n, i in enumerate(other[len2:len1]):
				res[str(n)] = (i, " ")
		if not any(res.values()):
			return {}
		return res

	def _getDifListIdleon(self, me, other, ignored: Set[str] = set()) -> Dict[str, any]:
		meD = {x.compareKey(): {"model": x, "index": str(n)} for n, x in enumerate(me)}
		otherD = {x.compareKey(): {"model": x, "index": str(n)} for n, x in enumerate(other)}

		diffs = {}
		keys1 = set(meD.keys())
		keys2 = set(otherD.keys())
		sameItems = keys1.intersection(keys2)
		newItems = keys2 - keys1
		for key in sameItems:
			if meD[key]["model"] == otherD[key]["model"]:
				continue
			if key in ignored:
				continue
			if isinstance(meD[key]["model"], IdleonModel) and meD[key]["model"].shouldCompare():
				diffs[meD[key]["index"]] = meD[key]["model"].compare(otherD[key]["model"], ignored)
				continue
			if isinstance(meD[key]["model"], list):
				diffs[meD[key]["index"]] = self._getDifList(meD[key]["model"], otherD[key]["model"], ignored)
				continue
			if isinstance(meD[key]["model"], dict):
				diffs[meD[key]["index"]] = self._getDifDict(meD[key]["model"], otherD[key]["model"], ignored)
				continue
			diffs[meD[key]["index"]] = (meD[key]["model"], otherD[key]["model"])

		for key in newItems:
			if isinstance(otherD[key]["model"], IdleonModel) and otherD[key]["model"].shouldCompare():
				toAdd = otherD[key]["model"].toDict(ignored)
				diffs[otherD[key]["index"]] = {}
				for atr, val in toAdd.items():
					if isinstance(val, list):
						diffs[otherD[key]["index"]][atr] = []
						for elem in val:
							diffs[otherD[key]["index"]][atr].append((" ", elem))
						continue
					diffs[otherD[key]["index"]][atr] = (" ", val)
				continue
			diffs[otherD[key]["index"]] = (" ", otherD[key]["model"])

		if not any(diffs.values()):
			return {}
		return diffs

	def _getDifDict(self, me, other, ignored: Set[str] = set()) -> Dict[str, any]:
		diffs = {}
		keys1 = set(me.keys())
		keys2 = set(other.keys())
		sameItems = keys1.intersection(keys2)
		newItems = keys2 - keys1
		for key in sameItems:
			if me[key] == other[key]:
				continue
			if key in ignored:
				continue
			if isinstance(me[key], IdleonModel) and me[key].shouldCompare():
				diffs[key] = me[key].compare(other[key], ignored)
				continue
			if isinstance(me[key], list):
				diffs[key] = self._getDifList(me[key], other[key], ignored)
				continue
			if isinstance(me[key], dict):
				diffs[key] = self._getDifDict(me[key], other[key], ignored)
				continue
			diffs[key] = (me[key], other[key])

		for key in newItems:
			if isinstance(other[key], IdleonModel) and other[key].shouldCompare():
				toAdd = other[key].toDict(ignored)
				diffs[key] = {}
				for atr, val in toAdd.items():
					if isinstance(val, list):
						diffs[key][atr] = []
						for elem in val:
							diffs[key][atr].append((" ", elem))
						continue
					diffs[key][atr] = (" ", val)
				continue
			diffs[key] = (" ", other[key])

		if not any(diffs.values()):
			return {}
		return diffs

	'''
		def _getDifList(self, me, other, ignored: Set[str] = set()) -> Dict[str, any]:
		res = {}
		len1 = len(me)
		len2 = len(other)

		if len1 == len2:
			for i in range(len1):
				if me[i] == other[i]:
					continue
				if isinstance(me[i], IdleonModel) and me[i].shouldCompare():
					res[str(i)] = (me[i].compare(other[i], ignored))
					continue
				res[str(i)] = (me[i], other[i])
		elif len1 < len2:

			for i in range(len1):
				if me[i] == other[i]:
					continue
				if isinstance(me[i], IdleonModel) and me[i].shouldCompare():
					res[str(i)] = (me[i].compare(other[i], ignored))
					continue
				res[str(i)] = (me[i], other[i])
			for n, i in enumerate(other[len1:len2]):
				res[str(n)] = (" ", i)
		else:
			for i in range(len2):
				if me[i] == other[i]:
					continue
				if isinstance(me[i], IdleonModel) and me[i].shouldCompare():
					res[str(i)] = (me[i].compare(other[i], ignored))
					continue
				res[str(i)] = (me[i], other[i])
			for n, i in enumerate(other[len2:len1]):
				res[str(n)] = (i, " ")

		return res'''
