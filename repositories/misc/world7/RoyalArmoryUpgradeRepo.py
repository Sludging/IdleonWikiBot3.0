from typing import List

from definitions.misc.world7.royalArmoryUpgrade import RoyalArmoryUpgrade
from helpers.HelperFunctions import getFromMixedArray, getFromSplitArray
from repositories.master.Repository import Repository


class RoyalArmoryUpgradeRepo(Repository[RoyalArmoryUpgrade]):
    RESEARCH_DISPLAY_ORDER_ROW = 43

    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["ArmoryUpg", "Research"]

    @classmethod
    def generateRepo(cls) -> None:
        upgrades = getFromSplitArray(cls.getSection())
        research = getFromMixedArray(cls.getSection(1))

        # Research[43] maps in-game shelf positions to ArmoryUpg source indices.
        displayOrder = [int(index) for index in research[cls.RESEARCH_DISPLAY_ORDER_ROW]]
        displayOrderByIndex = {sourceIndex: displayIndex for displayIndex, sourceIndex in enumerate(displayOrder)}

        
        for sourceIndex, data in enumerate(upgrades):
            displayIndex = displayOrderByIndex.get(sourceIndex)
            requiredUpgrades = upgrades[displayIndex][6] if displayIndex is not None else None
            upgrade = RoyalArmoryUpgrade.fromList(
                [sourceIndex, displayIndex, *data[:6], requiredUpgrades, *data[7:]]
            )
            cls.addList(upgrade)
            cls.add(f"{sourceIndex}", upgrade)
