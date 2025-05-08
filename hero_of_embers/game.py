import random
import time
import sys
import os

from hero_of_embers.enemy import Enemy
from library import Library
from get_language_text import GetTexts
from scene_manager import SceneManager
from trade_handler import TradeHandler
from save_handler import SaveGame
from battle_handler import BattleHandler
from enemies_init import EnemiesInit
from items_init import ItemsInit

class Game:
    def __init__(self, ui, player, lang):
        self.player = player
        self.lang = lang
        self.ui = ui
        self.scene_manager = SceneManager(self.lang)
        self.enemies_init = EnemiesInit(self.lang)

    def main(self):
        while True:
            self.ui.change_text(self.scene_manager.get_scene_data(self.scene_manager.DESCRIPTION).format(name=self.player.name))
            choices_ids = []
            for nr, choice in enumerate(self.scene_manager.get_scene_choices()):
                self.ui.change_text(f"{nr+1}. {choice[1]}")
                choices_ids.append(choice[0])
            choice_nr = self.ui.get_input(1, "") - 1
            self.ui.change_text(self.scene_manager.get_choices_data(choice_nr, "outcome_text"))
            if self.scene_manager.get_choices_data(choice_nr, self.scene_manager.IS_FIGHT):
                enemy_id = self.scene_manager.get_choices_data(choice_nr, self.scene_manager.ENEMY_ID)

                enemy = self.enemies_init.get_enemy(enemy_id)
                battle = BattleHandler(self.player, enemy, self.ui, self.lang)
                if battle.battle():
                    drop_data = self.enemies_init.get_enemy_drop(enemy_id)
                    for item in drop_data:
                        if random.random() < item[1]:
                            self.ui.change_text(GetTexts().load_texts("battle_enemy_item_drop").format(drop_name=[ItemsInit(self.lang).get_item(item[0])][0][0]))
                            self.player.inventory.add_to_inv(self.player.inventory.inventory, ItemsInit(self.lang).get_item(item[0]), 1)
                    self.scene_manager.set_current_scene(self.scene_manager.get_fight_result_data(choice_nr, True, self.scene_manager.GO_TO_SCENE))
                else:
                    self.scene_manager.set_current_scene(self.scene_manager.get_fight_result_data(choice_nr, False, self.scene_manager.GO_TO_SCENE))

                print("\n\n\n\nDEBUG\n\n\n\n")



if __name__ == "__main__":
    from ui_manager import UI
    from player import Player
    Game(UI("en"),Player(name="DEBUG", hp=50, armor=0,damage=5, player_class="", ui=UI("en"), lang="en"), "en").main()

