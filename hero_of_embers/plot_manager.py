import json
import os
import random
import sys
import time

from hero_of_embers.battle_handler import BattleHandler as bH
from hero_of_embers.enemy import Enemy
from hero_of_embers.library import Library
from hero_of_embers.save_handler import SaveGame


class PlotManager:
    def __init__(self, player, ui):
        """
        Manages the game plot and scenes loaded from the JSON file.

        Parameters
        ----------
        player : hero_of_embers.player.Player
            The player object.
        ui : hero_of_embers.ui_manager.UI
            The user interface manager.
        """
        self.ui = ui
        self.player = player
        with open('scenes.json', 'r', encoding='utf-8') as scene_file:
            self.scenes_data = json.load(scene_file)
        self.current_scene = list(self.scenes_data.keys())[0]
        self.was_in_shop = False

    def open_scene(self, scene_name):
        """
        Returns data for a specific scene.

        Parameters
        ----------
        scene_name : str
            The name of the scene.

        Returns
        -------
        dict
            The scene data.
        """
        return self.scenes_data[scene_name]

    def get_description(self):
        """
        Returns the description of the current scene.

        Returns
        -------
        str
            Scene description.
        """
        return self.scenes_data[self.current_scene]['description']

    def get_options_names(self):
        """
        Returns available option keys for the current scene.

        Returns
        -------
        list of str
            List of option keys.
        """
        return [key for key in self.scenes_data[self.current_scene] if key.isdigit()]

    def get_option_description(self, option_name):
        """
        Returns the description of a specific option.

        Parameters
        ----------
        option_name : str
            The option key.

        Returns
        -------
        str
            Option description or error message.
        """
        option_name = str(option_name)
        return self.scenes_data[self.current_scene].get(option_name, {}).get('description',
                                                                             f"Option {option_name} not found!")

    def get_option_effect(self, option_name):
        """
        Returns the effect of a selected option.

        Parameters
        ----------
        option_name : str
            The option key.

        Returns
        -------
        str
            Description of the effect.
        """
        return self.scenes_data[self.current_scene][option_name]['effect']

    def get_option_requirements(self, option_name):
        """
        Returns requirements for a selected option.

        Parameters
        ----------
        option_name : str
            The option key.

        Returns
        -------
        list
            List of requirements.
        """
        return self.scenes_data[self.current_scene][option_name]['requirements']

    def get_option_giving_item(self, option_name):
        """
        Returns the item granted by a selected option.

        Parameters
        ----------
        option_name : str
            The option key.

        Returns
        -------
        str
            The item name.
        """
        return self.scenes_data[self.current_scene][option_name]['giving_item']

    def get_option_next_scene(self, option_name):
        """
        Returns the next scene following a selected option.

        Parameters
        ----------
        option_name : str
            The option key.

        Returns
        -------
        str
            The name of the next scene.
        """
        return self.scenes_data[self.current_scene][option_name]['next_scene']

    def set_next_scene(self, option_name):
        """
        Sets the current scene to the next scene based on the selected option.

        Parameters
        ----------
        option_name : str
            The option key.
        """
        self.current_scene = self.get_option_next_scene(option_name)

    def get_drop_information(self, option_name):
        """
        Checks if the selected option grants a drop.

        Parameters
        ----------
        option_name : str
            The option key.

        Returns
        -------
        bool
            True if drop is given, else False.
        """
        return self.scenes_data[self.current_scene][option_name]['drop']

    def get_scene_id(self):
        """
        Returns the current scene's ID.

        Returns
        -------
        int
            The scene ID.
        """
        return self.scenes_data[self.current_scene]['scene_id']

    def show_all_options(self):
        """
        Returns all options available in the current scene.

        Returns
        -------
        list of str
            Descriptions of each option.
        """
        return [f"{opt}. {self.get_option_description(opt)}" for opt in self.get_options_names()]

    def show_description(self):
        """
        Returns formatted description of the current scene.

        Returns
        -------
        str
            Scene description with player name injected.
        """
        return self.get_description().format(name=self.player.name)

    def is_fight(self, option_name):
        """
        Checks if a fight will occur for the selected option.

        Parameters
        ----------
        option_name : str
            The option key.

        Returns
        -------
        bool
            True if a fight occurs.
        """
        return self.scenes_data[self.current_scene][option_name]['is_combat']

    def fight_who(self, option_name):
        """
        Returns the enemy's name for a fight.

        Parameters
        ----------
        option_name : str
            The option key.

        Returns
        -------
        str
            Name of the enemy.
        """
        return self.scenes_data[self.current_scene][option_name]['enemy_name']

    def random_drop(self, scene_id):
        """
        Grants a random drop to the player based on story progress.

        Parameters
        ----------
        scene_id : int
            ID of the current scene.
        """
        if scene_id <= 10:
            item = random.choice(Library.HEAL_ITEMS)
            self.player.inventory.add_to_inv(item[0], self.player.inventory.elixir_inventory,
                                             amount=random.randint(1, 3))
        elif 11 <= scene_id <= 25:
            lib = random.choice([Library.HEAL_ITEMS, Library.WEAPONS, Library.ARMORS])
            item = random.choice(lib)
            if lib == Library.HEAL_ITEMS:
                self.player.inventory.add_to_inv(item[0], self.player.inventory.elixir_inventory)
            else:
                self.player.inventory.add_to_inv(item[0], self.player.inventory.inventory)

    def buy(self, item):
        self.ui.change_text(f"You bought: {item[0][3]}")
        self.player.inventory.take_from_wallet(item[0][3])
        self.player.inventory.add_to_inv(item[0], self.player.inventory.inventory, 1)

    def trade(self):
        self.ui.change_text("You're my last client. When you leave, I’ll disappear. At least for now")
        while True:
            try:
                # Print random weapon
                random_weapon = random.choices(Library.WEAPONS, weights=[w[3] for w in Library.WEAPONS])
                self.ui.change_text(f"1. {random_weapon[0][0]} x{random_weapon[0][3]}Ɇ")
                # Print random armor
                random_armor = random.choices(Library.ARMORS, weights=[a[3] for a in Library.ARMORS])
                self.ui.change_text(f"2. {random_armor[0][0]} x{random_armor[0][3]}Ɇ")
                # Print random heal item
                random_heal_item = random.choices(Library.HEAL_ITEMS, weights=[h[3] for h in Library.HEAL_ITEMS])
                self.ui.change_text(f"3. {random_heal_item[0][0]} x{random_heal_item[0][3]}Ɇ")
                self.ui.change_text("4. Exit shop")
                ina = int(input())
                if ina > 0:
                    match ina:
                        case 1:
                            if self.player.inventory.check_if_can_buy(random_weapon[0][3]):
                                self.buy(random_weapon)
                                return True
                            else:
                                self.ui.change_text("You don't have enough dragon coins!")
                        case 2:
                            if self.player.inventory.check_if_can_buy(random_armor[0][3]):
                                self.buy(random_armor)
                                return True
                            else:
                                self.ui.change_text("You don't have enough dragon coins!")
                        case 3:
                            if self.player.inventory.check_if_can_buy(random_heal_item[0][3]):
                                self.buy(random_heal_item)
                                return True
                            else:
                                self.ui.change_text("You don't have enough dragon coins!")
                        case 4:
                            self.ui.change_text("Go now, before the Hollow Hand returns.")
                        case _:
                            self.ui.change_text("Are you trying to steal something! GO AWAY!")
                if ina < 5:
                    return True
                else:
                    self.ui.change_text("There is no such option! Try again!")
            except ValueError:
                self.ui.change_text("You have to enter the number!")

    def select_option(self):
        """
        Main control loop for user input and scene handling.

        Returns
        -------
        bool
            False if the game ends or player dies, otherwise True.
        """
        while True:
            try:
                self.ui.change_text(self.show_description())
                self.ui.change_text(self.show_all_options())
                if not self.was_in_shop:
                    self.ui.change_text(
                        ["T. Go trade", "I. Show inventory", "S. Save & Exit", "E. Exit without Saving"])
                else:
                    self.ui.change_text(["I. Show inventory", "S. Save & Exit", "E. Exit without Saving"])
                selected_option = self.ui.get_input("str", "Select Option: ").strip()
                self.ui.change_text("\n")
                if selected_option in self.get_options_names():
                    break
                elif selected_option.lower() == "t":
                    self.was_in_shop = self.trade()
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
            except ValueError:
                self.ui.change_text("You entered it wrong!")

        os.system('cls' if os.name == 'nt' else 'clear')
        self.ui.change_text(self.get_option_effect(selected_option))

        if self.get_drop_information(selected_option):
            self.random_drop(self.get_scene_id())

        if self.is_fight(selected_option):
            time.sleep(1)
            for en in Library.ENEMIES:
                if en[0] == self.fight_who(selected_option):
                    opponent = Enemy(self.fight_who(selected_option), *en[1:])
                    if bH(self.player, opponent, self.ui).battle():
                        if self.get_option_next_scene(selected_option) != "END":
                            self.set_next_scene(selected_option)
                            return self.select_option()
                        else:
                            return False
                    else:
                        self.ui.change_text("You died!")
                        return False

        if self.get_option_next_scene(selected_option) != "END":
            self.set_next_scene(selected_option)
            return self.select_option()
        return False
