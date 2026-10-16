from typing import List

from definitions.misc.world7.researchObservation import ResearchObservation
from helpers.HelperFunctions import getFromSplitArray, replaceUnderscores
from repositories.master.Repository import Repository


class ResearchObservationRepo(Repository[ResearchObservation]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["ResearchObservations"]

    @classmethod
    def generateRepo(cls) -> None:
        rows = getFromSplitArray(cls.getSection(), replaceUnderscores=False)
        for index, row in enumerate(rows):
            if row[0] == "Name":
                continue
            toAdd = ResearchObservation(
                index=index,
                name=replaceUnderscores(row[0]),
                requiredResearchLevel=row[1],
                mapId=row[2],
                x=row[3],
                y=row[4],
                x5=row[5],
                discoveryRollRequirement=row[6],
                hint=replaceUnderscores(row[7]),
            )
            cls.addList(toAdd)
            cls.add(str(index), toAdd)
