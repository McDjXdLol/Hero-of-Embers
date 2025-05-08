from typing import List, Union

from enemy import Enemy
from scene_manager import SceneManager

class EnemiesInit:
    def __init__(self, lang):
        self.scene_manager = SceneManager(lang)

    def get_enemy_data(self, enemy_id) -> List[Union[str, int]]:
        """
        Function that returns data about enemy in list
        Returns: [name, description, hp, max_hp, armor, dmg, xp_drop, item_id, drop_chance]
        """
        name = self.scene_manager.get_enemy_data(enemy_id, self.scene_manager.NAME)
        description = self.scene_manager.get_enemy_data(enemy_id, self.scene_manager.DESCRIPTION)
        hp = self.scene_manager.get_enemy_data(enemy_id, self.scene_manager.HEALTH)
        armor = self.scene_manager.get_enemy_data(enemy_id, self.scene_manager.ARMOR)
        dmg = self.scene_manager.get_enemy_data(enemy_id, self.scene_manager.ATTACK)
        xp_drop = self.scene_manager.get_enemy_data(enemy_id, self.scene_manager.XP_DROP)
        loot = self.scene_manager.get_enemy_data(enemy_id, self.scene_manager.LOOT)
        item_id = loot[0]
        drop_chance = loot[1]

        data = {
            "name": name,
            "description": description,
            "hp": hp,
            "armor": armor,
            "dmg": dmg,
            "xp_drop": xp_drop,
            "item_id": item_id,
            "drop_chance": drop_chance
        }
        return data

    def get_enemy(self, enemy_id):
        data = self.get_enemy_data(enemy_id)
        return Enemy(data["name"], data["hp"], data["armor"], data["dmg"], data["xp_drop"])

    def get_enemy_drop(self, enemy_id):
        data = self.get_enemy_data(enemy_id)
        drop = {
            "item_id": data["item_id"],
            "drop_chance": data["drop_chance"]
        }
        return drop