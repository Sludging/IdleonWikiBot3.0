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
        return ["ButtonTasks"]

    @classmethod
    def generateRepo(cls) -> None:
        data = getFromMixedArray(cls.getSection())
        for index, line in enumerate(data):
            toAdd = ButtonTask.fromList([index, *line])
            cls.addList(toAdd)
            cls.add(f"{index}", toAdd)
