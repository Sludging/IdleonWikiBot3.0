from typing import List

from definitions.misc.world5.hole.Study import Study
from definitions.misc.world5.hole.HoleOrder import HoleOrder
from helpers.HelperFunctions import getFromMixedArray, replaceUnderscores
from repositories.master.Repository import Repository


class StudyRepo(Repository[Study]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/5/Hole"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["HoleInfo"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromMixedArray(cls.getSection())
		
		# Get study data from holesInfo array
		names = data[HoleOrder.StudyNames.value]
		descriptions = data[HoleOrder.StudyDescriptions.value]
		multipliers = data[HoleOrder.StudyMultipliers.value]
		
		# 1.17 keeps placeholder BRUH rows after the described studies.
		study_count = min(len(names), len(descriptions), len(multipliers))
		
		# Process each described study
		for i in range(study_count):
			study = Study(
				index=i,
				name=replaceUnderscores(names[i]),
				description=replaceUnderscores(descriptions[i]),
				multiplier=float(multipliers[i])
			)
			cls.addList(study)
			cls.add(f"{i}", study) 
