from hero_of_embers.data_manager import SceneManager

class ItemsInit:
    """
    Initializes and manages item data using the SceneManager.

    This class provides methods to retrieve and organize item information,
    specifically for general items and healing items, based on data
    managed by the SceneManager.

    Attributes
    ----------
    scene_manager : SceneManager
        An instance of the SceneManager class, used to access item data.
    """
    def __init__(self, lang):
        """
        Initializes the ItemsInit class with a SceneManager instance.

        Parameters
        ----------
        lang : str
            The language code (e.g., 'en', 'fr') to be used by the SceneManager.
        """
        self.scene_manager = SceneManager(lang)

    def get_items(self):
        """
        Retrieves a list of all general items with their details.

        This method fetches item data from the SceneManager for all item IDs
        and organizes it into a list of lists, where each inner list
        represents an item and its attributes.  If the item is a weapon,
        its damage is included.

        Returns
        -------
        list of list
            A list containing lists of item details. Each inner list contains:
            - item_name : str
                The name of the item.
            - item_description : str
                The description of the item.
            - item_type : str
                The type of the item (e.g., "weapon", "other").
            - item_damage : int, optional
                The damage value of the item, if the item_type is "weapon".
            - item_value : int
                The value of the item.
        """
        items = []
        for item_id in self.scene_manager.get_all_items_ids():
            item_name = self.scene_manager.get_item_data(item_id, self.scene_manager.NAME)
            item_description = self.scene_manager.get_item_data(item_id, self.scene_manager.DESCRIPTION)
            item_type = self.scene_manager.get_item_data(item_id, self.scene_manager.TYPE)
            item_value = self.scene_manager.get_item_data(item_id, self.scene_manager.VALUE)
            if item_type == "weapon":
                item_damage = self.scene_manager.get_item_data(item_id, self.scene_manager.ATTACK)
                items.append([item_name, item_description, item_type, item_damage, item_value])
            else:
                items.append([item_name, item_description, item_type, item_value])

        return items

    def get_item(self, item_id):
        for itemm_id in self.scene_manager.get_all_items_ids():
            if itemm_id == item_id:
                item_name = self.scene_manager.get_item_data(item_id, self.scene_manager.NAME)
                item_description = self.scene_manager.get_item_data(item_id, self.scene_manager.DESCRIPTION)
                item_type = self.scene_manager.get_item_data(item_id, self.scene_manager.TYPE)
                item_value = self.scene_manager.get_item_data(item_id, self.scene_manager.VALUE)
                if item_type == "weapon":
                    item_damage = self.scene_manager.get_item_data(item_id, self.scene_manager.DAMAGE)
                    return [item_name, item_description, item_type, item_damage, item_value]
                if item_type == "armor":
                    item_armor = self.scene_manager.get_item_data(item_id, self.scene_manager.ARMOR)
                    return [item_name, item_description, item_type, item_armor, item_value]
                if item_type == "elixir":
                    heal_amount = self.scene_manager.get_item_data(item_id, self.scene_manager.HEAL_AMOUNT)
                    return [item_name, item_description, item_type, heal_amount, item_value]
                else:
                    return [item_name, item_description, item_type, item_value]
        return []

    def get_heal_items(self):
        """
        Retrieves a list of all healing items with their details.

        This method fetches healing item data from the SceneManager and
        organizes it into a list of lists, where each inner list
        represents a healing item and its attributes.

        Returns
        -------
        list of list
            A list containing lists of healing item details.  Each inner list
            contains:
            - item_name : str
                The name of the healing item.
            - item_description : str
                The description of the healing item.
            - item_heal_amount : int
                The amount of healing the item provides.
            - item_value : int
                The value of the healing item.
        """
        heal_items = []
        for item_id in self.scene_manager.get_all_heal_items_ids():
            item_name = self.scene_manager.get_heal_item_data(item_id, self.scene_manager.NAME)
            item_description = self.scene_manager.get_heal_item_data(item_id, self.scene_manager.DESCRIPTION)
            item_heal_amount = self.scene_manager.get_heal_item_data(item_id, self.scene_manager.HEAL_AMOUNT)
            item_value = self.scene_manager.get_heal_item_data(item_id, self.scene_manager.VALUE)

            heal_items.append([item_name, item_description, item_heal_amount, item_value])

        return heal_items

    def get_fight_item_by_choice_id(self, choice_id, won:bool):
        item_id = self.scene_manager.get_fight_result_data(choice_id, won, self.scene_manager.GIVE_ITEM)
        item = self.get_item(item_id)
        return item