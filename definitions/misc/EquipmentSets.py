from typing import List
from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric, Integer, Boolean


class EquipmentSets(IdleonModel):
	name: str
	armors: List[str]
	tools: List[str]
	weapons: List[str]
	toolsRequired: Boolean
	weaponRequired: Boolean
	bonusValue: Numeric
	description: str
	displayOrder: Integer
