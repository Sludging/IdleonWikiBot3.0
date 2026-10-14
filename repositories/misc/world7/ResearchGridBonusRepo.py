from typing import List

from definitions.misc.world7.researchGridBonus import ResearchGridBonus
from helpers.HelperFunctions import formatStr, getFromSplitArray
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
        data = getFromSplitArray(cls.getSection(), replaceUnderscores=False)
        for index, line in enumerate(data):
            fields = [formatStr(field, replaceUnderscores=True) for field in line[:-1]]
            description = line[-1].replace("_", " ")
            toAdd = ResearchGridBonus.fromList([index, *fields, description])
            cls.addList(toAdd)
            cls.add(f"{index}", toAdd)
