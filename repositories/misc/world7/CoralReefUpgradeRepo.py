from typing import List

from definitions.misc.world7.coralReefUpgrade import CoralReefUpgrade
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class CoralReefUpgradeRepo(Repository[CoralReefUpgrade]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["CoralReef"]

    @classmethod
    def generateRepo(cls) -> None:
        data = getFromSplitArray(cls.getSection())
        for n, line in enumerate(data):
            # Strip trailing filler "_" entry
            entry = line[:13]
            toAdd = CoralReefUpgrade.fromList(entry)
            cls.addList(toAdd)
            cls.add(f"{n}", toAdd)
