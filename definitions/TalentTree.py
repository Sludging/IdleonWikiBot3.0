from typing import List

from pydantic import validator

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric


class Talent(IdleonModel):
	name: str
	description: str
	x1: Numeric
	x2: Numeric
	funcX: str
	y1: Numeric
	y2: Numeric
	funcY: str
	lvlUpText: str

	@validator("x1", "x2", "y1", "y2", pre = True)
	def funcValidator(cls, v: str):
		if v == "_":
			return 0
		return v

	def writeWiki(self, newLine = True) -> str:
		res = "{{Talent\n"
		res += f"|name={self.name}\n"
		res += f"|textArr={self.getDesc()}\n"
		res += f"|form1={self.funcX}\n"
		res += f"|x1={self.x1}\n"
		res += f"|x2={self.x2}\n"
		if self.funcY not in ["txt", "NONE", "_"]:
			res += f"|form2={self.funcY}\n"
			res += f"|y1={self.y1}\n"
			res += f"|y2={self.y2}\n"
		res += "}}"
		return res

	def getDesc(self) -> str:
		return self.description.replace("{", "(Table 1)").replace("}", "(Table 2)")


class TalentTree(IdleonModel):
	talents: List[Talent]

	def writeWiki(self, newLine = True) -> str:
		return "\n".join(map(lambda x: x.writeWiki(), self.talents))
