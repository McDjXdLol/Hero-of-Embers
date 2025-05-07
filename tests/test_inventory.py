import unittest
from unittest.mock import MagicMock
from hero_of_embers.inventory import Inventory

class TestInventory(unittest.TestCase):
    def setUp(self):
        self.ui_mock = MagicMock()
        self.inventory = Inventory(self.ui_mock)

    def test_add_to_inv_new_item(self):
        item = ["Health Potion", 10]
        self.inventory.add_to_inv(item, self.inventory.inventory, 1)
        self.assertIn([item, 1], self.inventory.inventory)

    def test_add_to_inv_existing_item(self):
        item = ["Health Potion", 10]
        self.inventory.add_to_inv(item, self.inventory.inventory, 1)
        self.inventory.add_to_inv(item, self.inventory.inventory, 2)
        self.assertEqual(self.inventory.inventory[0][1], 3)

    def test_remove_from_inv(self):
        item = ["Health Potion", 10]
        self.inventory.add_to_inv(item, self.inventory.inventory, 3)
        self.inventory.remove_from_inv(item[0], self.inventory.inventory)
        self.assertEqual(self.inventory.inventory[0][1], 2)
        self.inventory.remove_from_inv(item[0], self.inventory.inventory)
        self.assertEqual(self.inventory.inventory[0][1], 1)
        self.inventory.remove_from_inv(item[0], self.inventory.inventory)
        self.assertNotIn([item, 1], self.inventory.inventory)

    def test_check_if_in_inv(self):
        item = ["Health Potion", 10]
        self.inventory.add_to_inv(item, self.inventory.inventory, 1)
        result = self.inventory.check_if_in_inv(item[0], self.inventory.inventory)
        self.assertTrue(result)
        result = self.inventory.check_if_in_inv("Mana Potion", self.inventory.inventory)
        self.assertFalse(result)

    def test_show_inv(self):
        item = ["Health Potion", 10]
        self.inventory.add_to_inv(item, self.inventory.inventory, 2)
        self.inventory.show_inv()
        self.ui_mock.change_text.assert_any_call("Weapons: ")
        self.ui_mock.change_text.assert_any_call(f"Health Potion x2")

    def test_equip_weapon(self):
        weapon = "Iron Sword"
        self.inventory.add_to_inv([weapon, 40], self.inventory.inventory, 1)
        old_damage, new_damage = self.inventory.equip_weapon(weapon)
        self.assertEqual(old_damage, 0)
        self.assertEqual(new_damage, 40)
        self.assertIn(weapon, self.inventory.weapon)

    def test_equip_armor(self):
        armor = "Knight Armor"
        self.inventory.add_to_inv([armor, 40], self.inventory.inventory, 1)
        old_armor_value, new_armor_value = self.inventory.equip_armor(armor)
        self.assertEqual(old_armor_value, 0)
        self.assertEqual(new_armor_value, 40)
        self.assertIn(armor, self.inventory.armor)

    def test_equip_weapon_removes_old(self):
        old_weapon = "Wooden Stick"
        new_weapon = "Gold Sword"
        self.inventory.add_to_inv([old_weapon, 10], self.inventory.inventory, 1)
        self.inventory.add_to_inv([new_weapon, 50], self.inventory.inventory, 1)
        self.inventory.equip_weapon(old_weapon)
        self.inventory.equip_weapon(new_weapon)
        self.assertNotIn(old_weapon, self.inventory.weapon)
        self.assertIn(new_weapon, self.inventory.weapon)

    def test_show_inv_elixirs(self):
        elixir = ["Small Heart Elixir", 10]
        self.inventory.elixir_inventory.append(elixir)
        self.inventory.show_inv_elixirs()
        self.ui_mock.change_text.assert_any_call("Small Heart Elixir x10")

if __name__ == "__main__":
    unittest.main()
