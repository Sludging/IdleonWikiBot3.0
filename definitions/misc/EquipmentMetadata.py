from typing import List

from definitions.master.IdleonModel import IdleonModel


class EquipmentMetadata(IdleonModel):
	powerSuffixes: List[str]
	equipmentTypeRequirements: List[List[str]]
	equipmentTypeGroups: List[List[str]]
	speedNames: List[str]
