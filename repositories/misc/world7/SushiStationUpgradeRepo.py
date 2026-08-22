from typing import List

from definitions.misc.world7.sushiStationUpgrade import SushiStationUpgrade
from helpers.HelperFunctions import getFromMixedArray, getFromSplitArray
from repositories.master.Repository import Repository


class SushiStationUpgradeRepo(Repository[SushiStationUpgrade]):
    RESEARCH_UPGRADE_ORDER_ROW = 32
    EXPECTED_FIELDS = 6

    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["SushiUpgrades", "Research"]

    @classmethod
    def generateRepo(cls) -> None:
        upgrades = getFromSplitArray(cls.getSection())
        research = getFromMixedArray(cls.getSection(1))
        if len(research) <= cls.RESEARCH_UPGRADE_ORDER_ROW:
            raise ValueError("Research section does not contain the Sushi upgrade-order row")

        upgradeOrder = [int(index) for index in research[cls.RESEARCH_UPGRADE_ORDER_ROW]]
        if len(upgrades) != len(upgradeOrder):
            raise ValueError("Sushi upgrades and upgrade-order mapping must have matching lengths")

        displayOrderByIndex = {index: displayOrder for displayOrder, index in enumerate(upgradeOrder)}
        if len(displayOrderByIndex) != len(upgrades) or set(displayOrderByIndex) != set(range(len(upgrades))):
            raise ValueError("Sushi upgrade-order mapping must contain every upgrade exactly once")

        for index, upgrade in enumerate(upgrades):
            if len(upgrade) != cls.EXPECTED_FIELDS:
                raise ValueError("Sushi upgrade entries must contain six fields")

            toAdd = SushiStationUpgrade(
                index=index,
                displayOrder=displayOrderByIndex[index],
                name=upgrade[0],
                maxLevel=upgrade[1],
                costExponent=upgrade[2],
                bonusPerLevel=upgrade[3],
                costMultiplier=upgrade[4],
                description=upgrade[5],
            )
            cls.addList(toAdd)
            cls.add(f"{index}", toAdd)
