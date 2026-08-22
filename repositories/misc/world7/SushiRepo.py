from typing import List

from definitions.misc.world7.sushi import Sushi
from helpers.HelperFunctions import getFromMixedArray
from repositories.master.Repository import Repository


class SushiRepo(Repository[Sushi]):
    RESEARCH_NAMES_ROW = 30
    RESEARCH_KNOWLEDGE_CATEGORY_ROW = 33
    RESEARCH_KNOWLEDGE_LABELS_ROW = 34
    RESEARCH_KNOWLEDGE_BASE_ROW = 35
    RESEARCH_UNLOCK_DESCRIPTION_ROW = 36
    RESEARCH_UNLOCK_BONUS_ROW = 37

    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["Research"]

    @classmethod
    def generateRepo(cls) -> None:
        data = getFromMixedArray(cls.getSection())
        requiredRows = [
            cls.RESEARCH_NAMES_ROW,
            cls.RESEARCH_KNOWLEDGE_CATEGORY_ROW,
            cls.RESEARCH_KNOWLEDGE_LABELS_ROW,
            cls.RESEARCH_KNOWLEDGE_BASE_ROW,
            cls.RESEARCH_UNLOCK_DESCRIPTION_ROW,
            cls.RESEARCH_UNLOCK_BONUS_ROW,
        ]
        if len(data) <= max(requiredRows):
            raise ValueError("Research section does not contain the Sushi data rows")

        names = data[cls.RESEARCH_NAMES_ROW]
        knowledgeCategories = data[cls.RESEARCH_KNOWLEDGE_CATEGORY_ROW]
        knowledgeLabels = data[cls.RESEARCH_KNOWLEDGE_LABELS_ROW]
        knowledgeBases = data[cls.RESEARCH_KNOWLEDGE_BASE_ROW]
        unlockDescriptions = data[cls.RESEARCH_UNLOCK_DESCRIPTION_ROW]
        unlockBonuses = data[cls.RESEARCH_UNLOCK_BONUS_ROW]

        if len(names) != len(unlockDescriptions) or len(names) != len(unlockBonuses):
            raise ValueError("Sushi names, descriptions, and bonuses must have matching lengths")
        if len(knowledgeLabels) != len(knowledgeBases):
            raise ValueError("Sushi Knowledge labels and base values must have matching lengths")
        if len(knowledgeCategories) > len(names):
            raise ValueError("Sushi Knowledge categories exceed the Sushi name list")

        for index, name in enumerate(names):
            knowledgeCategory = None
            knowledgeBase = None
            if index < len(knowledgeCategories):
                knowledgeIndex = int(knowledgeCategories[index])
                if knowledgeIndex >= len(knowledgeLabels):
                    raise ValueError("Sushi Knowledge category points outside the Knowledge label list")
                knowledgeCategory = knowledgeLabels[knowledgeIndex]
                knowledgeBase = knowledgeBases[knowledgeIndex]

            toAdd = Sushi(
                index=index,
                name=name,
                unlockDescription=unlockDescriptions[index],
                unlockBonus=unlockBonuses[index],
                knowledgeBonusCategory=knowledgeCategory,
                knowledgeBonusBase=knowledgeBase,
            )
            cls.addList(toAdd)
            cls.add(f"{index}", toAdd)
