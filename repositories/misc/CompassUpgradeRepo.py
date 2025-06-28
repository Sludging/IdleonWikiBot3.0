from typing import List

from definitions.misc.CompassUpgrade import CompassUpgrade
from helpers.Constants import Constants
from helpers.HelperFunctions import replaceUnderscores, getFromSplitArray
from repositories.master.Repository import Repository
from repositories.misc.RandoListRepo import RandoListRepo, RandoListDescriptions


class CompassUpgradeRepo(Repository[CompassUpgrade]):
    @classmethod
    def getCategory(cls) -> str:
        return "Misc"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["CompassUpg"]

    @classmethod
    def initDependencies(cls, log=True) -> None:
        RandoListRepo.initialise(cls.codeReader, False)

    @classmethod
    def generateRepo(cls) -> None:
        grimoire_data = getFromSplitArray(cls.getSection())

        element_upgrades = RandoListRepo.get(RandoListDescriptions.CompassElementalUpgrades).elements
        fighter_upgrades = RandoListRepo.get(RandoListDescriptions.CompassFighterUpgrades).elements
        survival_upgrades = RandoListRepo.get(RandoListDescriptions.CompassSurvivalUpgrades).elements
        nomadic_upgrades = RandoListRepo.get(RandoListDescriptions.CompassNomadicUpgrades).elements
        abomination_upgrades = RandoListRepo.get(RandoListDescriptions.CompassAbominationUpgrades).elements

        for index, data in enumerate(grimoire_data):
            name = data[0]

            upgrade_type = "Unknown"
            if str(index) in element_upgrades:
                upgrade_type = "Elemental"
            elif str(index) in fighter_upgrades:
                upgrade_type = "Fighter"
            elif str(index) in survival_upgrades:
                upgrade_type = "Survival"
            elif str(index) in nomadic_upgrades:
                upgrade_type = "Nomadic"
            elif str(index) in abomination_upgrades:
                upgrade_type = "Abomination"

            upgrade = CompassUpgrade(
                name = name,
                baseCost = data[1],
                costMult = data[2],
                dustType = data[3],
                maxLevel = data[4],
                bonusValue = data[5],
                x2 = data[6],
                x3 = data[7],
                x4 = data[8],
                x5 = data[9],
                x6 = data[10],
                description = data[11],
                upgradeType = upgrade_type
            )

            cls.add(name, upgrade) 
            cls.addList(upgrade)