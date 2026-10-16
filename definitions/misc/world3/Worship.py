from typing import List

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class WorshipWave(IdleonModel):
	index: Integer
	monsterCount: Integer
	skullLevel: Integer
	monsterTier: Integer
	# Source row[3] selects the wave's visual/status variant; the exact enum is not named in code.
	variant: Integer


class WorshipBaseInfo(IdleonModel):
	baseMonsterHp: Integer
	hueOffset: Integer
	monster: str
	# Source column [3] is used as a totem sprite animation-frame offset.
	totemFrame: Integer
	# These are world gameplay coordinates used to spawn the portal actor.
	portalX: Integer
	portalY: Integer
	soulCost: Integer
	efficiencyThreshold: Integer
	requiredWorship: Integer


class WorshipNodes(IdleonModel):
	nodeOrder: List[Integer]
	directionFlags: List[Integer]


class Worship(IdleonModel):
	trialType: Integer
	base: WorshipBaseInfo
	waves: List[WorshipWave]
	nodes: WorshipNodes
