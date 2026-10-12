import re
from typing import List

from definitions.misc.world7.researchMetadata import ResearchMetadata
from repositories.master.Repository import Repository


class ResearchMetadataRepo(Repository[ResearchMetadata]):
	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/7"

	@classmethod
	def getSections(cls) -> List[str]:
		return [
			"ResearchMinRoll",
			"ResearchMaxRoll",
			"ResearchRollsPerDay",
			"ResearchKaleidoscopeAdjacentBoost",
			"ResearchShapeRotationUnlock",
			"ResearchShapeRotationClockwise",
			"ResearchShapeRotationCounterclockwise",
		]

	@classmethod
	def generateRepo(cls) -> None:
		rotationPattern = (
			r'getGameAttribute\("Research"\)\s*\[6\]\s*'
			r'\[Math\.round\([^\n;]+\)\]\)\s*\+\s*([+-]?\d+)\s*\)'
		)
		patterns = [
			r"\breturn\s+Math\.floor\(\s*([+-]?\d+)\s*\+",
			r"\breturn\s+Math\.floor\(\s*([+-]?\d+)\s*\+",
			r"\breturn\s+Math\.round\(\s*([+-]?\d+)\s*\+",
			r"\breturn\s*\(\s*\(\s*([+-]?\d+)\s*\+",
			r"\breturn\s+(\d+)\s*<=\s*[A-Za-z_$][\w$]*\.asNumber\(",
			rotationPattern,
			rotationPattern,
		]
		values = []
		for index, pattern in enumerate(patterns):
			matches = re.findall(pattern, cls.getSection(index))
			if len(matches) != 1:
				raise ValueError(
					f"ResearchMetadataRepo: expected one source literal in "
					f"{cls.getSections()[index]}, found {len(matches)}"
				)
			values.append(int(matches[0]))

		if values[5] <= 0 or values[6] != -values[5]:
			raise ValueError("ResearchMetadataRepo: expected opposite shape rotation button steps")

		metadata = ResearchMetadata(
			baseDiscoveryMinRoll = values[0],
			baseDiscoveryMaxRoll = values[1],
			baseDiscoveryRollsPerDay = values[2],
			baseKaleidoscopeAdjacentBoostPercent = values[3],
			shapeRotationResearchLevel = values[4],
			shapeRotationStepDegrees = values[5],
		)
		cls.add("metadata", metadata)
		cls.addList(metadata)
