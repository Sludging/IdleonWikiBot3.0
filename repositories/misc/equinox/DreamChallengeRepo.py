from typing import Dict, List

from definitions.misc.equinox.DreamChallenge import DreamChallenge
from definitions.misc.weeklybosses.WeeklyAction import WeeklyAction, ActionType
from helpers.CustomTypes import Numeric
from helpers.HelperFunctions import getFromArrayArray
from repositories.master.Repository import Repository


class DreamChallengeRepo(Repository[DreamChallenge]):
	# Values are the additive amounts used by the game's Dreamstuff formulas.
	# Percentage-based multipliers are stored as percentage points (1.03x -> 3).
	# Food Lust contributes 22 points, taking its base 20% reduction to 42%.
	BONUS_VALUES: Dict[int, Numeric] = {
		1: 1,
		3: 10,
		6: 3,
		8: 200,  # Explicit max-level reward; this challenge has no CloudBonus call.
		9: 15,
		11: 1,
		12: 5,
		14: 20,
		15: 4,
		18: 10,
		19: 25,
		21: 5,
		22: 30,
		24: 35,
		25: 4,
		26: 10,
		27: 200,
		29: 40,
		30: 4,
		32: 6,
		33: 22,
		34: 10,
		35: 15,
		37: 5,
		38: 60,
		39: 10,
		40: 65,
		41: 1,
		42: 5,
		43: 5,
		44: 75,
		45: 3,
		46: 90,
		47: 5,
		48: 100,
		49: 5,
		50: 5,
		51: 120,
		52: 6,
		53: 100,
		54: 150,
		55: 5,
		56: 160,
		57: 170,
		58: 6,
		59: 7,
		60: 185,
		61: 6,
		62: 190,
		63: 195,
		64: 7,
		65: 200,
		66: 3,
		67: 7,
		68: 220,
		69: 5,
		70: 5,
		71: 1,
		72: 1,
		73: 1,
		74: 250,
		75: 8,
		76: 1,
	}

	@classmethod
	def getCategory(cls) -> str:
		return "Misc/Equinox"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["DreamChallenge"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromArrayArray(cls.getSection())
		for n, challenge in enumerate(data):
			toAdd = DreamChallenge.fromList([*challenge, cls.BONUS_VALUES.get(n)])
			cls.add(f"{n}", toAdd)
			cls.addList(toAdd)
