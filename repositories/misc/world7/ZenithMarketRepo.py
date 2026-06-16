from typing import List

from definitions.misc.world7.zenithMarket import ZenithMarket
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class ZenithMarketRepo(Repository[ZenithMarket]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["ZenithMarket"]

    @classmethod
    def generateRepo(cls) -> None:
        data = getFromSplitArray(cls.getSection())
        for line in data:
            toAdd = ZenithMarket.fromList(line)
            cls.addList(toAdd)
            cls.add(toAdd.name, toAdd)
