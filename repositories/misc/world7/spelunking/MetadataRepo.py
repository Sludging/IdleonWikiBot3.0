import re
from typing import Dict, List

from definitions.misc.world7.spelunking.metadata import (
    SpelunkingItemDrop,
    SpelunkingMetadata,
    SpelunkingRewardLabel,
)
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


# Spelunky[5] follows Number2Letter ordering: amber, then rewards a through k.
REWARD_LABELS_INDEX = 5
REWARD_DROP_CODES = "_abcdefghijk"
EXPECTED_ITEM_DROP_COUNT = 8


class SpelunkingMetadataRepo(Repository[SpelunkingMetadata]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["Spelunking", "SpelunkingRewardOutcomes", "SpelunkingRewardItemImages"]

    @classmethod
    def generateRepo(cls) -> None:
        data = getFromSplitArray(cls.getSection())
        if len(data) <= REWARD_LABELS_INDEX:
            raise ValueError("Spelunking reward label array is missing")
        names = data[REWARD_LABELS_INDEX]
        if len(names) != len(REWARD_DROP_CODES):
            raise ValueError("Spelunking reward labels no longer match drop-code ordering")
        labels = dict(zip(REWARD_DROP_CODES, names))

        outcomes = cls.getSection(1)
        images = cls.getSection(2)
        if not outcomes or not images:
            raise ValueError("Spelunking reward caller sections are missing")

        # Split at each code comparison so counter icons cannot join a later item icon.
        branches = re.split(r'"([a-z])"\s*==', images)
        if branches[1::2] != list(REWARD_DROP_CODES[1:]):
            raise ValueError("Spelunking reward image branches no longer match reward labels")
        itemIds = {}
        for code, branch in zip(branches[1::2], branches[2::2]):
            image = re.search(r'_customBlock_addImgInst\("([^"\n]+)_x1\.png"\)', branch)
            if image:
                itemIds[code] = image.group(1)
        if len(itemIds) != EXPECTED_ITEM_DROP_COUNT:
            raise ValueError("Spelunking item image identities are missing or changed")

        unlockUpgrades: Dict[str, int] = {}
        for upgrade, branch in re.findall(
            r'"ShopUpgBonus",\s*(\d+),\s*0\)(.*?)(?=_customBlock_Spelunk|$)',
            outcomes,
            re.DOTALL,
        ):
            if not re.match(r'\s*&&', branch):
                raise ValueError("Spelunking upgrade prerequisite no longer guards reward outcomes")
            codes = re.findall(r'\.push\("([a-z])"\)', branch)
            for index in re.findall(r'getGameAttribute\("Number2Letter"\)\[(\d+)\]', branch):
                if int(index) >= len(REWARD_DROP_CODES):
                    raise ValueError("Spelunking miscellaneous reward index is out of range")
                codes.append(REWARD_DROP_CODES[int(index)])
            if not codes:
                raise ValueError("Spelunking upgrade prerequisite has no reward outcomes")
            for code in codes:
                if code not in labels or code in unlockUpgrades:
                    raise ValueError("Spelunking reward upgrade join is unknown or duplicated")
                unlockUpgrades[code] = int(upgrade)

        worldItems = re.search(r'_customBlock_Spelunk\("w7itemDropChance",(.*)', outcomes, re.DOTALL)
        if not worldItems:
            raise ValueError("Spelunking tunnel-specific reward outcomes are missing")
        worldBranch = worldItems.group(1)
        guard = re.search(r'\(([^()]+)\)\s*&&\s*\(', worldBranch)
        if not guard:
            raise ValueError("Spelunking item tunnel restriction is missing")
        restrictions = re.findall(r'(\d+)\s*==\s*(this\.\w+\[\d+\])', guard.group(1))
        tunnels = [int(index) for index, _ in restrictions]
        codes = re.findall(r'\.push\("([a-z])"\)', worldBranch)
        explicitBranches = re.findall(
            r'(\d+)\s*==\s*(this\.\w+\[\d+\])\s*\?\s*this\.\w+\.push\("([a-z])"\)',
            worldBranch,
        )
        # The final code is the ternary fallback; the guard permits only one remaining tunnel.
        if (
            not tunnels
            or len(tunnels) != len(codes)
            or len(set(tunnels)) != len(tunnels)
            or len(set(codes)) != len(codes)
            or len({field for _, field in restrictions}) != 1
            or [(int(index), code) for index, _, code in explicitBranches] != list(zip(tunnels, codes))[:-1]
            or any(field != restrictions[0][1] for _, field, _ in explicitBranches)
            or any(code not in itemIds for code in codes)
        ):
            raise ValueError("Spelunking item tunnel restrictions no longer match reward outcomes")
        tunnelIndices = dict(zip(codes, tunnels))
        if set(itemIds) - set(tunnelIndices) != set(itemIds) & set(unlockUpgrades):
            raise ValueError("Spelunking shared item rewards are missing upgrade prerequisites")

        metadata = SpelunkingMetadata(
            rewardLabels = [
                SpelunkingRewardLabel(dropCode = code, displayName = name)
                for code, name in labels.items()
            ],
            itemDrops = [
                SpelunkingItemDrop(
                    dropCode = code,
                    itemId = itemId,
                    displayName = labels[code],
                    tunnelIndex = tunnelIndices.get(code),
                    unlockUpgradeIndex = unlockUpgrades.get(code),
                )
                for code, itemId in itemIds.items()
            ],
        )
        cls.add("metadata", metadata)
        cls.addList(metadata)
