from typing import List

from definitions.misc.world7.orionMegafeather import OrionMegafeather
from helpers.HelperFunctions import replaceUnderscores
from repositories.master.Repository import Repository


class OrionMegafeatherRepo(Repository[OrionMegafeather]):

    # Megafeather data is hardcoded in actor initialization code, not in a data function
    NAMES = "Maple,Amethyst,Frostraven,Phoenix,Obsidian,Evergreen,Pristine,Lavathian,Midas,Fractal".split(",")
    DESCS = (
        "Multiplies_all_Feather_generation_by_10x._Multiplicative,_so_extra_powerful!"
        "|Boosts_all_of_Orion's_Bonuses_by_double_their_base_amount."
        "|All_upgrades_cost_1%_less_feathers_per_LV_of_Feather_Generation."
        "|Instead_of_double,_all_of_Orion's_Bonuses_are_now_triple."
        "|The_Feather_Cheapener_upgrades_now_give_+2_and_+4_Feathers/sec_each_LV,_respectively."
        "|Forget_triple,_Orion's_Bonuses_are_now_quadruple!"
        "|The_upgrade_Feather_Restart_now_gives_a_5x_feather_bonus_instead_of_the_previous_3x."
        "|Quadruple?_Pfft_more_like_Noobruple,_Orion's_Bonuses_are_now_Quintuple_as_big,_that's_5x!"
        "|The_cost_of_Feather_Generation_upgrade_now_goes_up_25%_slower."
        "|Orion's_bonuses_are_now_{x_higher_than_they_were_at_first."
    ).split("|")

    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/7"

    @classmethod
    def getSections(cls) -> List[str]:
        return []

    @classmethod
    def generateRepo(cls) -> None:
        for n, name in enumerate(cls.NAMES):
            toAdd = OrionMegafeather(
                name=name,
                desc=replaceUnderscores(cls.DESCS[n]),
            )
            cls.addList(toAdd)
            cls.add(f"{n}", toAdd)
