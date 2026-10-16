import re
from typing import List

from definitions.misc.world2.shimmerChallenge import ShimmerChallenge
from helpers.HelperFunctions import replaceUnderscores
from repositories.master.Repository import Repository


class ShimmerChallengeRepo(Repository[ShimmerChallenge]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/2"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["ShimmerChallenges", "ShimmerChallengeThresholds"]

    @classmethod
    def generateRepo(cls) -> None:
        descriptions = [
            "Get_as_much_total_stats_as_possible,_STR_AGI_WIS_and_LUK_combined."
        ]
        descriptions.extend(re.findall(r'this\._DL1\.push\("([^"]*)"\)', cls.getSection(0)))
        thresholds = [50000]
        thresholds.extend(
            int(float(value))
            for value in re.findall(
                r"this\._DL1\.push\(([-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:e[-+]?\d+)?)\)",
                cls.getSection(1),
                re.IGNORECASE,
            )
        )

        if len(descriptions) != len(thresholds):
            raise ValueError(
                f"Expected matching shimmer challenge descriptions and thresholds, "
                f"found {len(descriptions)} and {len(thresholds)}"
            )

        for index, (description, threshold) in enumerate(zip(descriptions, thresholds)):
            toAdd = ShimmerChallenge(
                description=replaceUnderscores(description),
                threshold=threshold,
            )
            cls.addList(toAdd)
            cls.add(f"{index}", toAdd)
