from typing import List

from definitions.misc.world3.Worship import Worship, WorshipBaseInfo, WorshipNodes, WorshipWave
from helpers.HelperFunctions import getFrom4dArray, getFromSplitArray
from repositories.master.Repository import Repository


class WorshipRepo(Repository[Worship]):
	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/3"

	@classmethod
	def parse(cls, value) -> Worship:
		return Worship.parse_obj(value)

	@classmethod
	def getSections(cls) -> List[str]:
		return ["WorshipInfo", "WorshipBASEinfos", "WorshipNODESnETC"]

	@classmethod
	def generateRepo(cls) -> None:
		# getFrom4dArray pads this source's three nested array levels to four;
		# unwrap that compatibility level to retain trial -> wave -> field order.
		wavesByTrial = getFrom4dArray(cls.getSection(0))[0]
		baseRows = getFromSplitArray(cls.getSection(1))
		nodesByTrial = getFrom4dArray(cls.getSection(2))[0]

		if not (len(wavesByTrial) == len(baseRows) == len(nodesByTrial)):
			raise ValueError("Worship sections must contain the same number of trial configurations")

		for trialType, (waveRows, baseRow, nodeRows) in enumerate(zip(wavesByTrial, baseRows, nodesByTrial)):
			waves = [
				WorshipWave(
					index=waveIndex,
					monsterCount=wave[0],
					skullLevel=wave[1],
					monsterTier=wave[2],
					variant=wave[3],
				)
				for waveIndex, wave in enumerate(waveRows)
			]
			base = WorshipBaseInfo(
				baseMonsterHp=baseRow[0],
				hueOffset=baseRow[1],
				monster=baseRow[2],
				totemFrame=baseRow[3],
				portalX=baseRow[4],
				portalY=baseRow[5],
				soulCost=baseRow[6],
				efficiencyThreshold=baseRow[7],
				requiredWorship=baseRow[8],
			)
			nodes = WorshipNodes(
				nodeOrder=nodeRows[0],
				directionFlags=nodeRows[1],
			)
			toAdd = Worship(
				trialType=trialType,
				base=base,
				waves=waves,
				nodes=nodes,
			)
			cls.addList(toAdd)
			cls.add(str(trialType), toAdd)
