from typing import List

from pydantic import validator

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class ClassFamilyBonus(IdleonModel):
	"""One source row from ``ClassFamilyBonuses``.

	The index is the zero-based index in the source table; it lines up with the
	leading placeholder in the other class tables rather than a derived class
	name.
	"""

	index: Integer
	bonus: str
	x1: Numeric
	x2: Numeric
	func: str
	y1: Numeric
	y2: Numeric
	funcY: str

	@validator("x1", "x2", "y1", "y2", pre = True)
	def funcValidator(cls, v: str):
		if v == "_":
			return 0
		return v


class ClassSpecializeSkill(IdleonModel):
	"""One source row from ``ClassSpecializeSkills``."""

	index: Integer
	skill: str


class ClassAccountBonus(IdleonModel):
	"""One source row from ``ClassAccountBonus``.

	``x1`` is the table's second source column. The source does not label it
	with a formula or save-state meaning, so it remains a raw numeric field.
	"""

	index: Integer
	bonus: str
	x1: Integer


class ClassPromotionChoice(IdleonModel):
	"""One source row from ``ClassPromotionChoices``."""

	index: Integer
	choices: List[Integer]


class ClassProgression(IdleonModel):
	"""Static class progression tables shared by all talent trees."""

	classNames: List[str]
	familyBonuses: List[ClassFamilyBonus]
	familyBonusDisplayOrder: List[Integer]
	specializeSkills: List[ClassSpecializeSkill]
	accountBonuses: List[ClassAccountBonus]
	promotionChoices: List[ClassPromotionChoice]
