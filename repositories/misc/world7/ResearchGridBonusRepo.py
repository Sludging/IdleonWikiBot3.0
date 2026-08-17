from typing import List

from definitions.misc.world7.researchGridBonus import ResearchGridBonus
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class ResearchGridBonusRepo(Repository[ResearchGridBonus]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["ResearchGridBonus"]

    @classmethod
    def generateRepo(cls) -> None:
        data = getFromSplitArray(cls.getSection())
        for index, line in enumerate(data):
            toAdd = ResearchGridBonus.fromList([index, *line])
            cls.addList(toAdd)
            cls.add(f"{index}", toAdd)
