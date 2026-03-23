from typing import List

from definitions.misc.world7.tomeEpilogueBonus import TomeEpilogueBonus
from helpers.HelperFunctions import getFromSplitArray, replaceUnderscores
from repositories.master.Repository import Repository


class TomeEpilogueBonusRepo(Repository[TomeEpilogueBonus]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["Spelunking"]

    @classmethod
    def generateRepo(cls) -> None:
        data = getFromSplitArray(cls.getSection())
        # data[20] = bonus descriptions, data[21] = space-separated x0 x1 values
        descs = data[20]
        values = data[21]

        for n, desc in enumerate(descs):
            parts = values[n].split(" ")
            toAdd = TomeEpilogueBonus(
                bonus=replaceUnderscores(desc),
                x0=parts[0],
                x1=parts[1],
            )
            cls.addList(toAdd)
            cls.add(f"{n}", toAdd)
