from typing import List

from definitions.misc.world7.poppyMegafish import PoppyMegafish
from helpers.HelperFunctions import replaceUnderscores
from repositories.master.Repository import Repository


class PoppyMegafishRepo(Repository[PoppyMegafish]):

    # Megafish data is hardcoded in actor initialization code, not in a data function
    NAMES = "Squid,Sequin,Nautilus,Koi,Angler,Leech,Aquaray,Jettison,Shoal,Eel,Marlin,Eclectic".split(",")
    DESCS = (
        "Unlocks_the_first_3_upgrades_in_the_Tar_Pit,_visit_through_top_left_corner"
        "|Boosts_all_of_Poppy's_Bonuses_by_1.5x_their_base_amount"
        "|Adds_two_more_Reset_Spirals_to_upgrade,_and_gives_+5_Pts_when_Fisheroo_Resetting"
        "|Boosts_all_of_Poppy's_Bonuses_by_2x_their_base_amount."
        "|Unlocks_another_3_upgrades_in_the_Tar_Pit,_and_boosts_Tartar_Fish_gain_by_3x"
        "|The_Fishing_Buddy_upgrade_now_gives_+50%_Bluefin_caught_and_+50%_Shiny_Speed_per_Lv_past_Lv.5!"
        "|Boosts_all_of_Poppy's_Bonuses_by_2.5x_their_base_amount"
        "|Unlocks_the_final_2_upgrades_in_the_Tar_Pit,_and_boosts_Tartar_Fish_gain_by_another_3x"
        "|Boosts_all_of_Poppy's_Bonuses_by_3x_their_base_amount"
        "|Shiny_fishing_is_1%_faster_per_upgrade_LV_of_the_Tasty_Fishbait_upgrade"
        "|All_upgrades,_including_Tar_Pit_upgrades,_are_5%_cheaper_per_LV_of_King_Worm_upgrade"
        "|Poppy's_bonuses_are_now_{x_higher_than_they_were_at_first"
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
            toAdd = PoppyMegafish(
                name=name,
                desc=replaceUnderscores(cls.DESCS[n]),
            )
            cls.addList(toAdd)
            cls.add(f"{n}", toAdd)
