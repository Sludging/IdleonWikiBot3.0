from typing import List

from definitions.misc.world7.bubbaMegaflesh import BubbaMegaflesh
from helpers.HelperFunctions import getFromSplitArray, replaceUnderscores
from repositories.master.Repository import Repository


class BubbaMegafleshRepo(Repository[BubbaMegaflesh]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["Spelunking"]

    @classmethod
    def generateRepo(cls) -> None:
        data = getFromSplitArray(cls.getSection())
        # data[37] = megaflesh descriptions, data[41] = names (ALL_CAPS)
        descs = data[37]
        names = data[41]

        for n, name in enumerate(names):
            toAdd = BubbaMegaflesh(
                name=replaceUnderscores(name).title(),
                desc=replaceUnderscores(descs[n]),
            )
            cls.addList(toAdd)
            cls.add(f"{n}", toAdd)
