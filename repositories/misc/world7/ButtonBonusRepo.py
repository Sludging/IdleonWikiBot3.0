from typing import List

from definitions.misc.world7.buttonBonus import ButtonBonus
from helpers.HelperFunctions import getFromSplit
from repositories.master.Repository import Repository


class ButtonBonusRepo(Repository[ButtonBonus]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["ButtonBonuses"]

    @classmethod
    def generateRepo(cls) -> None:
        names = [
            "Research XP",
            "Minehead Currency",
            "Sushi Bucks",
            "Artifact Odds",
            "Xtra Masterclass Drops",
            "Spelunk POW",
            "Cooking SPD",
            "Crop Evo",
            "Class EXP",
        ]
        values = getFromSplit(cls.getSection())
        if len(values) != len(names):
            raise ValueError(f"Expected {len(names)} Button bonus values, found {len(values)}")

        for index, (name, value) in enumerate(zip(names, values)):
            toAdd = ButtonBonus(index=index, name=name, bonusPerPress=value)
            cls.addList(toAdd)
            cls.add(f"{index}", toAdd)
