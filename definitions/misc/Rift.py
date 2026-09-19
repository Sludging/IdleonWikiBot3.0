from typing import List

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class RiftChallenge(IdleonModel):
	index: Integer
	requirement: str
	threshold: Numeric


class RiftMilestone(IdleonModel):
	index: Integer
	bonus: str


class RiftTarget(IdleonModel):
	index: Integer
	target: str


class RiftTask(IdleonModel):
	index: Integer
	challengeIndex: Integer


class Rift(IdleonModel):
	challenges: List[RiftChallenge]
	milestones: List[RiftMilestone]
	targets: List[RiftTarget]
	taskOrder: List[RiftTask]
