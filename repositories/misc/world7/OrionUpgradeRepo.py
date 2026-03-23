from typing import List

from definitions.misc.world7.orionUpgrade import OrionUpgrade
from helpers.HelperFunctions import getFromSplitArray, replaceUnderscores
from repositories.master.Repository import Repository


class OrionUpgradeRepo(Repository[OrionUpgrade]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["Owlz"]

    @classmethod
    def generateRepo(cls) -> None:
        data = getFromSplitArray(cls.getSection())
        # Orion upgrades are indices 0-8 of Owlz
        # Each entry: name|part x0 x1 unlock bonusText desc x2
        for n in range(9):
            line = data[n]
            toAdd = OrionUpgrade(
                name=replaceUnderscores(line[0].replace("|", " ")),
                x0=line[1],
                x1=line[2],
                unlock=line[3],
                desc=replaceUnderscores(line[5]),
                x2=line[6],
            )
            cls.addList(toAdd)
            cls.add(f"{n}", toAdd)
