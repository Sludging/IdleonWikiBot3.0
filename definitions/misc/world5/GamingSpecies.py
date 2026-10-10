from typing import Optional

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class GamingSpecies(IdleonModel):
    speciesId: Integer
    name: str
    effectText: Optional[str] = None
