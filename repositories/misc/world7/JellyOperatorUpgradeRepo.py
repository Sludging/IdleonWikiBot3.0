from typing import List

from definitions.misc.world7.jellyOperatorUpgrade import JellyOperatorUpgrade
from helpers.HelperFunctions import getFromMixedArray, getFromSplitArray
from repositories.master.Repository import Repository


class JellyOperatorUpgradeRepo(Repository[JellyOperatorUpgrade]):
    EXPECTED_FIELDS = 6
    RESEARCH_DISPLAY_ORDER_ROW = 44

    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["JellyOperatorUpgrades", "Research"]

    @classmethod
    def generateRepo(cls) -> None:
        upgrades = getFromSplitArray(cls.getSection())
        research = getFromMixedArray(cls.getSection(1))
        if len(research) <= cls.RESEARCH_DISPLAY_ORDER_ROW:
            raise ValueError("Research section does not contain Jelly upgrade-order row")

        try:
            displayOrder = [
                int(index) for index in research[cls.RESEARCH_DISPLAY_ORDER_ROW][:len(upgrades)]
            ]
        except (TypeError, ValueError) as error:
            raise ValueError("Jelly upgrade display-order mapping must contain integers") from error

        expectedSourceIndexes = set(range(len(upgrades)))
        if len(displayOrder) != len(upgrades) or set(displayOrder) != expectedSourceIndexes:
            raise ValueError("Jelly upgrade display-order mapping must contain every upgrade exactly once")

        displayIndexBySourceIndex = {
            sourceIndex: displayIndex for displayIndex, sourceIndex in enumerate(displayOrder)
        }
        for index, line in enumerate(upgrades):
            if len(line) != cls.EXPECTED_FIELDS:
                raise ValueError("Jelly Operator upgrades must contain six fields")

            toAdd = JellyOperatorUpgrade.fromList(
                [index, displayIndexBySourceIndex[index], *line]
            )
            cls.addList(toAdd)
            cls.add(f"{index}", toAdd)
