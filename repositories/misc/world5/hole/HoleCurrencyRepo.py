from typing import List

from definitions.misc.world5.hole.HoleCurrency import HoleCurrency
from definitions.misc.world5.hole.HoleOrder import HoleOrder
from helpers.HelperFunctions import getFromLiteralArrayEntry
from repositories.master.Repository import Repository
from repositories.misc.world5.hole.FountainCurrencyRepo import FountainCurrencyRepo
from repositories.misc.world5.hole.HarpNotesRepo import HarpNotesRepo
from repositories.misc.world5.hole.SedimentRepo import SedimentRepo


class HoleCurrencyRepo(Repository[HoleCurrency]):
	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/5/Hole"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["HoleInfo"]

	@classmethod
	def initDependencies(cls, log = True) -> None:
		SedimentRepo.initialise(cls.codeReader, log)
		HarpNotesRepo.initialise(cls.codeReader, log)
		# The Hole predates the Fountain. Do not reuse currencies from a newer reader.
		if cls.codeReader.getSection("FountainUpgrade"):
			FountainCurrencyRepo.initialise(cls.codeReader, log)

	@classmethod
	def generateRepo(cls) -> None:
		# HoleInfo[29][0] is the shared font-glyph map, indexed directly by building[2].
		iconEntries = getFromLiteralArrayEntry(cls.getSection(), HoleOrder.FountainCurrencyIcons.value)
		if len(iconEntries) != 1:
			raise ValueError("HoleInfo currency icon map must contain one string")
		iconMap = iconEntries[0]

		def addCurrency(index: int, kind: str, localIndex: int, name: str) -> None:
			if index >= len(iconMap):
				raise ValueError(f"HoleInfo currency icon map is missing index {index}")
			currency = HoleCurrency(
				index = index,
				kind = kind,
				localIndex = localIndex,
				name = name,
				icon = iconMap[index],
			)
			cls.addList(currency)
			cls.add(str(index), currency)

		# Sediment production credits Holes[9][sedimentIndex]. Preserve legacy coral labels.
		for sediment in SedimentRepo.itemsList():
			name = sediment.name.replace(" ", "") if sediment.name in ("Rad Coral", "Hyper Coral") else sediment.name
			addCurrency(sediment.index, "Sediment", sediment.index, name)

		# Harp note production credits Holes[9][10 + noteIndex].
		for note in HarpNotesRepo.itemsList():
			addCurrency(10 + note.noteId, "HarpNote", note.noteId, note.noteName)

		# JarRupieTypeGiven produces regular types 0..9, credited to Holes[9][20 + type].
		# White (10) and dark (11) Rupies use Holes[11], not the global currency index space.
		# The source has no complete color-name table, so use factual indexed labels.
		for index in range(10):
			addCurrency(20 + index, "Rupie", index, f"Rupie {index}")

		# Fountain upgrade purchases and coin production use Holes[9][30 + currencyIndex].
		if cls.codeReader.getSection("FountainUpgrade"):
			for currency in FountainCurrencyRepo.itemsList():
				addCurrency(currency.holesResourceIndex, "Fountain", currency.index, currency.name)
