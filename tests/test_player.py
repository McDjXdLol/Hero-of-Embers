import unittest
from unittest.mock import MagicMock, patch
from hero_of_embers.player import Player
from hero_of_embers.ui_manager import UI


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.ui = UI("en")
        self.ui.change_text = MagicMock()
        self.player = Player("Aldric", 100, "Warrior", 50, 20, self.ui)

    def test_deal_damage_no_hp_loss(self):
        self.player.deal_damage(30)
        self.assertEqual(self.player.hp, 100)
        self.assertEqual(self.player.armor, 20)
        self.assertFalse(self.player.dead)

    def test_deal_damage_partial_hp_loss(self):
        self.player.deal_damage(70)
        self.assertEqual(self.player.hp, 80)
        self.assertEqual(self.player.armor, 0)
        self.assertFalse(self.player.dead)

    def test_deal_damage_kill(self):
        self.player.deal_damage(200)
        self.assertEqual(self.player.hp, 0)
        self.assertEqual(self.player.armor, 0)
        self.assertTrue(self.player.dead)

    def test_heal_hp_partial(self):
        self.player.hp = 50
        self.player.heal_hp(30)
        self.assertEqual(self.player.hp, 80)

    def test_heal_hp_over_max(self):
        self.player.hp = 90
        self.player.heal_hp(30)
        self.assertEqual(self.player.hp, 100)

    def test_give_experience_and_level_up(self):
        self.player.select_boost = MagicMock()
        self.player.level_handler.give_experience(60)
        self.assertEqual(self.player.level, 2)
        self.assertTrue(self.player.experience < 60)
        self.player.select_boost.assert_called_once()

    def test_max_level_reached(self):
        total_xp = sum(self.player.level_handler.experience_to_next_level[1:]) + sum(self.player.level_handler.experience_to_legendary_level)

        with patch("builtins.input", return_value="1"):
            self.player.level_handler.give_experience(total_xp)


        self.assertEqual(self.player.level, "MAX")
        self.assertEqual(self.player.experience, "MAX")

if __name__ == '__main__':
    unittest.main()
