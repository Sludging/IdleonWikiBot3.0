from typing import List

from definitions.misc.world7.spelunking.elixir import SpelunkingElixir
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class SpelunkingElixirRepo(Repository[SpelunkingElixir]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["Spelunking"]

    @classmethod
    def generateRepo(cls) -> None:
        data = getFromSplitArray(cls.getSection())
        for index, elixir in enumerate(data[16]):
            toAdd = SpelunkingElixir(
                index = index,
                description = elixir,
            )
            cls.addList(toAdd)
            cls.add(toAdd.index, toAdd)
