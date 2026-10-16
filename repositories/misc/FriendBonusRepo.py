import re
from typing import List

from definitions.misc.FriendBonus import FriendBonus
from helpers.HelperFunctions import replaceUnderscores
from repositories.master.Repository import Repository


class FriendBonusRepo(Repository[FriendBonus]):
    @classmethod
    def getCategory(cls) -> str:
        return "Misc"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["FriendBonusLabels", "FriendBonusValues"]

    @classmethod
    def generateRepo(cls) -> None:
        labels = "{%_Total_Damage" + cls.getSection(0)
        descriptions = labels.split(",")
        values = [int(value) for value in re.findall(r"\b(\d+)\s*\*\s*Math\.min", cls.getSection(1))]

        if len(descriptions) < len(values):
            raise ValueError(f"Expected at least {len(values)} friend bonus descriptions, found {len(descriptions)}")

        for index, (description, value) in enumerate(zip(descriptions, values)):
            toAdd = FriendBonus(description=replaceUnderscores(description), value=value)
            cls.addList(toAdd)
            cls.add(f"{index}", toAdd)
