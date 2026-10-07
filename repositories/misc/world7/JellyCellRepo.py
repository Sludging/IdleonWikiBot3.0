from typing import List

from definitions.misc.world7.jellyCell import JellyCell
from helpers.HelperFunctions import getFromMixedArray, getFromSplit, replaceUnderscores
from repositories.master.Repository import Repository


class JellyCellRepo(Repository[JellyCell]):
    RESEARCH_FOOTPRINT_ROW = 49

    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return [
            "Research",
            "JellyCellNames",
            "JellyCellPassives",
            "JellyCellDamageCoefficients",
            "JellyCellCooldownCoefficients",
        ]

    @classmethod
    def generateRepo(cls) -> None:
        research = getFromMixedArray(cls.getSection(), respectDelimiter=True)
        names = getFromSplit(cls.getSection(1))
        passives = getFromSplit(cls.getSection(2))
        damage = getFromSplit(cls.getSection(3))
        cooldowns = getFromSplit(cls.getSection(4))
        footprints = research[cls.RESEARCH_FOOTPRINT_ROW]
        if any(len(values) != len(names) for values in (footprints, damage, cooldowns)):
            raise ValueError("Jelly cell footprints and attack coefficients must align with cell names")

        for index, name in enumerate(names):
            offsets = footprints[index].split(",")
            toAdd = JellyCell(
                index=index,
                name=replaceUnderscores(name),
                tileCount=len(offsets),
                footprintOffsets=offsets,
                passiveDescription=replaceUnderscores(passives[index]) if index < len(passives) else None,
                # Source coefficients precede runtime multipliers; cooldown is not seconds.
                damageCoefficient=damage[index],
                attackCooldownCoefficient=cooldowns[index],
            )
            cls.addList(toAdd)
            cls.add(f"{index}", toAdd)
