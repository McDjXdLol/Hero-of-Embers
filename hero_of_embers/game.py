import random
import sys

from hero_of_embers.handlers.battle_handler import BattleHandler
from hero_of_embers.handlers.enemies_handler import EnemiesInit
from flag_manager import FlagManager
from get_language_text import GetTexts
from hero_of_embers.handlers.save_handler import SaveGame
from hero_of_embers.handlers.items_handler import ItemsInit
from data_manager import SceneManager


class Game:
    def __init__(self, ui, player, lang):
        self.player = player
        self.lang = lang
        self.ui = ui
        self.scene_manager = SceneManager(self.lang)
        self.enemies_init = EnemiesInit(self.lang)
        self.flag_manager = FlagManager()
        self.items_init = ItemsInit(self.lang)
        self.its_setting = False

    def main(self):
        while True:
            self.ui.change_text(
                self.scene_manager.get_scene_data(self.scene_manager.DESCRIPTION).format(name=self.player.name))

            # If it's not last scene
            # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            if not self.scene_manager.get_scene_data(self.scene_manager.IS_LAST_SCENE):

                # Choice handling
                # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                choices_ids = []
                # Print all choices
                for nr, choice in enumerate(self.scene_manager.get_scene_choices()):
                    self.ui.change_text(f"{nr + 1}. {choice[1]}")
                    choices_ids.append(choice[0])

                self.ui.change_text(GetTexts.load_texts("plot_show_inventory", self.lang))
                self.its_setting = False

                # Get choice from user
                choice_nr = self.ui.get_input("str", "")
                try:
                    choice_nr = int(choice_nr)
                    self.its_setting = False
                except ValueError:
                    self.its_setting = True

                # Check if user entered wrong number
                if not self.its_setting and choice_nr - 1 >= len(choices_ids):
                    self.ui.change_text(GetTexts.load_texts("plot_no_option", self.lang))
                    continue
                elif not self.its_setting and choice_nr - 1 <= -1:
                    self.ui.change_text(GetTexts.load_texts("plot_no_option", self.lang))
                    continue
                elif self.its_setting:
                    match choice_nr.lower():
                        case "i":
                            self.player.inventory.show_inv()
                            continue
                        case "t":
                            # Trading
                            continue
                        case "s":
                            SaveGame(self.player, self.scene_manager, self.flag_manager)
                            sys.exit()
                        case "e":
                            sys.exit()
                        case _:
                            self.ui.change_text(GetTexts.load_texts("plot_no_option", self.lang))
                            continue
                if not self.its_setting:
                    choice_nr -= 1
                # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                # Text of choice that player choose
                self.ui.change_text(self.scene_manager.get_choices_data(choice_nr, "outcome_text"))

                # If in this scene is fight
                # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
                if self.scene_manager.get_choices_data(choice_nr, self.scene_manager.IS_FIGHT):
                    # Enemy data
                    enemy_id = self.scene_manager.get_choices_data(choice_nr, self.scene_manager.ENEMY_ID)
                    enemy = self.enemies_init.get_enemy(enemy_id)

                    # Battle object
                    battle = BattleHandler(self.player, enemy, self.ui, self.lang)

                    # Battle starts
                    # ___________________________________________________________________________________________________________
                    if battle.battle():
                        # Fight won
                        # =======================================================================================================

                        # Give player random drop
                        # -------------------------------------------------------------------------------------------------------
                        drop_data = self.enemies_init.get_enemy_drop(enemy_id)
                        for item in drop_data:

                            # Chances to drop
                            if random.random() < item[1]:
                                self.ui.change_text(GetTexts().load_texts("battle_enemy_item_drop", self.lang).format(
                                    drop_name=self.items_init.get_item(item[0])[0][0]))
                                self.player.inventory.add_to_inv(self.items_init.get_item(item[0]),
                                                                 self.player.inventory.inventory, 1)
                        # -------------------------------------------------------------------------------------------------------

                        # Set flags after win
                        # -------------------------------------------------------------------------------------------------------
                        flag_to_set = self.scene_manager.get_fight_result_data(choice_nr, True,
                                                                               self.scene_manager.FLAGS)
                        self.flag_manager.add_flag(flag_to_set)
                        # -------------------------------------------------------------------------------------------------------

                        # Give player item after win
                        # -------------------------------------------------------------------------------------------------------
                        item_id_to_give = self.scene_manager.get_fight_result_data(choice_nr, True,
                                                                                   self.scene_manager.GIVE_ITEM)
                        # -------------------------------------------------------------------------------------------------------

                        # Check if there is item to give after winning
                        # -------------------------------------------------------------------------------------------------------
                        if not item_id_to_give is None:
                            for item_id in item_id_to_give:
                                # Give item to player
                                item_to_give = self.items_init.get_item(item_id)
                                self.ui.change_text(
                                    GetTexts.load_texts("battle_enemy_item_drop", self.lang).format(
                                        drop_name=item_to_give[0][0]))
                                self.player.inventory.add_to_inv(item_to_give, self.player.inventory.inventory, 1)
                        # -------------------------------------------------------------------------------------------------------

                        # Set next scene
                        # -------------------------------------------------------------------------------------------------------
                        self.scene_manager.set_current_scene(
                            self.scene_manager.get_fight_result_data(choice_nr, True, self.scene_manager.GO_TO_SCENE))
                        # -------------------------------------------------------------------------------------------------------
                        # =======================================================================================================


                    else:
                        # Fight lose
                        # =======================================================================================================

                        # Set flags after lose
                        # -------------------------------------------------------------------------------------------------------
                        flag_to_set = self.scene_manager.get_fight_result_data(choice_nr, False,
                                                                               self.scene_manager.FLAGS)
                        self.flag_manager.add_flag(flag_to_set)
                        # -------------------------------------------------------------------------------------------------------

                        # Give items after lose
                        # -------------------------------------------------------------------------------------------------------
                        item_to_give = self.items_init.get_fight_item_by_choice_id(choice_nr, False)
                        self.ui.change_text(
                            GetTexts.load_texts("battle_enemy_item_drop", self.lang).format(
                                drop_name=item_to_give[0][0][0]))
                        self.player.inventory.add_to_inv(item_to_give)
                        # -------------------------------------------------------------------------------------------------------

                        # Set next scene
                        # -------------------------------------------------------------------------------------------------------
                        self.scene_manager.set_current_scene(
                            self.scene_manager.get_fight_result_data(choice_nr, False, self.scene_manager.GO_TO_SCENE))
                        # -------------------------------------------------------------------------------------------------------
                        # =======================================================================================================
                    # ___________________________________________________________________________________________________________
                # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
                else:
                    # If there is no fight
                    # =======================================================================================================

                    # Set flags
                    # -------------------------------------------------------------------------------------------------------
                    flag_to_set = self.scene_manager.get_choices_data(choice_nr, self.scene_manager.FLAGS)
                    self.flag_manager.add_flag(flag_to_set)
                    # -------------------------------------------------------------------------------------------------------

                    # Give item
                    # -------------------------------------------------------------------------------------------------------
                    item_id_to_give = self.scene_manager.get_choices_data(choice_nr, self.scene_manager.GIVE_ITEM)
                    item_to_give = self.items_init.get_item(item_id_to_give)

                    if len(item_to_give) != 0:
                        self.ui.change_text(
                            GetTexts.load_texts("battle_enemy_item_drop", self.lang).format(
                                drop_name=item_to_give[0][0][0]))

                    self.player.inventory.add_to_inv(self.player.inventory.inventory, item_to_give, 1)
                    # -------------------------------------------------------------------------------------------------------

                    # Change scene
                    # -------------------------------------------------------------------------------------------------------
                    self.scene_manager.set_current_scene(
                        self.scene_manager.get_choices_data(choice_nr, self.scene_manager.GO_TO_SCENE))
                    # -------------------------------------------------------------------------------------------------------
                    # =======================================================================================================
            # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            else:
                break


if __name__ == "__main__":
    from ui_manager import UI
    from hero_of_embers.player_data.player import Player

    Game(UI("en"), Player(name="DEBUG", hp=50, armor=0, damage=5, player_class="", ui=UI("en"), lang="en"), "en").main()
