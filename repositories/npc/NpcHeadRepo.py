import re
from typing import List, Dict, Optional

from mwparserfromhell import parse as mwparse
from pywikibot import Site, Page
from rich.progress import track

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
		website = Site()
		reNpcs = r'..\.addDialogueFor\("([a-zA-Z0-9_]*)", [^\s"]*\)'

		for n in range(len(cls.getSections())):
			questText = formatStr(cls.getSection(n), ["\n"])
			questData = re.split(reNpcs, questText)
			for i in track(range(1, len(questData), 2), "Pulling heads..."):
				npcName = replaceUnderscores(questData[i])
				npcName = Constants.nameConflicts.get(npcName, npcName)
				cls.add(npcName, cls.getHead(website, npcName, questData[i]))

	@classmethod
	def getHead(cls, website: Site, dispName: str, rawName: str) -> NpcHead:
		if dispName in ["", " "]: return {}
		text = Page(website, dispName).text
		replacedText = text.replace("\n", Constants.newLineRep)
		wikiCode = mwparse(replacedText)
		templates = wikiCode.filter_templates(recursive = False)
		selectedTemplate = None
		for template in templates:
			if "world" in template:
				selectedTemplate = template
				break
		codeWorld = cls.getWorld(rawName)
		hardcoded = cls.hardcodedWorlds.get(rawName)
		if selectedTemplate is None:
			if codeWorld:
				hardcodedType = hardcoded["type"] if hardcoded else "Unknown"
				return cls.newHead(world = codeWorld, typ = hardcodedType)
			return cls.newHead()
		typ = ""
		if "npcType" in selectedTemplate:
			typ = cls.getParsed(selectedTemplate, "npcType")
		if hardcoded and hardcoded["type"]:
			typ = hardcoded["type"]
		notes = " "
		if "notes" in selectedTemplate:
			notes = re.escape(cls.getParsed(selectedTemplate, "notes")).replace('"', "'")
		noQuest = 0
		if "noquest" in selectedTemplate:
			noQuest = cls.getParsed(selectedTemplate, "noquest")
		resolvedWorld = codeWorld if codeWorld else cls.getParsed(selectedTemplate, "world")
		if resolvedWorld == "Unknown":
			raise ValueError(f"NPC '{dispName}' (raw: '{rawName}') has unknown world — add it to a RandoList or the hardcoded fallback")
		return NpcHead(
			location = cls.getParsed(selectedTemplate, "location"),
			world = resolvedWorld,
			noQuest = noQuest,
			type = typ,
			notes = notes
		)

	# NPCs not present in any RandoList — world and type assigned manually.
	# Keys use raw underscore names (as they appear in game code / RandoLists).
	hardcodedWorlds: Dict[str, Dict[str, str]] = {
		"Humble_Hugh":       {"world": "Shimmerfin Deep", "type": ""},
		"Coralcave_Prince":  {"world": "Shimmerfin Deep", "type": ""},
		"Bort":              {"world": "Blunder Hills",   "type": "Event"},
		"Luckulyte":         {"world": "Blunder Hills",   "type": "Event"},
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
		hardcoded = cls.hardcodedWorlds.get(rawName)
		typ = hardcoded["type"] if hardcoded and hardcoded["type"] else "Unknown"
		return cls.newHead(world = world if world else "Unknown", typ = typ)
