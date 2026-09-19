from typing import List

from definitions.misc.world7.exoticMarket import ExoticMarketUpgrade
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class ExoticMarketRepo(Repository[ExoticMarketUpgrade]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["MarketExoticInfo"]

    @classmethod
    def generateRepo(cls) -> None:
        rows = getFromSplitArray(cls.getSection())
        for index, row in enumerate(rows):
            # Names are duplicated by the source for the NAME_MAGNI rows;
            # index keys retain every ordered upgrade in the dict export.
            toAdd = ExoticMarketUpgrade.fromList(row)
            cls.addList(toAdd)
            cls.add(f"{index}", toAdd)
