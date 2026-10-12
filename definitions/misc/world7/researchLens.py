from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class ResearchLens(IdleonModel):
    index: Integer
    name: str
    descriptionTemplate: str
