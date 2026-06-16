from typing import List

from definitions.misc.world5.hole.holeJarBonus import HoleJarBonus
from helpers.HelperFunctions import getFromSplitArray, replaceUnderscores
from repositories.master.Repository import Repository


class HoleJarBonusRepo(Repository[HoleJarBonus]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/5/Hole"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["HoleInfo"]

    @classmethod
    def generateRepo(cls) -> None:
        data = getFromSplitArray(cls.getSection())
        # data[54] = jar bonus entries, each is a space-joined string:
        # "NAME WORDS... bonus Filler description..."
        # Name is all uppercase words until a numeric token
        for n, entry in enumerate(data[54]):
            parts = entry.split(" ")
            # Find where the name ends (first numeric token)
            split_idx = next(i for i, p in enumerate(parts) if p.lstrip("-").isdigit())
            name = " ".join(parts[:split_idx])
            bonus = parts[split_idx]
            filler1 = parts[split_idx + 1]
            desc = " ".join(parts[split_idx + 2:])
            toAdd = HoleJarBonus(
                name=name,
                bonus=bonus,
                filler1=filler1,
                description=desc,
            )
            cls.addList(toAdd)
            cls.add(f"{n}", toAdd)
