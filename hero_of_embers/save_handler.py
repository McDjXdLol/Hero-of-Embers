import json
import os.path


class SaveGame:
    def __init__(self, player, plot_manager):
        # Player Data
        self.player_name = player.name
        self.player_hp = player.hp
        self.player_max_hp = player.max_hp
        self.player_armor = player.armor
        self.player_max_armor = player.max_armor
        self.player_damage = player.damage
        self.player_class = player.player_class
        self.player_inventory = player.inventory.inventory
        self.player_elixir_inventory = player.inventory.elixir_inventory
        self.player_weapon_equiped = player.inventory.weapon
        self.player_armor_equiped = player.inventory.armor
        self.player_level = player.level
        self.player_experience = player.experience

        # Plot Data
        self.current_scene = plot_manager.actual_scene

        # All data prepared to save
        self.data = {
            "player_name": self.player_name,
            "player_hp": self.player_hp,
            "player_max_hp": self.player_max_hp,
            "player_armor": self.player_armor,
            "player_max_armor": self.player_max_armor,
            "player_damage": self.player_damage,
            "player_class": self.player_class,
            "player_inventory": self.player_inventory,
            "player_elixir_inventory": self.player_elixir_inventory,
            "player_weapon_equiped": self.player_weapon_equiped,
            "player_armor_equiped": self.player_armor_equiped,
            "player_level": self.player_level,
            "player_experience": self.player_experience,
            "current_scene": self.current_scene
        }

    def save_game(self):
        with open('savegame.json', 'w') as file:
            json.dump(self.data, file)

class LoadGame:
    def __init__(self, player, plot_manager):
        self.player = player
        self.plot_manager = plot_manager

    @staticmethod
    def load_game():
        if os.path.exists("savegame.json"):
            with open('savegame.json', 'r') as file:
                return json.load(file)
        else:
            return None

    def load_data(self):
        print("Loading save file...")
        save_data = self.load_game()
        if save_data is not None:
            self.player.name = save_data["player_name"]
            self.player.hp = save_data['player_hp']
            self.player.max_hp = save_data['player_max_hp']
            self.player.armor = save_data['player_armor']
            self.player.max_armor = save_data['player_max_armor']
            self.player.damage = save_data['player_damage']
            self.player.player_class = save_data['player_class']
            self.player.inventory.inventory = save_data["player_inventory"]
            self.player.inventory.elixir_inventory = save_data["player_elixir_inventory"]
            self.player.inventory.weapon = save_data["player_weapon_equiped"]
            self.player.inventory.armor = save_data["player_armor_equiped"]
            self.player.level = save_data["player_level"]
            self.player.experience = save_data["player_experience"]
            self.plot_manager.actual_scene = save_data["current_scene"]
            print("Save file loaded successfully!")
        else:
            print("There is no save file to load!")
