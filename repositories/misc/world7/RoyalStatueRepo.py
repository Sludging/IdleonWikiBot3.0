from typing import List

from definitions.misc.world7.royalStatue import RoyalStatue
from helpers.HelperFunctions import getFromMixedArray, getFromSplitArray
from repositories.master.Repository import Repository


class RoyalStatueRepo(Repository[RoyalStatue]):
    RESEARCH_DESCRIPTION_ROW = 40
    RESEARCH_BASE_BONUS_ROW = 41
    RESEARCH_BONUS_PER_LEVEL_ROW = 42

    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["Research", "RoyalStatueUnlockOdds", "RoyalStatueAttemptCost"]

    @classmethod
    def generateRepo(cls) -> None:
        research = getFromMixedArray(cls.getSection(0))
        unlockOdds = getFromSplitArray(cls.getSection(1))[0]
        attemptCost = int(cls.getSection(2).strip())

        # Research rows 40-42 contain descriptions, base bonuses, and per-level bonuses.
        for index in range(len(research[cls.RESEARCH_DESCRIPTION_ROW])):
            statue = RoyalStatue(
                index=index,
                description=research[cls.RESEARCH_DESCRIPTION_ROW][index],
                baseBonus=research[cls.RESEARCH_BASE_BONUS_ROW][index],
                bonusPerLevel=research[cls.RESEARCH_BONUS_PER_LEVEL_ROW][index],
                unlockItem=f"RGshard{index}",
                unlockChanceDenominator=unlockOdds[index],
                upgradeItem="RGenh",
                attemptCost=attemptCost,
            )
            cls.addList(statue)
            cls.add(f"{index}", statue)
