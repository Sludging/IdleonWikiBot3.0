import re
from typing import List

from definitions.misc.world7.researchPostyNote import ResearchPostyNote
from helpers.HelperFunctions import getFromMixedArray, replaceUnderscores
from repositories.master.Repository import Repository


class ResearchPostyNoteRepo(Repository[ResearchPostyNote]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["Research", "ResearchPostyNoteUnlock"]

    @classmethod
    def generateRepo(cls) -> None:
        research = getFromMixedArray(cls.getSection(), respectDelimiter=True)
        # Research[2] stores hidden position, rotation, and shown position; [6] stores text.
        layouts = research[2]
        descriptions = research[6]
        intervalMatch = re.search(r"/\s*(\d+)\s*\)", cls.getSection(1))
        if intervalMatch is None:
            raise ValueError("Could not parse Research Posty Note unlock interval")
        interval = int(intervalMatch.group(1))

        for index, description in enumerate(descriptions):
            hiddenX, hiddenY, rotationDegrees, shownX, shownY = layouts[index].split(",")
            toAdd = ResearchPostyNote(
                index=index,
                requiredResearchLevel=(index + 1) * interval,
                description=replaceUnderscores(description),
                hiddenX=hiddenX,
                hiddenY=hiddenY,
                rotationDegrees=rotationDegrees,
                shownX=shownX,
                shownY=shownY,
            )
            cls.addList(toAdd)
            cls.add(str(index), toAdd)
