from typing import List

from definitions.misc.world7.jellyOperatorUpgrade import JellyOperatorUpgrade
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class JellyOperatorUpgradeRepo(Repository[JellyOperatorUpgrade]):
    EXPECTED_FIELDS = 6

    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["JellyOperatorUpgrades"]

    @classmethod
    def generateRepo(cls) -> None:
        data = getFromSplitArray(cls.getSection())
        for index, line in enumerate(data):
            if len(line) != cls.EXPECTED_FIELDS:
                raise ValueError("Jelly Operator upgrades must contain six fields")

            toAdd = JellyOperatorUpgrade.fromList([index, *line])
            cls.addList(toAdd)
            cls.add(f"{index}", toAdd)
