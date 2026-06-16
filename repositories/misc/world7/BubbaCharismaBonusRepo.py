from typing import List

from definitions.misc.world7.bubbaCharismaBonus import BubbaCharismaBonus
from helpers.HelperFunctions import getFromSplitArray, replaceUnderscores
from repositories.master.Repository import Repository


class BubbaCharismaBonusRepo(Repository[BubbaCharismaBonus]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["Spelunking"]

    @classmethod
    def generateRepo(cls) -> None:
        data = getFromSplitArray(cls.getSection())
        # data[34] = charisma descriptions, data[35] = names, data[36] = values
        descs = data[34]
        names = data[35]
        values = data[36]

        for n, name in enumerate(names):
            desc = replaceUnderscores(descs[n])
            # Hustle's desc is "}x____" in the codefile; the game replaces "____" with a flesh icon
            if name == "Hustle":
                desc = "}x Flesh"
            toAdd = BubbaCharismaBonus(
                name=replaceUnderscores(name),
                desc=desc,
                value=values[n],
            )
            cls.addList(toAdd)
            cls.add(f"{n}", toAdd)
