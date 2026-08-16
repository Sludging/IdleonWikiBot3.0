from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class ButtonTask(IdleonModel):
    index: Integer
    description: str
    baseRequirement: Numeric
    scalingType: str
    scalingValue: Numeric
    x4: Integer
