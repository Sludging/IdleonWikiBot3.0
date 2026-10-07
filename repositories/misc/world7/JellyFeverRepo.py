from typing import List

from definitions.misc.world7.jellyFever import JellyFever
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class JellyFeverRepo(Repository[JellyFever]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["JellyFeverDisplay"]

    @classmethod
    def generateRepo(cls) -> None:
        names, descriptions = getFromSplitArray(cls.getSection())
        for index, name in enumerate(names):
            toAdd = JellyFever(
                index=index,
                name=name,
                description=descriptions[index],
            )
            cls.addList(toAdd)
            cls.add(f"{index}", toAdd)
