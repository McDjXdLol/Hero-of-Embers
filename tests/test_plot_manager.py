import unittest
from unittest.mock import MagicMock
from hero_of_embers.plot_manager import PlotManager


class TestPlotManager(unittest.TestCase):

    def setUp(self):
        # Inicjalizacja plot_manager z mockiem
        self.player_mock = MagicMock()
        self.ui_mock = MagicMock()
        self.plot_manager = PlotManager(self.player_mock, self.ui_mock)

        # Zakładając, że wczytujesz plik scenes.json w PlotManager
        self.plot_manager.scenes_data = {
            "scene_1": {
                "scene_id": 1,
                "scene_name": "Ash and Soil",
                "description": "You are {name}, a poor farmer from a dying village. With nothing left, you've just arrived in the city of Eldoria, cold and hungry.",
                "1": {
                    "description": "Search the alleys for work or food.",
                    "next_scene": "scene_2",
                },
                "2": {
                    "description": "Go straight to the tavern district.",
                    "next_scene": "scene_3",
                }
            },
            "scene_2": {
                "scene_id": 2,
                "scene_name": "Shady Alley",
                "description": "You wander into a shady alley and are approached by a suspicious man.",
                "1": {
                    "description": "Fight the man.",
                    "next_scene": "scene_4",
                },
                "2": {
                    "description": "Run away.",
                    "next_scene": "scene_5",
                }
            },
            # Dodaj inne sceny, jeśli są
        }

    def test_get_description(self):
        expected_description = "You are {name}, a poor farmer from a dying village. With nothing left, you've just arrived in the city of Eldoria, cold and hungry."
        self.assertEqual(self.plot_manager.get_description(), expected_description)

    def test_get_options_names(self):
        expected_options = ["1", "2"]
        self.assertEqual(self.plot_manager.get_options_names(), expected_options)

    def test_set_next_scene(self):
        # Symulacja wyboru opcji przez gracza
        option_name = "1"  # Gracz wybiera opcję 1
        self.plot_manager.set_next_scene(option_name)

        # Sprawdzenie, czy kolejna scena została ustawiona poprawnie
        self.assertEqual(self.plot_manager.actual_scene, "scene_2")

    def test_show_all_options(self):
        options = self.plot_manager.show_all_options()
        self.assertIn("1. Search the alleys for work or food.", options)
        self.assertIn("2. Go straight to the tavern district.", options)


if __name__ == '__main__':
    unittest.main()
