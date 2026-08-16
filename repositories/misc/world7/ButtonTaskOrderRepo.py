from typing import List

from definitions.misc.world7.buttonTaskOrder import ButtonTaskOrder
from helpers.HelperFunctions import getFromMixedArray
from repositories.master.Repository import Repository
from repositories.misc.world7.ButtonTaskRepo import ButtonTaskRepo


class ButtonTaskOrderRepo(Repository[ButtonTaskOrder]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["Research"]

    @classmethod
    def initDependencies(cls, log=True) -> None:
        ButtonTaskRepo.initialise(cls.codeReader, log)

    @classmethod
    def generateRepo(cls) -> None:
        data = getFromMixedArray(cls.getSection())
        schedules = [row for row in data if len(row) == 100 and sorted(map(int, row)) == list(range(100))]
        if len(schedules) != 1:
            raise ValueError(f"Expected one 100-entry Button task schedule, found {len(schedules)}")

        schedule = schedules[0]
        taskCount = len(ButtonTaskRepo.itemsList())
        for cycleIndex, selectionValue in enumerate(schedule):
            toAdd = ButtonTaskOrder(
                cycleIndex=cycleIndex,
                selectionValue=selectionValue,
                taskIndex=int(selectionValue) % taskCount,
            )
            cls.addList(toAdd)
            cls.add(f"{cycleIndex}", toAdd)
