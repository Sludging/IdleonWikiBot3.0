from typing import List

from definitions.misc.world7.eventShopBonus import EventShopBonus
from helpers.HelperFunctions import getFromSplitArray, replaceUnderscores
from repositories.master.Repository import Repository


class EventShopBonusRepo(Repository[EventShopBonus]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["NinjaInfo"]

    @classmethod
    def generateRepo(cls) -> None:
        data = getFromSplitArray(cls.getSection())
        # data[37] = event shop pairs: "name_@_desc" then price, alternating
        raw = data[37]

        for n in range(0, len(raw), 2):
            text = replaceUnderscores(raw[n])
            parts = text.split(" @ ", 1)
            name = parts[0] if len(parts) > 1 else text
            desc = parts[1] if len(parts) > 1 else ""
            toAdd = EventShopBonus(
                name=name,
                desc=desc,
                price=raw[n + 1],
            )
            cls.addList(toAdd)
            cls.add(f"{n // 2}", toAdd)
