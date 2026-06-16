from typing import List

from definitions.misc.world7.voteBonus import VoteBonus
from helpers.HelperFunctions import getFromSplitArray, replaceUnderscores
from repositories.master.Repository import Repository


class VoteBonusRepo(Repository[VoteBonus]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["NinjaInfo"]

    @classmethod
    def generateRepo(cls) -> None:
        data = getFromSplitArray(cls.getSection())
        # data[36] = vote bonus triplets: text, bonus, value
        raw = data[36]

        for n in range(0, len(raw), 3):
            toAdd = VoteBonus(
                text=replaceUnderscores(raw[n]),
                bonus=raw[n + 1],
                value=raw[n + 2],
            )
            cls.addList(toAdd)
            cls.add(f"{n // 3}", toAdd)
