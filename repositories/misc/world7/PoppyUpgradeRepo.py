from typing import List

from definitions.misc.world7.poppyUpgrade import PoppyUpgrade
from helpers.HelperFunctions import getFromSplitArray, replaceUnderscores
from repositories.master.Repository import Repository


class PoppyUpgradeRepo(Repository[PoppyUpgrade]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["Owlz"]

    @classmethod
    def generateRepo(cls) -> None:
        data = getFromSplitArray(cls.getSection())
        # Poppy main upgrades are indices 9-20, tarpit upgrades are 21-28
        # Each entry: name|part x0 x1 unlock bonusText desc x2
        for n in range(9, len(data)):
            line = data[n]
            unlock = 0 if line[3] == "Nah" else line[3]
            toAdd = PoppyUpgrade(
                name=replaceUnderscores(line[0].replace("|", " ")),
                x0=line[1],
                x1=line[2],
                unlock=unlock,
                desc=replaceUnderscores(line[5]),
                x2=line[6],
            )
            cls.addList(toAdd)
            cls.add(f"{n - 9}", toAdd)
