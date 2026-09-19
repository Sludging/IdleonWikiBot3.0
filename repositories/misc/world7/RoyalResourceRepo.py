from typing import List

from definitions.misc.world7.royalResource import RoyalResource
from helpers.HelperFunctions import getFromMixedArray
from repositories.master.Repository import Repository


class RoyalResourceRepo(Repository[RoyalResource]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["RoyalResources"]

    @classmethod
    def generateRepo(cls) -> None:
        rows = getFromMixedArray(cls.getSection(), replaceUnderscores=False)
        for resourceId, row in enumerate(rows):
            # RoyalResources is flattened as 20 node slots for each world.
            world, order = divmod(resourceId, 20)
            toAdd = RoyalResource.fromList([resourceId, world, order, *row])
            cls.addList(toAdd)
            cls.add(f"{resourceId}", toAdd)
