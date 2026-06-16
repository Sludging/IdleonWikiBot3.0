from typing import List, Dict

from definitions.misc.UpgradeVault import UpgradeVault
from helpers.HelperFunctions import replaceUnderscores, getFromSplitArray
from repositories.master.Repository import Repository


class UpgradeVaultRepo(Repository[UpgradeVault]):
	# Mapping of upgrade index to tooltip text from the UI code
	TOOLTIP_TEXTS: Dict[int, str] = {
		1: "These talent points are just for the 1st Tab.",
		4: "As a Beginner you... wait, why are you a beginner? Go get a class!",
		6: "These talent points are just for the 2nd Tab.",
		10: "You can actually craft from ANYWHERE! Open your Codex, go to Quik Ref tab, then click Anvil! Boom!",
		11: "Seriously, craft the Max Carry Bags at the anvil whenever you can! Being able to carry 1000s of items in each slot is baller!",
		12: "Create more characters at the Main Menu! Open MENU\\SWAP PLAYERS\\_PLAYER_MENU in the top left corner! Ez Pz!",
		14: "POW 10 means Power of 10. So you get more bonus at 100, 1000, and so on! ALSO, this counts kills from ALL your players!",
		15: "A Knockout, or KO, is when you kill the target monster in a single hit using your bare hands, no weapon equipped!",
		17: "This bonus INCREASES for every ore you mine! It also counts ores mined from any player, so go make a 2nd player!",
		19: "He a happy boi!",
		20: "POW 10 means Power of 10. So you get more bonus at 100, 1000, and so on! ALSO, this counts kills from ALL your players!",
		21: "Orion the Owl can be found in the SECRET portal on the Bored Beans map! Ok, it's not really a secret, but like whatever...",
		24: "Click the PRODUCE tab at the anvil, it will flash if you haven't found it yet!",
		27: "POW 10 means Power of 10. So you get more bonus at 100, 1000, and so on! ALSO, this counts kills from ALL your players!",
		31: "Can't find poops? The sewer entrance is literally where you started the game!",
		34: "Talk to Grasslands Gary in World 1 town, then UNLOCKS in the top right. Spend trophies from completing tasks to get new Anvil Recipes!",
		35: "You don't know how to fish? World 2 my friend, left of town can't miss it!",
		37: "This bonus only counts the first 100 Levels of each bubble. Sorry endgamers, those big ahh bubbles you got dont count!",
		42: "Find vials in the 3rd tab at the top of ALCHEMY!",
		44: "These are the first of MANY cards you will turn passive! You'll find more ways in the RIFT in World 4!",
		45: "Poppy the Kangaroo Mouse is over at the SECRET oasis, buy the Map from the bottom of the World 2 town shop to go find them!!!",
		48: "Construction is a World 3 feature. Sheepies are also World 3. Just tellin' ya incase you're still in World 2!",
		49: "This star talent tracks how many different quests you've done on ANY player. No need to do the same quest twice!!!",
		50: "These will become a LOT easier to collect after building the Automation Arm in Construction! A LOT less running around!",
		75: "Captains gain EXP at the end of each sailing voyage, based on how far the trip was. Leveling them up increases their bonuses, as shown in the CREW tab.",
		76: "Divinity Blessings are the passive, permanent upgrades that each Divinity has. You'll see them underneath the MINOR bonus description of each Divinity.",
		78: "Crop Evo chance is the chance that a crop evolves to the next type. You want this to happen so you can collect more and more crop types, for bigger bonuses!",
		79: "The Crop Depot bonuses can be found by clicking on the Scientist Blobulyte. He's the one with the giant pencil, left of the Farmer's Market!",
		83: "You can find the Summoning Upgrades by clicking on the floating White Stone. It's on the left side of the World 6 town map!",
		85: "Get Magic Beans by buying the 'Crop Transfer Ticket' from W6 Town Shop, and dropping it on Legumulyte found in the Mama Troll map deep in the Bamboo Forest of World 6!",
	}

	@classmethod
	def getCategory(cls) -> str:
		return "Misc"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["UpgradeVault"]

	@classmethod
	def generateRepo(cls) -> None:
		vault_data = getFromSplitArray(cls.getSection())

		for index, data in enumerate(vault_data):
			if not data or len(data) < 11:  # We need at least 11 fields since we use index 10
				continue

			name = replaceUnderscores(data[0])
			has_tooltip = "製" in name

			# Mapping based on game's UI code:
			# data[0] is name
			# data[1] is base_cost
			# data[2] is scaling_factor
			# data[3] is x1 (unknown purpose)
			# data[4] is max_level (used in level checks)
			# data[5] is value (used in bonus calculations)
			# data[6] is unlock_req (used in unlock checks)
			# data[8] is x2 (unknown purpose)
			# data[9] is description_line1
			# data[10] is description_line2
			description_line1 = data[9]
			description_line2 = None if data[10] == "_" else data[10]
			x2 = data[8]

			# Get tooltip text if it exists for this index
			tooltip_text = cls.TOOLTIP_TEXTS.get(index)

			upgrade = UpgradeVault(
				name = name,
				base_cost = data[1],
				scaling_factor = data[2],
				x1 = data[3],
				max_level = data[4],
				value = data[5],
				unlock_req = data[6],
				x2 = x2,
				description_line1 = description_line1,
				description_line2 = description_line2,
				has_tooltip = has_tooltip,
				tooltip_text = tooltip_text
			)

			cls.add(name, upgrade)
			cls.addList(upgrade)
