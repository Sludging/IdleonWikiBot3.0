
import re
from typing import Dict, Type, Union, List

from definitions.itemdef.itemtypes.CommonItem import CommonItem
from definitions.itemdef.itemtypes.ConsumableItem import ConsumeableItem
from definitions.itemdef.itemtypes.EquipItem import EquipItem
from definitions.itemdef.itemtypes.QuestItem import QuestItem
from helpers.HelperFunctions import formatStr
from repositories.Repository import Repository


class ItemDetailRepo(Repository[CommonItem]):

    @classmethod
    def getSections(cls) -> List[str]:
        return ["Items"]

    @ classmethod
    def generateRepo(cls) -> None:

        itemTypes: Dict[str, Type[CommonItem]] = {
            'Item': CommonItem,
            'Quest': QuestItem,
            'Equip': EquipItem,
            'Consumable': ConsumeableItem,
        }

        reNames = r'.\.addNew([a-zA-Z0-9_]*)\("([a-zA-Z0-9_]*)", ..?.?\);'
        reData = r'..\.setReserved\("([a-zA-Z0-9_]*)", ?"?([^\s"]*)"?\)'
        items: Dict[str, Dict[str, Union[str, int]]] = {}
        itemText = formatStr(cls.getSection(), ["\n", "  "])
        itemData = re.split(reNames, itemText)
        for i in range(0, len(itemData), 3):
            if data := re.findall(reData, itemData[i]):
                itemName = itemData[i + 2]
                itemType = itemData[i + 1]
                items[itemName] = {}
                item = items[itemName]
                for atr, val in data:
                    item[atr] = formatStr(val, replaceUnderscores=True)
                item["internalID"] = itemName
                cls.add(itemName, itemTypes[itemType].parse_obj(item))
