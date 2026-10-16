from typing import List

from definitions.misc.world7.orbletMarketBonus import OrbletMarketBonus
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class OrbletMarketBonusRepo(Repository[OrbletMarketBonus]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["OrbletMarket"]

    @classmethod
    def generateRepo(cls) -> None:
        rows = getFromSplitArray(cls.getSection(), replaceUnderscores=False)
        for index, row in enumerate(rows):
            bonus = OrbletMarketBonus.fromList([index, *row])
            cls.addList(bonus)
            cls.add(f"{index}", bonus)
