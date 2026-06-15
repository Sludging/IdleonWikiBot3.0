import re
from typing import List, Dict, Optional

from definitions.questdef.NpcHead import NpcHead
from helpers.Constants import Constants
from helpers.CustomTypes import Integer
from helpers.HelperFunctions import formatStr, replaceUnderscores
from repositories.master.FileRepository import FileRepository
from repositories.misc.RandoListRepo import RandoListRepo, RandoListDescriptions


class NpcHeadRepo(FileRepository[NpcHead]):
	@classmethod
	def getCategory(cls) -> str:
		return "Npc"

	@classmethod
	def parse(cls, value: Dict[str, any]) -> NpcHead:
		return NpcHead.parse_obj(value)

	@classmethod
	def getSections(cls) -> List[str]:
		return ["Quests", "Quests2"]

	@classmethod
	def initDependencies(cls, log = True) -> None:
		RandoListRepo.initialise(cls.codeReader, False)

	@classmethod
	def generateRepo(cls) -> None:
		raise NotImplementedError(
			"NpcHeadRepo cannot regenerate from wiki. Delete the cached JSON and re-run with a "
			"wiki-connected machine if you need to rebuild from scratch."
		)

	# NPCs not present in any RandoList — world and type assigned manually.
	# Keys use raw underscore names (as they appear in game code / RandoLists).
	hardcodedWorlds: Dict[str, Dict[str, str]] = {
		# W1 — Blunder Hills
		"Forest_Soul":       {"world": "Blunder Hills",      "type": ""},
		"Root_Soul":         {"world": "Blunder Hills",      "type": ""},
		"Pet_Dog":           {"world": "Blunder Hills",      "type": ""},
		"Keymaster":         {"world": "Blunder Hills",      "type": ""},
		"Bort":              {"world": "Blunder Hills",      "type": "Event"},
		"Luckulyte":         {"world": "Blunder Hills",      "type": "Event"},
		# W2 — Yum-Yum Desert
		"Dune_Soul":         {"world": "Yum-Yum Desert",     "type": ""},
		# W3 — Frostbite Tundra
		"Frigid_Soul":       {"world": "Frostbite Tundra",   "type": ""},
		# W4 — Hyperion Nebula
		"Squish_Soul":       {"world": "Hyperion Nebula",    "type": ""},
		# W5 — Smolderin' Plateau
		"Oozie_Soul":        {"world": "Smolderin' Plateau", "type": ""},
		# W6 — Spirited Valley
		"Brezy_Soul":        {"world": "Spirited Valley",    "type": ""},
		# W7 — Shimmerfin Deep
		"Humble_Hugh":       {"world": "Shimmerfin Deep",    "type": ""},
		"Coralcave_Prince":  {"world": "Shimmerfin Deep",    "type": ""},
		"Coral_Kid":         {"world": "Shimmerfin Deep",    "type": ""},
		"Musselini":         {"world": "Shimmerfin Deep",    "type": ""},
		"Deeps_Soul":        {"world": "Shimmerfin Deep",    "type": ""},
		"Glimbo":            {"world": "Shimmerfin Deep",    "type": ""},
		"Minehead":          {"world": "Shimmerfin Deep",    "type": ""},
		"Sushi_Station":     {"world": "Shimmerfin Deep",    "type": ""},
		"The_Button":        {"world": "Shimmerfin Deep",    "type": ""},
	}

	@classmethod
	def getWorld(cls, rawName: str) -> str:
		"""Return the world for rawName (underscore format), or empty string if unknown."""
		npcInWorld = [
			RandoListRepo.get(RandoListDescriptions.npcsInBlunder).elements,
			RandoListRepo.get(RandoListDescriptions.npcsInYumyum).elements,
			RandoListRepo.get(RandoListDescriptions.npcsInFrostbite).elements,
			RandoListRepo.get(RandoListDescriptions.npcsInNebulon).elements,
			RandoListRepo.get(RandoListDescriptions.npcsInSmolderin).elements,
			RandoListRepo.get(RandoListDescriptions.npcsInSpirited).elements,
			RandoListRepo.get(RandoListDescriptions.npcsInShimmerfin).elements,
		]
		for worldIndex, worldList in enumerate(npcInWorld):
			if rawName in worldList:
				return Constants.worlds[worldIndex]
		if rawName in cls.hardcodedWorlds:
			return cls.hardcodedWorlds[rawName]["world"]
		return ""

	@classmethod
	def newHead(cls, world: str = "Unknown", noQuest: Integer = 0, typ: str = "Unknown"):
		return NpcHead(
			location = "Unknown",
			world = world,
			noQuest = noQuest,
			type = typ,
			notes = " "
		)

	@classmethod
	def get(cls, key: str) -> Optional[NpcHead]:
		if cls.contains(key):
			return super().get(key)
		# Try to resolve world from game code even if NPC has no wiki page
		rawName = key.replace(" ", "_")
		world = cls.getWorld(rawName)
		if not world:
			raise ValueError(f"NPC '{key}' (raw: '{rawName}') has unknown world — add it to a RandoList or the hardcoded fallback")
		hardcoded = cls.hardcodedWorlds.get(rawName)
		typ = hardcoded["type"] if hardcoded and hardcoded["type"] else "Unknown"
		return cls.newHead(world = world, typ = typ)
