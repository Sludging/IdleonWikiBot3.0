import re
from typing import List

from definitions.enemy.BossDetails import BossDetails, BossAttack
from helpers.HelperFunctions import formatStr, wrap, strToArray
from repositories.enemies.EnemyDetailsRepo import EnemyDetailsRepo
from repositories.master.Repository import Repository


class BossDetailRepo(Repository[BossDetails]):

	@classmethod
	def getCategory(cls) -> str:
		return "Enemy"

	@classmethod
	def initDependencies(cls, log = True) -> None:
		EnemyDetailsRepo.initialise(cls.codeReader, log)

	@classmethod
	def getSections(cls) -> List[str]:
		return ["BossDetails"]

	@classmethod
	def generateRepo(cls) -> None:
		bossIntNames = ["wolf", "Boss2", "Boss3", "FILLER"]
		tabs = ["health", "defence", "exp", "keys"]
		letters = ["A", "B", "C"]

		attackNames = [
			["Fireball", "Stomp", "Rock Spikes", "Spike Traps", "Sword Swing", "Uppercut", "Rocketfist"],
			["Hammer", "Scimitar", "Fire Column", "Purple Psionic Hoops", "Finger Gun", "Headpat", "Blue Psionic",
			 "Hoops", "Kick"],
			["Front Stomp", "Back Stomp", "Frozen Spikes", "Falling Icicles", "Tusk Swipe", "filler", "filler", "filler", "filler",
			 "filler", "filler", "filler"],
			["filler", "filler", "filler", "filler", "filler", "filler", "filler", "filler", "filler", "filler",
			 "filler", "filler", "filler"],
		]

		bossInformation = {}
		bossData = formatStr(cls.getSection(), ["\n", "  "])

		bossSections = [wrap(x) for x in re.split(r"],?],\[\[", bossData)]
		for i, bossSection in enumerate(bossSections):
			bossDetails = [strToArray(x) for x in re.split(r",?],\[", bossSection)]
			for j, bossDetail in enumerate(bossDetails[0:4]):
				for k, det in enumerate(bossDetail):
					working = f"{bossIntNames[i]}{letters[k]}"
					if working not in bossInformation:
						bossInformation[working] = {}
					bossInformation[working][tabs[j]] = det

			for j, bossDetail in enumerate(bossDetails[4:7]):
				working = f"{bossIntNames[i]}{letters[j]}"
				bossInformation[working]["Attacks"] = {}
				for k, det in enumerate(bossDetail):
					bossInformation[working]["Attacks"][attackNames[i][k]] = det

		for boss, detail in bossInformation.items():
			attacks = []
			for name, damage in detail.get("Attacks").items():
				attacks.append(BossAttack(name = name, damage = damage))
			cls.add(boss, BossDetails(
				health = detail["health"],
				defence = detail["defence"],
				exp = detail["exp"],
				keys = detail["keys"],
				attacks = attacks.copy(),
			))

	@classmethod
	def getWikiName(cls, name: str) -> str:
		return EnemyDetailsRepo.get(name).Name
