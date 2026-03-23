from typing import List

from definitions.misc.world7.bigFishBonus import BigFishBonus
from helpers.HelperFunctions import getFromSplitArray, replaceUnderscores
from repositories.master.Repository import Repository


class BigFishBonusRepo(Repository[BigFishBonus]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["Spelunking"]

    @classmethod
    def generateRepo(cls) -> None:
        data = getFromSplitArray(cls.getSection())
        # data[18] = BigFish bonus entries, each comma-separated
        for n, entry in enumerate(data[18]):
            fields = entry.split(",")
            fields[0] = replaceUnderscores(fields[0])
            fields[1] = replaceUnderscores(fields[1])
            toAdd = BigFishBonus.fromList(fields)
            cls.addList(toAdd)
            cls.add(f"{n}", toAdd)
