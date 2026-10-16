from typing import List

from definitions.misc.world7.minehead.MineheadOpponent import MineheadOpponent
from helpers.HelperFunctions import getFromMixedArray
from repositories.master.Repository import Repository


class MineheadOpponentRepo(Repository[MineheadOpponent]):
    PROGRESSION_COUNT = 32

    RESEARCH_DISPLAY_IDS_ROW = 10
    RESEARCH_NAMES_ROW = 11
    RESEARCH_ORDINAL_LABELS_ROW = 15
    RESEARCH_TITLE_LABELS_ROW = 16
    RESEARCH_BONUS_DESCRIPTIONS_ROW = 19
    RESEARCH_BONUS_VALUES_ROW = 20

    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["Research"]

    @classmethod
    def generateRepo(cls) -> None:
        data = getFromMixedArray(cls.getSection(), replaceUnderscores=True, respectDelimiter=True)

        # Research[10] maps each progression slot to a display ID, and
        # Research[11] stores names by display ID. Research[15], [16], [19],
        # and [20] store ordinal labels, title labels, bonus descriptions,
        # and bonus values by progression slot, respectively.
        displayIds = data[cls.RESEARCH_DISPLAY_IDS_ROW]
        names = data[cls.RESEARCH_NAMES_ROW]
        ordinalLabels = data[cls.RESEARCH_ORDINAL_LABELS_ROW]
        titleLabels = data[cls.RESEARCH_TITLE_LABELS_ROW]
        bonusDescriptions = data[cls.RESEARCH_BONUS_DESCRIPTIONS_ROW]
        bonusValues = data[cls.RESEARCH_BONUS_VALUES_ROW]


        for progressionIndex in range(cls.PROGRESSION_COUNT):
            displayId = int(displayIds[progressionIndex])
            toAdd = MineheadOpponent(
                progressionIndex=progressionIndex,
                displayId=displayId,
                name=names[displayId],
                ordinalLabel=ordinalLabels[progressionIndex],
                titleLabel=titleLabels[progressionIndex],
                bonusDescription=bonusDescriptions[progressionIndex],
                bonusValue=bonusValues[progressionIndex],
            )
            cls.addList(toAdd)
            cls.add(str(progressionIndex), toAdd)
