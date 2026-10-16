from typing import Dict, List

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class JellyPlot(IdleonModel):
	index: Integer
	startSlot: Integer
	width: Integer
	height: Integer


class JellyObstructionSlotGrant(IdleonModel):
	obstructionIndex: Integer
	slots: List[Integer]


class JellyBoard(IdleonModel):
	columns: Integer
	rows: Integer
	initialSlots: List[Integer]
	blockedSlots: List[Integer]
	obstructionSlotGrants: List[JellyObstructionSlotGrant]
	plots: List[JellyPlot]


class JellyOperationMetadata(IdleonModel):
	initialObstructionHp: Dict[str, Integer]
	board: JellyBoard
