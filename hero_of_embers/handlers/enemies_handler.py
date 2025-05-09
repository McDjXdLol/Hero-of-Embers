from typing import List, Union

from hero_of_embers.enemy import Enemy
from hero_of_embers.scene_manager import SceneManager

class EnemiesInit:
    """
    Initializes and manages enemy data using the SceneManager.

    This class provides methods to retrieve and process enemy information,
    including enemy attributes and drop data, based on data managed by
    the SceneManager.  It also creates Enemy objects.

    Attributes
    ----------
    scene_manager : SceneManager
        An instance of the SceneManager class, used to access enemy data.
    """
    def __init__(self, lang):
        """
        Initializes the EnemiesInit class with a SceneManager instance.

        Parameters
        ----------
        lang : str
            The language code (e.g., 'en', 'pl') to be used by the SceneManager.
        """
        self.scene_manager = SceneManager(lang)

    def get_enemy_data(self, enemy_id) -> List[Union[str, int]]:
        """
        Retrieves data about a specific enemy.

        This method fetches enemy data from the SceneManager using the enemy's ID
        and organizes it into a dictionary.

        Parameters
        ----------
        enemy_id : int
            The unique identifier of the enemy.

        Returns
        -------
        dict
            A dictionary containing the enemy's data, with the following keys and values:
            - "name" : str
                The name of the enemy.
            - "description" : str
                The description of the enemy.
            - "hp" : int
                The health points of the enemy.
            - "armor" : int
                The armor value of the enemy.
            - "dmg" : int
                The damage the enemy can inflict.
            - "xp_drop" : int
                The experience points dropped by the enemy upon defeat.
            - "item_id" : int
                The ID of the item that the enemy may drop.
            - "drop_chance" : float
                The probability (between 0 and 1) that the enemy will drop the item.
        """
        name = self.scene_manager.get_enemy_data(enemy_id, self.scene_manager.NAME)
        description = self.scene_manager.get_enemy_data(enemy_id, self.scene_manager.DESCRIPTION)
        hp = self.scene_manager.get_enemy_data(enemy_id, self.scene_manager.HEALTH)
        armor = self.scene_manager.get_enemy_data(enemy_id, self.scene_manager.ARMOR)
        dmg = self.scene_manager.get_enemy_data(enemy_id, self.scene_manager.ATTACK)
        xp_drop = self.scene_manager.get_enemy_data(enemy_id, self.scene_manager.XP_DROP)
        loot = self.scene_manager.get_enemy_data(enemy_id, self.scene_manager.LOOT)
        drop = []
        for item in loot:
            drop.append([item[0], item[1]])

        data = {
            "name": name,
            "description": description,
            "hp": hp,
            "armor": armor,
            "dmg": dmg,
            "xp_drop": xp_drop,
            "drop": drop
        }
        return data

    def get_enemy(self, enemy_id):
        """
        Creates an Enemy object with data retrieved from get_enemy_data.

        Parameters
        ----------
        enemy_id : int
            The unique identifier of the enemy.

        Returns
        -------
        Enemy
            An Enemy object initialized with the enemy's name, health points,
            armor, damage, and experience points.
        """
        data = self.get_enemy_data(enemy_id)
        return Enemy(data["name"], data["hp"], data["armor"], data["dmg"], data["xp_drop"])

    def get_enemy_drop(self, enemy_id):
        """
        Retrieves the drop data for a specific enemy.

        This method fetches the item ID and drop chance for a given enemy from
        the data retrieved by get_enemy_data.

        Parameters
        ----------
        enemy_id : int
            The unique identifier of the enemy.

        Returns
        -------
        dict
            A dictionary containing the enemy's drop data, with the following keys and values:
            - "item_id" : int
                The ID of the item that the enemy may drop.
            - "drop_chance" : float
                The probability that the enemy will drop the item.
        """
        data = self.get_enemy_data(enemy_id)
        return data["drop"]
