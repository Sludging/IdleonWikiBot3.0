from typing import List

from definitions.misc.Rift import Rift, RiftChallenge, RiftMilestone, RiftTarget, RiftTask
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class RiftRepo(Repository[Rift]):
	@classmethod
	def getCategory(cls) -> str:
		return "Misc"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["Rift"]

	@classmethod
	def generateRepo(cls) -> None:
		# RiftStuff contains seven parallel static tables:
		# descriptions, milestone positions/labels, target mobs, visual filters,
		# per-level challenge ids, challenge thresholds, and UI hue offsets.
		data = getFromSplitArray(cls.getSection(), replaceUnderscores = False)

		challenges = [
			RiftChallenge(index = index, requirement = requirement, threshold = data[5][index])
			for index, requirement in enumerate(data[0])
		]
		milestones = [
			RiftMilestone(index = index, bonus = data[1][index * 5 + 2])
			for index in range(len(data[1]) // 5)
		]
		targets = [
			RiftTarget(index = index, target = target)
			for index, target in enumerate(data[2])
		]
		taskOrder = [
			RiftTask(index = index, challengeIndex = challengeIndex)
			for index, challengeIndex in enumerate(data[4])
		]

		toAdd = Rift(
			challenges = challenges,
			milestones = milestones,
			targets = targets,
			taskOrder = taskOrder,
		)
		cls.add("0", toAdd)
		cls.addList(toAdd)
