import json
import os
import random
import sys
import time

from hero_of_embers.enemy import Enemy
from hero_of_embers.library import Library
from hero_of_embers.battle_handler import BattleHandler as bH
from hero_of_embers.save_handler import SaveGame


class PlotManager:
    def __init__(self, player, ui):
        """
        Class that is being used to control scenes.json/plot file.
        :param player: player class object
        :param ui: ui class object
        :type player: hero_of_embers.player.Player
        :type ui: hero_of_embers.ui_manager.UI
        """
        self.ui = ui
        self.player = player
        scene_file = open('scenes.json')
        scene_str = scene_file.read()
        self.scenes_data = json.loads(scene_str)
        first_scene = list(self.scenes_data.keys())[0]
        self.current_scene = first_scene

    def open_scene(self, scene_name):
        """
        Function that returns the scene
        :param scene_name: scene name
        :type scene_name: str
        """
        return self.scenes_data[scene_name]

    def get_description(self):
        """
        Function that returns description of current scene
        """
        return self.scenes_data[self.current_scene]['description']

    def get_options_names(self):
        """
        Function that returns names of the options
        """
        options = []
        for key in self.scenes_data[self.current_scene]:
            if key.isdigit():
                options.append(key)
        return options

    def get_option_description(self, option_name):
        """
        Function that returns option description
        :param option_name: option name
        :type option_name: str
        """
        option_name = str(option_name)
        if option_name in self.scenes_data[self.current_scene]:
            return self.scenes_data[self.current_scene][option_name]['description']
        else:
            return f"Option {option_name} not found!"

    def get_option_effect(self, option_name):
        """
        Function that returns the effect of selected option
        :param option_name: option name
        :type option_name: str
        """
        return self.scenes_data[self.current_scene][option_name]['effect']

    def get_option_requirements(self, option_name):
        """
        Function that returns requirements for selected option
        :param option_name: option name
        :type option_name: str
        """
        return self.scenes_data[self.current_scene][option_name]['requirements']

    def get_option_giving_item(self, option_name):
        """
        Function that returns item that the selected option give
        :param option_name: option name
        :type option_name: str
        """
        return self.scenes_data[self.current_scene][option_name]['giving_item']

    def get_option_next_scene(self, option_name):
        """
        Function that returns next scene after selected option
        :param option_name: option name
        :type option_name: str
        """
        return self.scenes_data[self.current_scene][option_name]['next_scene']

    def set_next_scene(self, option_name):
        """
        Function that sets the next scene as new current scene
        :param option_name: option name
        :type option_name: str
        """
        self.current_scene = self.scenes_data[self.current_scene][option_name]['next_scene']

    def get_drop_information(self, option_name):
        """
        Function that return information if the selected option give the drop
        :param option_name: option name
        :type option_name: str
        """
        return self.scenes_data[self.current_scene][option_name]['drop']

    def get_scene_id(self):
        """
        Function that returns the scene_id of current scene
        """
        return self.scenes_data[self.current_scene]['scene_id']

    def show_all_options(self):
        """
        Function that returns all the options
        """
        options = []
        for option in self.get_options_names():
            options.append(f"{option}. {self.get_option_description(option)}")
        return options

    def show_description(self):
        """
        Function that returns description of current scene
        """
        return f"{self.get_description().format(name=self.player.name)}"

    def is_fight(self, option_name):
        """
        Function that returns if in selected options there is a fight
        :param option_name: option name
        :type option_name: str
        """
        return self.scenes_data[self.current_scene][option_name]['is_combat']

    def fight_who(self, option_name):
        """
        Function that return with whom the fight is going to be
        :param option_name: option name
        :type option_name: str
        """
        return self.scenes_data[self.current_scene][option_name]['enemy_name']

    def random_drop(self, scene_id):
        """
        Function that gives player random drop according to scene_id/ how far in plot player is
        :param scene_id: scene id
        :type scene_id: int
        """
        if scene_id <= 10:
            dropping_item = Library.HEAL_ITEMS[random.randint(0, len(Library.HEAL_ITEMS) - 1)]
            amount = random.randint(1, 3)
            self.player.inventory.add_to_inv(dropping_item[0], self.player.inventory.elixir_inventory, amount=amount)
        elif 11 <= scene_id <= 25:
            libraries = [Library.HEAL_ITEMS, Library.WEAPONS, Library.ARMORS]
            rolled_library = libraries[random.randint(0, 2)]
            dropping_item = rolled_library[random.randint(0, len(rolled_library) - 1)]
            match rolled_library:
                case Library.HEAL_ITEMS:
                    self.player.inventory.add_to_inv(dropping_item[0], self.player.inventory.elixir_inventory, amount=1)
                case _:
                    self.player.inventory.add_to_inv(dropping_item[0], self.player.inventory.inventory, amount=1)

    def select_option(self):
        """
        Function that is used to control main loop of the game
        """
        selected_option = None
        while True:
            try:
                self.ui.change_text(self.show_description())
                self.ui.change_text(self.show_all_options())
                self.ui.change_text("\n")
                self.ui.change_text("I. Show inventory")
                self.ui.change_text("S. Save & Exit")
                self.ui.change_text("E. Exit without Saving")
                selected_option = self.ui.get_input("str","Select Option: ")
                self.ui.change_text("\n")
                if selected_option in self.get_options_names():
                    break
                elif selected_option.lower() == "i":
                    self.player.inventory.show_inv()
                elif selected_option.lower() == "s":
                    self.ui.change_text("Saving & Exiting...")
                    SaveGame(self.player, self).save_game()
                    time.sleep(1)
                    sys.exit()
                elif selected_option.lower() == "e":
                    self.ui.change_text("Exiting...")
                    time.sleep(1)
                    sys.exit()
                else:
                    self.ui.change_text("There is no such option!")
                    continue
            except ValueError:
                self.ui.change_text("You entered it wrong!")
                continue
        if selected_option is None:
            self.ui.change_text("There was an error!")
            return False
        else:
            os.system('cls')
            self.ui.change_text(self.get_option_effect(selected_option))
            if self.get_drop_information(selected_option):
                self.random_drop(self.get_scene_id())
            if self.is_fight(selected_option):
                time.sleep(1)
                for en in Library.ENEMIES:
                    if en[0] == self.fight_who(selected_option):
                        oponent = Enemy(self.fight_who(selected_option), en[1], en[2], en[3], en[4])
                        if bH(self.player, oponent, self.ui).battle():
                            if self.get_option_next_scene(selected_option) != "END":
                                self.set_next_scene(selected_option)
                                self.select_option()
                            else:
                                return False
                        else:
                            self.ui.change_text("You died!")
                            return False

            if self.get_option_next_scene(selected_option) != "END":
                self.set_next_scene(selected_option)
                self.select_option()
                return True
            else:
                return False
