from typing import List

from pydantic import conlist

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class CogMatrix(IdleonModel):
	matrixIndex: Integer
	offsets: List[conlist(Integer, min_items = 2, max_items = 2)]
