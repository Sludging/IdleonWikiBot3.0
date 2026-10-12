from typing import List

from definitions.misc.world7.researchShape import ResearchPoint, ResearchShape
from helpers.HelperFunctions import getFromMixedArray, replaceUnderscores
from repositories.master.Repository import Repository


class ResearchShapeRepo(Repository[ResearchShape]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["Research"]

    @classmethod
    def generateRepo(cls) -> None:
        research = getFromMixedArray(cls.getSection(), respectDelimiter=True)
        # Research rows: vertices, dimensions, names, templates, bonus percentages.
        vertices = research[0]
        dimensions = research[1]
        names = research[3]
        descriptions = research[4]
        bonuses = research[5]

        for index, name in enumerate(names):
            points = []
            for vertex in vertices[index].split(";"):
                x, y = vertex.split(",")
                points.append(ResearchPoint(x=x, y=y))
            width, height = dimensions[index].split(",")
            toAdd = ResearchShape(
                index=index,
                name=replaceUnderscores(name),
                vertices=points,
                width=width,
                height=height,
                bonusPercent=bonuses[index],
                descriptionTemplate=replaceUnderscores(descriptions[index]),
            )
            cls.addList(toAdd)
            cls.add(str(index), toAdd)
