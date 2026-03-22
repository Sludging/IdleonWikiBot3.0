from typing import List

from definitions.misc.world7.bubbaUpgrade import BubbaUpgrade
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class BubbaUpgradeRepo(Repository[BubbaUpgrade]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["BubbaUpg"]

    @classmethod
    def generateRepo(cls) -> None:
        data = getFromSplitArray(cls.getSection())
        for line in data:
            cls.addList(BubbaUpgrade.fromList(line))
            cls.add(line[0], BubbaUpgrade.fromList(line))
