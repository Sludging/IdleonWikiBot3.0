from typing import List

from definitions.misc.world7.spelunking.upgrade import SpelunkingUpgrade
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class SpelunkingUpgradeRepo(Repository[SpelunkingUpgrade]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["SpelunkUpg"]

    @classmethod
    def generateRepo(cls) -> None:
        data = getFromSplitArray(cls.getSection())
        for line in data:
            cls.addList(SpelunkingUpgrade.fromList(line))
            cls.add(line[0], SpelunkingUpgrade.fromList(line))
