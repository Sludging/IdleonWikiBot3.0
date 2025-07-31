from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class ItemRequirement(IdleonModel):
	id: str
	name: str


class MeasurementType(IdleonModel):
	type: str
	name: str


class Measurement(IdleonModel):
	index: Integer
	itemRequirement: ItemRequirement
	measurementType: MeasurementType
	description: str
	formula: str
	formulaType: str 
