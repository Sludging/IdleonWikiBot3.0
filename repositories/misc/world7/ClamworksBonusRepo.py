from typing import List

from definitions.misc.world7.clamworksBonus import ClamworksBonus
from helpers.HelperFunctions import getFromSplitArray, replaceUnderscores
from repositories.master.Repository import Repository


class ClamworksBonusRepo(Repository[ClamworksBonus]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["Spelunking"]

    @classmethod
    def generateRepo(cls) -> None:
        data = getFromSplitArray(cls.getSection())
        # data[27] = descriptions, data[28] = values, data[29] = costs
        descs = data[27]
        values = data[28]
        costs = data[29]

        for n, desc in enumerate(descs):
            toAdd = ClamworksBonus(
                description=replaceUnderscores(desc),
                value=values[n],
                cost=costs[n],
            )
            cls.addList(toAdd)
            cls.add(f"{n}", toAdd)
