import re
from typing import List

import numpy as np

from definitions.common.Source import Source

reAll = r'[ a-zA-Z0-_\'n()@,!$+{}%:.~-]'


def getFromSplitArray(v: str) -> List[List[str]]:
	"""
	Converts a section into a list of strings based upon the exportation of an array represented as
	"0 1 2 3 4 5 6 7 8 9".split(" ")
	Args:
		v:

	Returns:

	"""
	section = formatStr(v, ["  ", "\n"])
	subSections = re.findall(fr'"({reAll}*)"\.', section)
	subSections = [x.split(" ") for x in subSections]
	newList = []
	for subSection in subSections:
		internalList = []
		for i in range(len(subSection)):
			internalList.append(replaceUnderscores(subSection[i]))
		newList.append(internalList[:])
	return newList


def getFromSplit(v: str) -> List[str]:
	"""
	Converts a section into a list of strings based upon the exportation of an array represented as
	"0 1 2 3 4 5 6 7 8 9".split(" ")
	Args:
		v:

	Returns:

	"""
	section = formatStr(v, ["  ", "\n"])
	subSections = re.findall(fr'"({reAll}*)"\.', section)
	return subSections[0].split(" ")


def getFromArrayArray(v: str) -> List[List[str]]:
	"""
	Converts a string representation of a 2d array into an actual 2d array
	Args:
		v:

	Returns:

	"""
	section = formatStr(v, ["  ", "\n"])
	subSections = section.split("],[")
	return [strToArray(x) for x in subSections]


def getFrom4dArray(v: str) -> List[List[List[List[str]]]]:
	section = formatStr(v, ["\n", "  "])
	subSections = [wrap(x) for x in re.split(r"],?],?],\[\[\[", section)]
	outer = []
	for subSection in subSections:
		subSubSections = [wrap(x) for x in re.split(r",?],?],\[\[", subSection)]
		mid = []
		for subSubSection in subSubSections:
			subSubSubSection = [wrap(x) for x in re.split(r",?],\[", subSubSection)]
			inner = []
			for subSubSubSection in subSubSubSection:
				inner.append(strToArray(subSubSubSection))
			mid.append(inner.copy())
		outer.append(mid.copy())
	return outer


def isRecipe(name: str) -> bool:
	return name[:-1] == "SmithingRecipes"


def isTalent(name: str) -> bool:
	return name[:-1] == "TalentBook"


def formatFloat(v: float) -> str:
	return np.format_float_positional(v)


def camelCaseSplitter(string: str) -> List[str]:
	"""
	Splits a string base on camel case.
	eg: camelCaseSplitter("helloThere") = ["hello", "There"]

	Args:
		string: The string to split on

	Returns:
		A list of strings split based on camel case

	"""
	return re.sub("([A-Z][a-z]+)", r" \1", re.sub("([A-Z]+)", r" \1", string)).split()


def camelCaseToTitle(string: str) -> str:
	"""
	Converts Camel Case to a title
	eg: camelCaseToTitle("helloThere") = "Hello There"
	Args:
		string: The string to conver

	Returns:
		The string as a title

	"""
	return " ".join(map(lambda x: x.title(), camelCaseSplitter(string)))


def formatStr(val: str, remove: List[str] = [], replaceUnderscores: bool = False) -> str:
	"""Formats the given string by first stripping the left and right, then removes all occurrences of all strings
		inside the remove list and finally replaces underscores with a space

	Args:
		val (str): [The string to be formatted]
		remove (List[str], optional): [A list of substrings to be removed from the input string]. Defaults to [].
		replaceUnderscores (bool, optional): [Whether to replace underscores with spaces]. Defaults to False.

	Returns:
		str: [The formatted string]
	"""
	if val:
		for rep in remove:
			val = val.replace(rep, "")
		if replaceUnderscores:
			val = val.replace("_", " ")
			if val[0] != "|":
				val = val.replace("|", " ")
		return val.lstrip().rstrip()
	return val


def scientificToInt(val: str) -> int:
	"""Converts a string reprisenting an integer in scientific notion to the corresponding integer

	Eg: scientificToInt("4e2") = "400"

	Args:
		val (str): the string to convert

	Returns:
		int: the resulting integer
	"""
	if "e" in val:
		return int(float(val))
	return int(val)


def replaceUnderscores(val: str) -> str:
	return formatStr(val, replaceUnderscores = True)


def wrap(v: str) -> str:
	return f"[[{v}]]"


def strToArray(v: str) -> List[str]:
	"""
	Converts a string reprisentation of a list to an actual python list
	strToArray("[1,2,3,4]") = ["1", "2", "3", "4"]
	Args:
		v: [str] the string to convert

	Returns:
		the resulting list

	"""
	string = v.replace(",_", "&&&&")
	parts = formatStr(string, ["[", "]", '"', "return", ";", "\n", "{", "}"]).split(",")
	return [formatStr(x).replace("&&&&", ", ") for x in parts if formatStr(x).replace("&&&&", ", ") != ""]


def changeChestNames(intName, name):
	"""

	Args:
		intName: the internal name of the enemy
		name: the dislpay name of the enemy

	Returns:
		A more descriptive version of the chests name

	"""
	COLNAMES = ["Dewdrop", "Sandstone", "Chillsnap", "NYI", "NYI", "NYI", "NYI", "NYI", "NYI"]
	col = int(intName[6]) - 1
	return f"{COLNAMES[col]} {name}"


def wikiSource(source: Source) -> str:
	return source.wikiName
