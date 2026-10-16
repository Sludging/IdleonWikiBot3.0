from typing import List

from definitions.misc.world7.tournamentRaid import TournamentRaid, TournamentRewardTier
from helpers.HelperFunctions import getFromMixedArray
from repositories.master.Repository import Repository


class TournamentRaidRepo(Repository[TournamentRaid]):
    """Extract the stable Grand Tournament/Pet Raid tables.

    The readable source rows are parallel arrays, rather than per-record
    ``.split(" ")`` rows.  Keep their source ordering so consumers can join
    the values to the corresponding game index without copying item or
    companion definitions.
    """

    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["TournyStuff", "TournyRewards"]

    @classmethod
    def generateRepo(cls) -> None:
        tournamentData = getFromMixedArray(cls.getSection(0))
        rewardData = getFromMixedArray(cls.getSection(1))

        # TournyStuff[13] contains five named divisions followed by three
        # filler slots.  The parser normalizes those "_" placeholders to an
        # empty string, so omit them from the public rank list.  The adjacent
        # numeric row remains a complete source array because it is the stable
        # rank/material metadata table.
        rankNames = [name for name in tournamentData[13] if name]
        rankMaterials = [int(value) for value in tournamentData[17]]

        # TournyStuff[41] contains the readable tournament background/map
        # labels.  Preserve duplicate labels by retaining their list order.
        mapNames = list(tournamentData[41])
        mapLimits = [int(value) for value in tournamentData[42]]

        rewardTiers = [
            TournamentRewardTier(tier=tier, itemIds=list(itemIds))
            for tier, itemIds in enumerate(rewardData)
        ]
        toAdd = TournamentRaid(
            rankNames=rankNames,
            rankMaterials=rankMaterials,
            mapNames=mapNames,
            mapLimits=mapLimits,
            rewardTiers=rewardTiers,
        )
        cls.add("tournament", toAdd)
        cls.addList(toAdd)
