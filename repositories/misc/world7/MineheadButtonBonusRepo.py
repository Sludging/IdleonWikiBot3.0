import re
from typing import List

from definitions.misc.world7.mineheadButtonBonus import MineheadButtonBonus
from repositories.master.Repository import Repository


class MineheadButtonBonusRepo(Repository[MineheadButtonBonus]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["Minehead"]

    @classmethod
    def generateRepo(cls) -> None:
        match = re.search(
            r'"Button_BonusPerTime"\s*==\s*e\)\s*return\s+c\.asNumber\("([^"]+)"\.split',
            cls.getSection(),
        )
        if match is None:
            raise ValueError("Could not find Minehead Button_BonusPerTime values")

        for index, value in enumerate(match.group(1).split(" ")):
            toAdd = MineheadButtonBonus(index=index, bonusPerCycle=value)
            cls.addList(toAdd)
            cls.add(f"{index}", toAdd)
