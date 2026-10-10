from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class GamingImport(IdleonModel):
    importId: Integer
    name: str
    effectText: str
    upgradeBonusText: str
    boxId: Integer
    flavorText: str
