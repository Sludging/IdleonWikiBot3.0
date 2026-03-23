from typing import List

from definitions.misc.world7.bubbaGift import BubbaGift
from helpers.HelperFunctions import getFromSplitArray, replaceUnderscores
from repositories.master.Repository import Repository


class BubbaGiftRepo(Repository[BubbaGift]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["Spelunking"]

    @classmethod
    def generateRepo(cls) -> None:
        data = getFromSplitArray(cls.getSection())
        # data[38] = gift names, data[39] = descriptions, data[40] = values
        names = data[38]
        descs = data[39]
        values = data[40]

        for n, name in enumerate(names):
            desc = replaceUnderscores(descs[n])
            # The game uses 貴貯 as a separator between passive and active gift descriptions
            desc = desc.replace(" @ 貴貯 @ ", ". ")
            toAdd = BubbaGift(
                name=replaceUnderscores(name),
                desc=desc,
                value=values[n],
            )
            cls.addList(toAdd)
            cls.add(f"{n}", toAdd)
