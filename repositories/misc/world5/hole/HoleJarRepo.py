from typing import List

from definitions.misc.world5.hole.holeJar import HoleJar
from helpers.HelperFunctions import getFromSplitArray, replaceUnderscores
from repositories.master.Repository import Repository


class HoleJarRepo(Repository[HoleJar]):

    # Jar type names are hardcoded in the game UI, not in a data array
    JAR_NAMES = [
        "Simple Jar", "Tall Jar", "Ornate Jar", "Great Jar", "Enchanted Jar",
        "Artisan Jar", "Epic Jar", "Gilded Jar", "Ceremony Jar", "Heirloom Jar",
    ]

    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/5/Hole"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["HoleInfo"]

    @classmethod
    def generateRepo(cls) -> None:
        data = getFromSplitArray(cls.getSection())
        # data[52] = jar descriptions
        descs = data[52]

        for n, desc in enumerate(descs):
            toAdd = HoleJar(
                name=cls.JAR_NAMES[n] if n < len(cls.JAR_NAMES) else f"Jar {n}",
                description=replaceUnderscores(desc),
            )
            cls.addList(toAdd)
            cls.add(f"{n}", toAdd)
