from typing import List, Dict

from definitions.misc.TesseractUpgrade import TesseractUpgrade
from helpers.HelperFunctions import replaceUnderscores, getFromSplitArray
from repositories.master.Repository import Repository


class TesseractUpgradeRepo(Repository[TesseractUpgrade]):
	# Mapping of upgrade index to tooltip text from the UI code
	# Based on the game's UI code - will need to be discovered for Tesseract
	TOOLTIP_TEXTS: Dict[int, str] = {
		0: "Enter Arcanist Form to collect Tachyons from monsters! Defeat Arcane Monsters spawned by your Crystal Talent within the timer to unlock the next map. If you run out of time, arcane mobs will despawn and your crystal will lose its charge.",
		3: "This chance goes down with each Prisma Bubble you get. Also, drop chance increases based on your current World. @   @ You have found % Prisma bubbles so far!",
		5: "Quality is a rough idea of how powerful a weapon is. Only the stats themselves matter. @ Every Weapon Power gives a 1.04x DMG multi stack. @ Mobs will only drop up to 100 Arcanist weapons a day.",
		10: "You have to be in Arcanist Form, duh...",
		18: "2x Quantity just means that if a monster drops 3 statues, you'll get 6 instead! This also affects Statues dropped from AFK gains.",
		23: "Quality is a rough idea of how powerful a ring is. Only the stats themselves matter. @ Mobs will only drop up to 100 Arcanist rings a day.",
		30: "2x Quantity just means that if a monster drops 17 golden food, you'll get 34 instead! This also affects Gold Food dropped from AFK gains.",
		49: "Upgrades' here means Tesseract Upgrades, as you might have assumed...",
		51: "For example, if your normal Drop Rate is 20x, and this upgrade is 25%, it would give you 5x Prisma drop chance!",
		54: "Endless mode is accessed in the Top Right of the Summoner's Table",
		58: "Higher than what, you ask? Well, higher than the amount shown in the Overwhelming Energy talent.",
	}

	@classmethod
	def getCategory(cls) -> str:
		return "Misc"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["ArcaneUpg"]

	@classmethod
	def generateRepo(cls) -> None:
		tesseract_data = getFromSplitArray(cls.getSection())

		for index, data in enumerate(tesseract_data):
			if not data or len(data) < 10:  # We need at least 10 fields
				continue

			name = data[0]
			has_tooltip = "製" in name
			
			# Clean up the name by removing the tooltip indicator
			if has_tooltip:
				charIndex = name.index("製")
				name = name[0:charIndex].rstrip()

			# Mapping based on game's UI code:
			# data[0] is name
			# data[1] is base_cost
			# data[2] is scaling_factor
			# data[3] is x1 (unknown purpose)
			# data[4] is max_level
			# data[5] is value
			# data[6] is unlock_req
			# data[8] is x2 (unknown purpose)
			# data[9] is description

			# Get tooltip text if it exists for this index
			tooltip_text = cls.TOOLTIP_TEXTS.get(index)

			upgrade = TesseractUpgrade(
				name = name,
				base_cost = data[1],
				scaling_factor = data[2],
				x1 = data[3],
				max_level = data[4],
				value = data[5],
				unlock_req = data[6],
				x2 = data[8],
				description = data[9],
				has_tooltip = has_tooltip,
				tooltip_text = tooltip_text
			)

			cls.add(name, upgrade)
			cls.addList(upgrade) 
