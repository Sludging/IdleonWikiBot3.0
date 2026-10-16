import re
from typing import Dict, List

from definitions.misc.world7.spelunking.tool import SpelunkingTool, SpelunkingToolUnlock
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


TOOL_DATA_SECTION = 0
TOOL_UNLOCK_SECTION = 1
TOOL_COUNT = 7


class SpelunkingToolRepo(Repository[SpelunkingTool]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["Spelunking", "SpelunkingToolUnlocks"]

    @classmethod
    def generateRepo(cls) -> None:
        data = getFromSplitArray(cls.getSection(TOOL_DATA_SECTION))
        if len(data) <= 13:
            raise ValueError("Spelunking tool arrays are missing")
        radii, multipliers, staminaCosts, names = data[10], data[11], data[12], data[13]
        if not (len(radii) == len(multipliers) == len(staminaCosts) == len(names) == TOOL_COUNT):
            raise ValueError("Spelunking tool arrays no longer contain seven aligned entries")

        unlockSource = cls.getSection(TOOL_UNLOCK_SECTION)
        if not unlockSource:
            raise ValueError("Spelunking tool unlock predicate is missing")
        unlocks: Dict[int, SpelunkingToolUnlock] = {}
        defaultBranch = re.search(r"\breturn\s+0\s*==\s*(\w+)", unlockSource)
        if not defaultBranch:
            raise ValueError("Spelunking default tool unlock branch changed")
        toolArgument = re.escape(defaultBranch.group(1))
        unlocks[0] = SpelunkingToolUnlock(kind="default")

        for toolIndex, upgradeIndex in re.findall(
            rf"\b(\d+)\s*==\s*{toolArgument}\s*&&\s*1\s*<=\s*\w+\._customBlock_Spelunk\(\s*\"ShopUpgBonus\"\s*,\s*(\d+)\s*,\s*0\s*\)",
            unlockSource,
        ):
            index, upgrade = int(toolIndex), int(upgradeIndex)
            if index in unlocks or index not in range(1, 5) or upgrade != index + 13:
                raise ValueError("Spelunking tool upgrade unlock mapping changed")
            unlocks[index] = SpelunkingToolUnlock(
                kind="upgrade", upgradeIndex=upgrade, minimumBonus=1
            )
        if set(unlocks) != set(range(5)):
            raise ValueError("Spelunking tool unlock predicate no longer matches tools 0-4")
        toolBranches = [
            int(index) for index in re.findall(rf"\b(\d+)\s*==\s*{toolArgument}\b", unlockSource)
        ]
        if toolBranches != list(range(5)):
            raise ValueError("Spelunking tool unlock predicate has unexpected tool branches")


        for index, name in enumerate(names):
            unlock = unlocks.get(index, SpelunkingToolUnlock(kind="unavailable"))
            tool = SpelunkingTool(
                index=index,
                name=name,
                baseStaminaCost=staminaCosts[index],
                hitRadius=radii[index],
                damageMultiplier=multipliers[index],
                unlock=unlock,
            )
            cls.addList(tool)
            cls.add(str(index), tool)
