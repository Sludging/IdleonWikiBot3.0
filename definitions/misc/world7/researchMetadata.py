from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class ResearchMetadata(IdleonModel):
	baseDiscoveryMinRoll: Integer
	baseDiscoveryMaxRoll: Integer
	baseDiscoveryRollsPerDay: Integer
	baseKaleidoscopeAdjacentBoostPercent: Integer
	shapeRotationResearchLevel: Integer
	shapeRotationStepDegrees: Integer
