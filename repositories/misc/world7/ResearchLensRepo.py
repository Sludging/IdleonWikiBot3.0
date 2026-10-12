from typing import List

from definitions.misc.world7.researchLens import ResearchLens
from helpers.HelperFunctions import getFromMixedArray, replaceUnderscores
from repositories.master.Repository import Repository


class ResearchLensRepo(Repository[ResearchLens]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["Research"]

    @classmethod
    def generateRepo(cls) -> None:
        research = getFromMixedArray(cls.getSection(), respectDelimiter=True)
        names = research[7]
        descriptions = research[8]

        for index, name in enumerate(names):
            toAdd = ResearchLens(
                index=index,
                name=replaceUnderscores(name),
                descriptionTemplate=replaceUnderscores(descriptions[index]),
            )
            cls.addList(toAdd)
            cls.add(str(index), toAdd)
