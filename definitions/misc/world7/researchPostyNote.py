from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class ResearchPostyNote(IdleonModel):
    index: Integer
    requiredResearchLevel: Integer
    description: str
    hiddenX: Integer
    hiddenY: Integer
    rotationDegrees: Integer
    shownX: Integer
    shownY: Integer
