from typing import List

from definitions.misc.world3.CogMatrix import CogMatrix
from helpers.HelperFunctions import getFromNumericNestedArray
from repositories.master.Repository import Repository


class CogMatrixRepo(Repository[CogMatrix]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/3"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["CogMatrices"]

	@classmethod
	def generateRepo(cls) -> None:
		for index, offsets in enumerate(getFromNumericNestedArray(cls.getSection())):
			matrix = CogMatrix(matrixIndex = index, offsets = offsets)
			cls.add(str(index), matrix)
			cls.addList(matrix)
