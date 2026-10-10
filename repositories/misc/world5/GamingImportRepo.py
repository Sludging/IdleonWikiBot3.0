from typing import List

from definitions.misc.world5.GamingImport import GamingImport
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class GamingImportRepo(Repository[GamingImport]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/5"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["GamingMetadata"]

    @classmethod
    def generateRepo(cls) -> None:
        # Preserve pipe and brace tokens while decoding display underscores.
        data = getFromSplitArray(cls.getSection(), replaceUnderscores=False)
        # Rows 1/2/4/5 contain names/flavor/effects/upgrades. ID 9 is "idk".
        for importId, name in enumerate(data[1][:9]):
            gamingImport = GamingImport(
                importId=importId,
                name=name.replace("_", " "),
                effectText=data[4][importId].replace("_", " "),
                upgradeBonusText=data[5][importId].replace("_", " "),
                boxId=importId,
                flavorText=data[2][importId].replace("_", " "),
            )
            cls.addList(gamingImport)
            cls.add(str(importId), gamingImport)
