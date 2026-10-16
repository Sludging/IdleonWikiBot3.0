import re
from typing import List

from definitions.misc.world2.shimmerBonus import ShimmerBonus
from helpers.HelperFunctions import replaceUnderscores
from repositories.master.Repository import Repository


class ShimmerBonusRepo(Repository[ShimmerBonus]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/2"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["ShimmerBonuses", "ShimmerBonusLevels"]

    @classmethod
    def generateRepo(cls) -> None:
        descriptions = ["+{,Base_STR"]
        descriptions.extend(re.findall(r'this\._DL1\.push\("([^"]*)"\)', cls.getSection(0)))
        divisors = [12]
        divisors.extend(
            int(value)
            for value in re.findall(
                r'OptionsListAccount"\)\[\d+\]\)\s*/\s*(\d+)',
                cls.getSection(1),
            )
        )

        if len(descriptions) != len(divisors):
            raise ValueError(
                f"Expected matching shimmer bonus descriptions and divisors, "
                f"found {len(descriptions)} and {len(divisors)}"
            )

        for index, (description, divisor) in enumerate(zip(descriptions, divisors)):
            toAdd = ShimmerBonus(
                description=replaceUnderscores(description),
                levelDivisor=divisor,
            )
            cls.addList(toAdd)
            cls.add(f"{index}", toAdd)
