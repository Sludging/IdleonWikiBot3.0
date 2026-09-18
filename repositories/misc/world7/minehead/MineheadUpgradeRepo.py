from typing import List

from definitions.misc.world7.minehead.MineheadUpgrade import MineheadUpgrade
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class MineheadUpgradeRepo(Repository[MineheadUpgrade]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["MineheadUpgrades"]

    @classmethod
    def generateRepo(cls) -> None:
        data = getFromSplitArray(cls.getSection())
        for index, line in enumerate(data):
            toAdd = MineheadUpgrade.fromList([index, *line])
            cls.addList(toAdd)
            cls.add(f"{index}", toAdd)
