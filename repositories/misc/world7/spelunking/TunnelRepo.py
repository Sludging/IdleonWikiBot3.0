from typing import List

from definitions.misc.world7.spelunking.tunnel import SpelunkingTunnel
from helpers.HelperFunctions import getFromSplitArray
from repositories.misc.world7.spelunking.DiscoveryRepo import SpelunkingDiscoveryRepo
from repositories.master.Repository import Repository


class SpelunkingTunnelRepo(Repository[SpelunkingTunnel]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["Spelunking"]

    @classmethod
    def initDependencies(cls, log = True):
        SpelunkingDiscoveryRepo.initialise(cls.codeReader, log)

    @classmethod
    def generateRepo(cls) -> None:
        data = getFromSplitArray(cls.getSection())
        
        tunnelNames = data[6]
        bossDepths = data[7]
        loreBonuses = data[14]
        for index, tunnel in enumerate(tunnelNames):
            # Get all discoveries
            discoveries = SpelunkingDiscoveryRepo.itemsList()

            # Filter discoveries by tunnel index
            tunnelDiscoveries = []
            for discovery in discoveries:
                if discovery.tunnelIndex == index:
                    tunnelDiscoveries.append(discovery)

            toAdd = SpelunkingTunnel(
                index = index,
                name = tunnel,
                loreBonus = loreBonuses[index],
                # Boss depth is the value + 1, because .. Lava
                bossDepth = int(bossDepths[index]) + 1,
                discoveries = tunnelDiscoveries,
            )
            cls.addList(toAdd)
            cls.add(toAdd.index, toAdd)
