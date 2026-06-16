from typing import List

from definitions.misc.world7.spelunking.chapter import SpelunkingChapter, ChapterBonus
from helpers.HelperFunctions import getFromArrayArray, getFromSplit, replaceUnderscores
from repositories.master.Repository import Repository


class SpelunkingChapterRepo(Repository[SpelunkingChapter]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["SpelunkChapters"]

    @classmethod
    def generateRepo(cls) -> None:

        chapterNames = ["The fear within", "Decay surrounds", "This is gospel", "No escape", "Sunken Plunder", "Kelp Primeval", "FILLER"]

        # 2d array, bonuses grouped by chapter
        data = getFromArrayArray(cls.getSection(), repU = False)
        # For each chapter
        for index, chapterData in enumerate(data):
            # For each bonus in the chapter
            chapterBonuses = []
            for rawBonus in chapterData:
                # Get the bonus data
                bonus = getFromSplit(rawBonus)
                # Replace underscores in the name
                bonus[0] = replaceUnderscores(bonus[0])
                
                chapterBonuses.append(ChapterBonus.fromList(bonus))

            toAdd = SpelunkingChapter(
                name = chapterNames[index],
                bonuses = chapterBonuses
            )

            cls.addList(toAdd)
            cls.add(toAdd.name, toAdd)
