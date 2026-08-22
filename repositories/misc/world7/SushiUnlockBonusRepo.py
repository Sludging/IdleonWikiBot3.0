from typing import List

from definitions.misc.world7.sushiUnlockBonus import SushiUnlockBonus
from helpers.HelperFunctions import getFromMixedArray
from repositories.master.Repository import Repository


class SushiUnlockBonusRepo(Repository[SushiUnlockBonus]):
    RESEARCH_UNLOCK_BONUS_ROW = 37

    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["Research"]

    @classmethod
    def generateRepo(cls) -> None:
        data = getFromMixedArray(cls.getSection())
        if len(data) <= cls.RESEARCH_UNLOCK_BONUS_ROW:
            raise ValueError("Research section does not contain the Sushi unlock-bonus row")

        for index, bonus in enumerate(data[cls.RESEARCH_UNLOCK_BONUS_ROW]):
            toAdd = SushiUnlockBonus(index=index, bonus=bonus)
            cls.addList(toAdd)
            cls.add(f"{index}", toAdd)
