from typing import List

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class TournamentRewardTier(IdleonModel):
    """Static item IDs shown in one tournament reward group."""

    tier: Integer
    itemIds: List[str]


class TournamentRaid(IdleonModel):
    """Static Grand Tournament data available in the codefile.

    ``TournyStuff`` mixes these stable arrays with obfuscated localization,
    layout metadata, and values supplied by the tournament service.  Only the
    readable rank/material/map/limit arrays are exposed here.  The source does
    not contain raid opponents, daily difficulty state, standings, or player
    participation data; ``rewardTiers`` therefore represents the complete
    static raid/tournament reward surface without inventing raid state.
    """
    rankNames: List[str]
    rankMaterials: List[Integer]
    mapNames: List[str]
    mapLimits: List[Integer]
    rewardTiers: List[TournamentRewardTier]
