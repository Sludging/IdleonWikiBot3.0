from typing import List

from definitions.misc.world5.GamingSpecies import GamingSpecies
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class GamingSpeciesRepo(Repository[GamingSpecies]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/5"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["GamingMetadata"]

    @classmethod
    def generateRepo(cls) -> None:
        # Disable helper normalization so mutation text keeps its pipe tokens.
        data = getFromSplitArray(cls.getSection(), replaceUnderscores=False)
        names = (
            "Sprout",
            "Fungi",
            "Bonsai",
            "Cactus",
            "Blossom",
            "Voraci",
            "Berri Bush",
            "Evergreen",
            "Chemical",
            "Royale",
        )
        # Species 0 is empty; row 0 holds effects for mutation species 2..10.
        for speciesId, name in enumerate(names, start=1):
            species = GamingSpecies(
                speciesId=speciesId,
                name=name,
                effectText=(data[0][speciesId - 2].replace("_", " ")
                            if speciesId > 1 else None),
            )
            cls.addList(species)
            cls.add(str(speciesId), species)
