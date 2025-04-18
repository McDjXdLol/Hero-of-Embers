import unittest
from hero_of_embers.enemy import Enemy

class TestEnemy(unittest.TestCase):

    def setUp(self):
        self.enemy = Enemy(name="Goblin", hp=50, armor=30, damage=10, experience=15)

    def test_initial_enemy_stats(self):
        self.assertEqual(self.enemy.name, "Goblin")
        self.assertEqual(self.enemy.hp, 50)
        self.assertEqual(self.enemy.max_hp, 50)
        self.assertEqual(self.enemy.armor, 30)
        self.assertEqual(self.enemy.damage, 10)
        self.assertEqual(self.enemy.experience_drop, 15)
        self.assertFalse(self.enemy.dead)

    def test_deal_damage_with_armor(self):
        self.enemy.deal_damage(15)
        self.assertEqual(self.enemy.armor, 15)
        self.assertEqual(self.enemy.hp, 50)

    def test_deal_damage_without_armor(self):
        self.enemy.deal_damage(40)
        self.assertEqual(self.enemy.armor, 0)
        self.assertEqual(self.enemy.hp, 40)

    def test_deal_damage_and_kill(self):
        result = self.enemy.deal_damage(100)
        self.assertTrue(self.enemy.dead)
        self.assertEqual(self.enemy.hp, 0)
        self.assertEqual(self.enemy.armor, 0)
        self.assertTrue(result)

    def test_heal_hp(self):
        self.enemy.hp = 40
        self.enemy.heal_hp(10)
        self.assertEqual(self.enemy.hp, 50)

    def test_heal_hp_over_max(self):
        self.enemy.heal_hp(100)
        self.assertEqual(self.enemy.hp, 50)

if __name__ == "__main__":
    unittest.main()
