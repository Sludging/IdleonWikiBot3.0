from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric


class BubbaGift(IdleonModel):
    name: str
    desc: str
    value: Numeric
