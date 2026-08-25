import json
import re
from typing import List, Set

import numpy as np
from tree_sitter import Language, Node, Parser
import tree_sitter_javascript

from helpers.Constants import Constants

reAll = r'[ a-zA-Z0-_\'n()@,#!$+{/}%:.~\-&\|/\*\u4E00-\u9FFF`]'
javascriptParser = Parser(Language(tree_sitter_javascript.language()))



def getFromSplitArray(v: str, replaceUnderscores: bool = True) -> List[List[str]]:
	"""Extracts every string ``.split()`` expression in source order."""
	source, root = _parseJavascript(v)
	newList = []
	for call in _findNodes(root, "call_expression"):
		values = _splitValues(source, call)
		if values is not None:
			newList.append([formatStr(value, replaceUnderscores = replaceUnderscores) for value in values])
	return newList

def getFromNestedSplitArray(v: str, replaceUnderscores: bool = True) -> List[List[List[str]]]:
	"""Extract nested arrays whose leaf entries are string ``.split()`` calls."""
	source, arrayNode = _topLevelArray(v)
	groups = []
	for groupNode in arrayNode.named_children:
		if groupNode.type != "array":
			continue
		rows = []
		for rowNode in groupNode.named_children:
			values = _splitValues(source, rowNode)
			if values is not None:
				rows.append([formatStr(value, replaceUnderscores = replaceUnderscores) for value in values])
		groups.append(rows)
	return groups


def getFromLiteralArrayEntry(v: str, index: int, replaceUnderscores: bool = False) -> List[str]:
	"""Read string literals from one indexed nested array without legacy normalization."""
	source, arrayNode = _topLevelArray(v)
	entries = arrayNode.named_children
	if index < 0 or index >= len(entries):
		raise IndexError(f"Array entry {index} is out of range")
	entry = entries[index]
	if entry.type != "array":
		raise ValueError(f"Array entry {index} is not a literal array")
	values = []
	for valueNode in entry.named_children:
		if valueNode.type != "string":
			raise ValueError(f"Array entry {index} contains a non-string literal")
		value = _stringValue(source, valueNode)
		values.append(formatStr(value, replaceUnderscores = replaceUnderscores))
	return values


def _findNode(node: Node, nodeType: str) -> Node | None:
	"""Finds the first named AST node of ``nodeType`` below ``node``.

	Tree-sitter exposes punctuation such as brackets as anonymous children.
	``named_children`` visits only meaningful syntax nodes such as arrays,
	function calls, and string literals.
	"""
	if node.type == nodeType:
		return node
	for child in node.named_children:
		result = _findNode(child, nodeType)
		if result:
			return result
	return None

def _findNodes(node: Node, nodeType: str) -> List[Node]:
	"""Finds all named AST nodes of ``nodeType`` in source order."""
	results = [node] if node.type == nodeType else []
	for child in node.named_children:
		results.extend(_findNodes(child, nodeType))
	return results


def _parseJavascript(v: str) -> tuple[bytes, Node]:
	"""Parses a CodeReader function section, complete array, or array fragment."""
	if re.search(r"\breturn\b", v):
		source = f"function extract() {{ {v} }}".encode("utf-8")
		return source, javascriptParser.parse(source).root_node

	source = f"const extract = {v};".encode("utf-8")
	root = javascriptParser.parse(source).root_node
	declaration = _findNode(root, "variable_declarator")
	value = declaration.child_by_field_name("value") if declaration else None
	if not root.has_error and value and value.type == "array":
		return source, root

	source = f"const extract = [{v}];".encode("utf-8")
	return source, javascriptParser.parse(source).root_node


def _topLevelArray(v: str) -> tuple[bytes, Node]:
	"""Returns the AST array represented by a function return or array fragment."""
	source, root = _parseJavascript(v)
	returnNode = _findNode(root, "return_statement")
	if returnNode:
		return source, returnNode.named_children[0]
	declaration = _findNode(root, "variable_declarator")
	return source, declaration.child_by_field_name("value")


def _nodeText(source: bytes, node: Node) -> str:
	"""Returns the exact source text represented by a Tree-sitter node."""
	return source[node.start_byte:node.end_byte].decode("utf-8")


def _stringValue(source: bytes, node: Node) -> str:
	"""Decodes a JavaScript double-quoted string node, including escape sequences."""
	return json.loads(_nodeText(source, node))



def _splitValues(source: bytes, node: Node) -> List[str] | None:
	"""Returns WikiBot-normalized values when ``node`` is a string ``.split()`` call."""
	if node.type != "call_expression":
		return None
	function = node.child_by_field_name("function")
	if not function or function.type != "member_expression":
		return None
	target = function.child_by_field_name("object")
	propertyName = function.child_by_field_name("property")
	if not target or target.type != "string" or not propertyName or _nodeText(source, propertyName) != "split":
		return None
	value = _stringValue(source, target)
	delimiter = " " if value.count(" ") > value.count(";") else ";"
	return value.split(delimiter)

def _mixedArrayEntry(source: bytes, node: Node, replaceUnderscores: bool) -> List[str] | None:
	"""Converts one top-level JavaScript array entry into WikiBot string values.

	Supported AST shapes mirror the data formats used by the codefile:

	- ``"a b".split(" ")`` is a call expression whose function is the
	  ``split`` member of a string. WikiBot keeps its existing space-versus-semicolon
	  delimiter rule so generated exports do not change.
	- ``["a", 1]`` is an array node passed to the existing ``strToArray``
	  converter, preserving WikiBot's formatting behavior.

	Other expressions are not static data entries and are ignored.
	"""
	values = _splitValues(source, node)
	if values is not None:
		return values

	if node.type == "array":
		return strToArray(_nodeText(source, node), replaceUnderscores)
	return None


