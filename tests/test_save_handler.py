import unittest
from unittest.mock import MagicMock
import json
import os
from hero_of_embers.save_handler import SaveGame, LoadGame


class TestSaveGame(unittest.TestCase):

    def setUp(self):
        self.player_mock = MagicMock()
        self.plot_manager_mock = MagicMock()
        self.player_mock.name = "Hero"
        self.player_mock.hp = 100
        self.player_mock.max_hp = 100
        self.player_mock.armor = 50
        self.player_mock.max_armor = 50
        self.player_mock.damage = 20
        self.player_mock.player_class = "Warrior"
        self.player_mock.inventory.inventory = ["sword", "shield"]
        self.player_mock.inventory.elixir_inventory = ["health potion"]
        self.player_mock.inventory.weapon = "sword"
        self.player_mock.inventory.armor = "shield"
        self.player_mock.level = 1
        self.player_mock.experience = 0
        self.plot_manager_mock.actual_scene = "scene_1"
        self.save_game = SaveGame(self.player_mock, self.plot_manager_mock)

    def test_save_game(self):
        self.save_game.save_game()
        self.assertTrue(os.path.exists('savegame.json'))
        with open('savegame.json', 'r') as file:
            data = json.load(file)
        self.assertEqual(data["player_name"], "Hero")
        self.assertEqual(data["player_hp"], 100)
        self.assertEqual(data["current_scene"], "scene_1")

    def test_load_game(self):
        save_data = {
            "player_name": "Hero",
            "player_hp": 100,
            "player_max_hp": 100,
            "player_armor": 50,
            "player_max_armor": 50,
            "player_damage": 20,
            "player_class": "Warrior",
            "player_inventory": ["sword", "shield"],
            "player_elixir_inventory": ["health potion"],
            "player_weapon_equiped": "sword",
            "player_armor_equiped": "shield",
            "player_level": 1,
            "player_experience": 0,
            "current_scene": "scene_1"
        }
        with open('savegame.json', 'w') as file:
            json.dump(save_data, file)
        load_game = LoadGame(self.player_mock, self.plot_manager_mock)
        load_game.load_data()
        self.assertEqual(self.player_mock.name, "Hero")
        self.assertEqual(self.player_mock.hp, 100)
        self.assertEqual(self.plot_manager_mock.actual_scene, "scene_1")

    def tearDown(self):
        if os.path.exists('savegame.json'):
            os.remove('savegame.json')


if __name__ == '__main__':
    unittest.main()
