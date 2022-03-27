from typing import List

from definitions.misc.StarSign import StarSign
from helpers.HelperFunctions import getFromArrayArray, replaceUnderscores
from repositories.master.Repository import Repository


class StarSignsRepo(Repository[StarSign]):
	@classmethod
	def getCategory(cls) -> str:
		return "Misc"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["StarSigns", "SSignInfoUI"]

	@classmethod
	def generateRepo(cls) -> None:
		# StarSigns
		signData = getFromArrayArray(cls.getSection(0))
		# SSignInfoUI
		UIData = getFromArrayArray(cls.getSection(1))
		for idx, sign in enumerate(signData):
			# Find the UI info based on the star sign index
			uiInfo = next(filter(lambda x: x[0] == str(idx), UIData))
			name = replaceUnderscores(sign[0])
			signInfo = StarSign(
				name = name,
				text =' '.join([replaceUnderscores(text) for text in sign[1:] if text != "_"]),
				x = uiInfo[1],
				y = uiInfo[2],
				prevReq = uiInfo[3],
				cost = uiInfo[4]
			)
			cls.add(name, signInfo)
			cls.addList(signInfo)
			
