import re
from typing import Dict, List, Optional


class Section:
	def __init__(self, start: str, end: str, sectionName: str) -> None:
		self.start = start
		self.end = end
		self.between = ""
		self.sectionName = sectionName


class CodeReader:
	def __init__(self, version: str) -> None:
		self.version = version
		self.codeFile = f"./codefiles/idleon{version}.txt"
		self.currentSection: Optional[Section] = None
		self.sections: List[Section] = []
		self.sectionResults: Dict[str, str] = {}

	def addSection(self, start: str, end: str, sectionName: str) -> None:
		self.sections.append(Section(start, end, sectionName))

	def readCode(self) -> None:
		with open(self.codeFile, mode = "r") as infile:
			lines = infile.read()
			for section in self.sections:
				escapedStart = re.escape(section.start)
				escapedEnd = re.escape(section.end)
				regex = re.compile(rf"(?s){escapedStart}(.*?){escapedEnd}")
				res = regex.findall(lines)
				if res:
					self.sectionResults[section.sectionName] = res[0]
				else:
					self.sectionResults[section.sectionName] = ""

	def getSection(self, sectionName: str) -> Optional[str]:
		return self.sectionResults.get(sectionName)


class IdleonReader:
	def __init__(self, codeFile: str) -> None:
		self.codeReader = CodeReader(codeFile)
		self.readSections()

	def readSections(self):
		self.codeReader.addSection('__name__ = "scripts.ItemDefinitions";',
		                           "addNewItem = function", "Items")
		self.codeReader.addSection('__name__ = "scripts.ItemDefinitions2";', "addNewItem = function", "Items2")
		self.codeReader.addSection("dialogueDefs = new", "finishDialogue", "Quests")
		self.codeReader.addSection("scripts.MonsterDefinitions", "};", "Enemies")
		self.codeReader.addSection("ItemToCraftNAME = function () {", "}", "AnvilItems")
		self.codeReader.addSection("ItemToCraftCostTYPE = function ()", "}", "Recipes")
		self.codeReader.addSection("ItemToCraftEXP = function ()", "}", "RecipeLevel")
		self.codeReader.addSection("SceneNPCquestInfo = function ()", "}", "QuestNames")
		self.codeReader.addSection("MonsterDrops = function ()", "}", "EnemyDropTables")
		self.codeReader.addSection("DropTables = function ()", "}", "DropTables")
		self.codeReader.addSection("AnvilProductionInfo = function", "}", "Production")
		self.codeReader.addSection("ShopNames = function ()", "}", "ShopItems")
		self.codeReader.addSection("ShopQTY = function () ", "}", "ShopQTY")
		self.codeReader.addSection("ShopLocations = function ()", "}", "ShopLocations")
		self.codeReader.addSection("MapDispName = function", "}", "MapNames")
		self.codeReader.addSection("MapAFKtarget = function ()", "}", "MapEnemies")
		self.codeReader.addSection(
			"PostOfficePossibleOrders = function ()", "}", "PostOffice")
		self.codeReader.addSection("FishToolkitInfo = function ()", "}", "FishToolkit")
		self.codeReader.addSection("AlchemyDescription = function", "}", "Bubbles")
		self.codeReader.addSection("TalentOrder = function ()", "}", "TalentOrder")
		self.codeReader.addSection("TalentIconNames = function ()", "}", "TalentNames")
		self.codeReader.addSection("TalentDescriptions = function ()", "};", "TalentData")
		self.codeReader.addSection("ClassNames = function ()", "}", "ClassNames")
		self.codeReader.addSection("atkMoveMap = new ", "};", "ActiveSkill")
		self.codeReader.addSection("StatueInfo = function ()", "}", "StatueInfo")
		self.codeReader.addSection("CardStuff = function ()", "}", "CardInfo")
		self.codeReader.addSection("TaskUnlocks = function ()", "}", "TaskUnlocks")
		self.codeReader.addSection("RefineryInfo = function ()", "}", "RefineryCost")
		self.codeReader.addSection("TowerInfo = function () {", "};", "BuildingData")
		self.codeReader.addSection("SaltLicks = function () {", "};", "SaltLicks")
		self.codeReader.addSection("MTXinfo = function () {", "};", "GemShop")
		self.codeReader.addSection("TrappingInfo = function () {", "};", "TrappingInfo")
		self.codeReader.addSection("PrayerInfo = function () {", "};", "PrayerInfo")
		self.codeReader.addSection("ShrineInfo = function () {", "};", "ShrineInfo")
		self.codeReader.addSection("GuildBonuses = function () {", "};", "GuidBonuses")
		self.codeReader.addSection("BossDetails = function () {", "};", "BossDetails")
		self.codeReader.addSection("DungFlurboShop = function () {", "};", "DungFlurbo")
		self.codeReader.addSection("ArcadeShopInfo = function () {", "};", "ArcadeBonus")
		self.codeReader.addSection("DungEnhanceINFO = function () {", "};", "DungEnhance")
		self.codeReader.addSection("RegAchieves = function () {", "};", "Achieve")
		self.codeReader.addSection("TraitDescriptions = function () {", "};", "DungTraits")
		self.codeReader.addSection("DungPassiveStats = function () {", "};", "DungPassiveI")
		self.codeReader.addSection("DungPassiveStats2 = function () {", "};", "DungPassiveF")
		self.codeReader.addSection("DungKEYCHAINS = function () {", "};", "DungKeychain")
		self.codeReader.addSection("DungItems = function () {", "};", "DungItems")
		self.codeReader.addSection("DungMobs = function () {", "};", "DungEnemies")
		self.codeReader.addSection("DungKEYCHAINS = function () {", "};", "DungKeychain")
		self.codeReader.addSection("UnlockinRNGitems = function () {", "};", "UnlockRNG")
		self.codeReader.readCode()
