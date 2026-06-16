from typing import List

from definitions.misc.world7.spelunking.discovery import SpelunkingDiscovery
from helpers.HelperFunctions import getFromArrayArray, getFromSplit, replaceUnderscores
from repositories.master.Repository import Repository


class SpelunkingDiscoveryRepo(Repository[SpelunkingDiscovery]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["SpelunkRocks"]

    @classmethod
    def generateRepo(cls) -> None:
        
        # 2d array, discoveries grouped by tunnel
        data = getFromArrayArray(cls.getSection(), repU = False)
        # For each tunnel
        for index, rockData in enumerate(data):
            # For each discovery in the tunnel
            for rawDiscovery in rockData:
                # Get the discovery data
                discovery = getFromSplit(rawDiscovery)
                # Replace underscores in the name
                discovery[0] = replaceUnderscores(discovery[0])
                # Add the tunnel index to the discovery
                discovery = [index] + discovery

                cls.addList(SpelunkingDiscovery.fromList(discovery))
                cls.add(discovery[1], SpelunkingDiscovery.fromList(discovery))
