from typing import List

from definitions.misc.world7.buttonTask import ButtonTask
from helpers.HelperFunctions import getFromMixedArray
from repositories.master.Repository import Repository


class ButtonTaskRepo(Repository[ButtonTask]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["ButtonTasks", "Research"]

    @classmethod
    def generateRepo(cls) -> None:
        data = getFromMixedArray(cls.getSection())
        schedule = getFromMixedArray(cls.getSection(1))[39]
        cycleIndexes = [[] for _ in data]
        for cycleIndex, selectionValue in enumerate(schedule):
            taskIndex = int(selectionValue) % len(data)
            cycleIndexes[taskIndex].append(cycleIndex)

        for index, line in enumerate(data):
            toAdd = ButtonTask.fromList([index, *line, cycleIndexes[index]])
            cls.addList(toAdd)
            cls.add(f"{index}", toAdd)
