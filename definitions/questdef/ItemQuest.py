from typing import List

from definitions.component.Component import Component
from definitions.questdef.Quest import Quest


class ItemQuest(Quest):
	ItemReq: List[Component]

	def getRequirements(self) -> List[Component]:
		return self.ItemReq
