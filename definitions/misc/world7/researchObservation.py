from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class ResearchObservation(IdleonModel):
    index: Integer
    name: str
    requiredResearchLevel: Integer
    mapId: Integer
    x: Integer
    y: Integer
    x5: Integer
    discoveryRollRequirement: Integer
    hint: str
