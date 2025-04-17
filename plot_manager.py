import json
import os
import time

from enemy import Enemy
from library import Library
from battle_handler import BattleHandler as bH

class PlotManager:
    def __init__(self, player):
        self.player = player
        scene_file = open('scenes.json')
        scene_str = scene_file.read()
        self.scenes_data = json.loads(scene_str)
        first_scene = list(self.scenes_data.keys())[0]
        self.actual_scene = first_scene

    def open_scene(self, scene_name):
        return self.scenes_data[scene_name]

    def get_description(self):
        return self.scenes_data[self.actual_scene]['description']

    def get_options_names(self):
        options = []
        for nr, p in enumerate(self.scenes_data[self.actual_scene]):
            if nr > 1:
                options.append(p.lower())
        return options

    def get_option_description(self, option_name):
        return self.scenes_data[self.actual_scene][option_name]['description']

    def get_option_effect(self, option_name):
        return self.scenes_data[self.actual_scene][option_name]['effect']

    def get_option_requirements(self, option_name):
        return self.scenes_data[self.actual_scene][option_name]['requirements']

    def get_option_giving_item(self, option_name):
        return self.scenes_data[self.actual_scene][option_name]['giving_item']

    def get_option_next_scene(self, option_name):
        return self.scenes_data[self.actual_scene][option_name]['next_scene']

    def set_next_scene(self, option_name):
        self.actual_scene = self.scenes_data[self.actual_scene][option_name]['next_scene']

    def show_all_options(self):
        for option in self.get_options_names():
            print(f"{option}. {self.get_option_description(option)}")

    def show_description(self):
        print(f"{self.get_description().format(name=self.player.name)}")

    def is_fight(self, option_name):
        return self.scenes_data[self.actual_scene][option_name]['is_combat']

    def fight_who(self, option_name):
        return self.scenes_data[self.actual_scene][option_name]['enemy_name']

    def select_option(self):
        selected_option = None
        while True:
            try:
                self.show_description()
                print()
                self.show_all_options()
                print("\n")
                print("I. Show inventory")
                selected_option = input("Select Option: ")
                print("\n")
                if selected_option in self.get_options_names():
                    break
                elif selected_option.lower() == "i":
                    self.player.inventory.show_inv()
                else:
                    print("There is no such option!")
                    continue
            except ValueError:
                print("You entered it wrong!")
                continue
        if selected_option is None:
            print("There was an error!")
        else:
            os.system('cls')
            print(self.get_option_effect(selected_option))
            if self.is_fight(selected_option):
                time.sleep(1)
                for en in Library.ENEMIES:
                    if en[0] == self.fight_who(selected_option):
                        oponent = Enemy(self.fight_who(selected_option), en[1], en[2], en[3], en[4])
                        if bH(self.player,oponent).battle():
                            if self.get_option_next_scene(selected_option) != "END":
                                self.set_next_scene(selected_option)
                                self.select_option()
                            else:
                                return False
                        else:
                            print("You died!")
                            return False

            if self.get_option_next_scene(selected_option) != "END":
                self.set_next_scene(selected_option)
                self.select_option()
            else:
                return False
