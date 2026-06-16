from typing import List

from definitions.misc.world7.dancingCoralBonus import DancingCoralBonus
from helpers.HelperFunctions import getFromSplitArray, replaceUnderscores
from repositories.master.Repository import Repository


class DancingCoralBonusRepo(Repository[DancingCoralBonus]):

    # Coral names from UI code (not in a data array)
    CORAL_NAMES = [
        "Reef Coral", "Vibrant Coral", "Glowing Coral", "Char Coral",
        "Neon Coral", "Aegean Coral", "Gilded Coral", "Twisted Coral", "Eternal Coral",
    ]

    # Coral item sources (not in extractable data)
    CORAL_SOURCES = [
        "Generated Daily in Town", "Dropped by Shellslugs", "Dropped by Litterfish",
        "Dropped by Coralcave crab", "Dropped by Pirate Pou", "Dropped by RIPtide",
        "Dropped by RIPtide", "Dropped by RIPtide", "Dropped by RIPtide",
    ]

    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["Spelunking"]

    @classmethod
    def generateRepo(cls) -> None:
        data = getFromSplitArray(cls.getSection())
        # data[22] = costs, data[23] = descriptions, data[24] = bonus values (single chars)
        costs = data[22]
        descs = data[23]
        # data[24] is a single string where each character is a bonus value
        bonuses = data[24][0]

        for n in range(len(descs)):
            toAdd = DancingCoralBonus(
                name=cls.CORAL_NAMES[n] if n < len(cls.CORAL_NAMES) else f"Coral {n}",
                itemSource=cls.CORAL_SOURCES[n] if n < len(cls.CORAL_SOURCES) else "Unknown",
                desc=replaceUnderscores(descs[n]),
                cost=costs[n],
                bonus=bonuses[n],
            )
            cls.addList(toAdd)
            cls.add(f"{n}", toAdd)
