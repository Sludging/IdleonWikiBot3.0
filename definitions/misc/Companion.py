from typing import Optional

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric, Integer


class Companion(IdleonModel):
	id: str
	desc: str
	bonus: Numeric
	x1: Integer
	x2: Integer
	x3: Integer
	x4: Integer
	x5: Integer
	x6: Optional[Integer] = None
	x7: Optional[Integer] = None
	desc2: Optional[str] = None
	bonus2: Optional[Numeric] = None
