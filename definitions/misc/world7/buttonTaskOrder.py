from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class ButtonTaskOrder(IdleonModel):
    cycleIndex: Integer
    selectionValue: Integer
    taskIndex: Integer
