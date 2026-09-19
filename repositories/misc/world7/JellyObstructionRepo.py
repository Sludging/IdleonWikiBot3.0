from typing import List

from definitions.misc.world7.jellyObstruction import JellyObstruction
from helpers.HelperFunctions import getFromMixedArray
from repositories.master.Repository import Repository


class JellyObstructionRepo(Repository[JellyObstruction]):
    RESEARCH_NAMES_ROW = 45
    RESEARCH_DESCRIPTIONS_ROW = 46
    RESEARCH_BONUSES_ROW = 47

    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["Research"]

    @classmethod
    def generateRepo(cls) -> None:
        data = getFromMixedArray(cls.getSection())
        requiredRows = [
            cls.RESEARCH_NAMES_ROW,
            cls.RESEARCH_DESCRIPTIONS_ROW,
            cls.RESEARCH_BONUSES_ROW,
        ]
        if len(data) <= max(requiredRows):
            raise ValueError("Research section does not contain Jelly obstruction rows")

        names = data[cls.RESEARCH_NAMES_ROW]
        descriptions = data[cls.RESEARCH_DESCRIPTIONS_ROW]
        bonuses = data[cls.RESEARCH_BONUSES_ROW]
        if len(names) != len(descriptions) or len(names) != len(bonuses):
            raise ValueError("Jelly obstruction rows must have matching lengths")

        for index, name in enumerate(names):
            toAdd = JellyObstruction(
                index=index,
                name=name,
                description=descriptions[index],
                bonusValue=bonuses[index],
            )
            cls.addList(toAdd)
            cls.add(f"{index}", toAdd)
