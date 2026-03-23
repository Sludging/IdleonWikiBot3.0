from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class EventShopBonus(IdleonModel):
    name: str
    desc: str
    price: Integer
