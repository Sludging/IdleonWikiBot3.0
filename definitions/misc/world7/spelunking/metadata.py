from typing import List, Optional

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class SpelunkingRewardLabel(IdleonModel):
    dropCode: str
    displayName: str


class SpelunkingItemDrop(IdleonModel):
    dropCode: str
    itemId: str
    displayName: str
    # None means no tunnel-specific restriction, not unconditional availability.
    tunnelIndex: Optional[Integer] = None
    unlockUpgradeIndex: Optional[Integer] = None


class SpelunkingMetadata(IdleonModel):
    rewardLabels: List[SpelunkingRewardLabel]
    itemDrops: List[SpelunkingItemDrop]