def getFromMixedArray(v: str, replaceUnderscores: bool = True, formatSubSection: bool = True) -> List[List[str]]:
	"""
	Converts the top-level entries of a JavaScript array containing a mix of
	``.split()`` strings and array literals into lists of strings.

	Tree-sitter owns JavaScript tokenization and nesting. Function sections are
	wrapped as a complete function; callers such as EquipmentSets that provide
	an array fragment are wrapped as an array initializer.

	Tree-sitter nodes reference byte ranges in the parsed ``source`` rather than
	storing decoded values. The helper keeps that source beside the syntax tree
	and uses those ranges to recover literals.
	"""
	source, arrayNode = _topLevelArray(v)

	newList = []
	# ``named_children`` returns array elements only; bracket and comma tokens are
	# anonymous children and therefore require no manual filtering.
	for entry in arrayNode.named_children:
		subSection = _mixedArrayEntry(source, entry, replaceUnderscores)
		if subSection is None:
			continue
		if formatSubSection:
			newList.append([formatStr(value, replaceUnderscores = replaceUnderscores) for value in subSection])
		else:
			newList.append(subSection)
	return newList


def getFromSplit(v: str) -> List[str]:
	"""Extracts the first string ``.split()`` expression from a code section."""
	source, root = _parseJavascript(v)
	for call in _findNodes(root, "call_expression"):
		values = _splitValues(source, call)
		if values is not None:
			return values
	section = formatStr(v, ["  ", "\n"])
	return section.replace(".split( )", "").split(" ")


def getFromArrayArray(v: str, repU = True) -> List[List[str]]:
	"""Converts a JavaScript array or its direct child arrays into string lists."""
	source, arrayNode = _topLevelArray(v)
	arrayChildren = [child for child in arrayNode.named_children if child.type == "array"]
	if not arrayChildren:
		return [strToArray(_nodeText(source, arrayNode), repU)]
	return [strToArray(_nodeText(source, child), repU) for child in arrayChildren]


def getFrom4dArray(v: str) -> List[List[List[List[str]]]]:
	"""Converts nested arrays to the four-dimensional shape expected by existing repositories."""
	source, arrayNode = _topLevelArray(v)
	def convert(node: Node):
		arrayChildren = [child for child in node.named_children if child.type == "array"]
		if not arrayChildren:
			return strToArray(_nodeText(source, node))

		children = []
		for child in node.named_children:
			if child.type == "array":
				children.append(convert(child))
				continue
			values = _splitValues(source, child)
			if values is not None:
				children.append(values)
		return children

	# Source functions vary between three and four nested array levels. The
	# helper's public contract has always padded shallower inputs to four levels.
	result = convert(arrayNode)
	depth = 0
	current = result
	while isinstance(current, list):
		depth += 1
		current = current[0] if current else None
	while depth < 4:
		result = [result]
		depth += 1
	return result


def isRecipe(name: str) -> bool:
	return name[:-1] == "SmithingRecipes"


def isTalent(name: str) -> bool:
	return name[:10] == "TalentBook"


def formatFloat(v: float) -> str:
	res = np.format_float_positional(v)
	if res[-1] == ".":
		return res[:-1]
	return res


def camelCaseSplitter(string: str) -> List[str]:
	"""
	Splits a string base on camel case.
	eg: camelCaseSplitter("helloThere") = ["hello", "There"]

	Args:
		string: The string to split on

	Returns:
		A list of strings split based on camel case

	"""
	return re.sub("([A-Z][a-z]+|[0-9])", r" \1", re.sub("([A-Z]+)", r" \1", string)).split()


def camelCaseToTitle(string: str) -> str:
	"""
	Converts Camel Case to a title
	eg: camelCaseToTitle("helloThere") = "Hello There"
	Args:
		string: The string to conver

	Returns:
		The string as a title

	"""
	if "_" in string:
		return replaceUnderscores(string)
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


def strToArray(v: str, repU = False) -> List[str]:
	"""
	Converts a string reprisentation of a list to an actual python list
	strToArray("[1,2,3,4]") = ["1", "2", "3", "4"]
	Args:
		v: [str] the string to convert

	Returns:
		the resulting list

	"""
	string = v.replace(",_", "&&&&").replace(",0", "$$$$").replace("{_", "****").replace("{%_", "####")
	parts = formatStr(string, ["[", "]", '"', "return ", ";", "\n", "{", "}"]).split(",")
	res = []
	for x in parts:
		formatted = formatStr(x).replace("&&&&", ",_").replace("$$$$", ",0").replace("****", "{_").replace("####",
		                                                                                                   "{%_")
		if formatted:
			res.append(replaceUnderscores(formatted) if repU else formatted)
	return res


def changeChestNames(intName, name):
	"""

	Args:
		intName: the internal name of the enemy
		name: the dislpay name of the enemy

	Returns:
		A more descriptive version of the chests name

	"""
	col = int(intName[6]) - 1
	return f"{Constants.COLNAMES[col]} {name}"


def toLowerCamel(imp: str) -> str:
	return imp[0].lower() + imp[1:]


def extractImportsClass(imports: Set[str]) -> str:
	res = []
	for imp in sorted(imports):
		if "Enum" in imp:
			res.append("import { "f"{imp}"" } from "f"'../enum/{toLowerCamel(imp)}';")
			continue
		res.append("import { "f"{imp}"" } from "f"'../model/{toLowerCamel(imp)}';")
	return "\n".join(res) + '\n\n'


def formatToSingleSpace(val: str) -> str:
	return re.sub(' +', ' ', val)
