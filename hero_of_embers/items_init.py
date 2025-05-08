from scene_manager import SceneManager

class ItemsInit:
    def __init__(self, lang):
        self.scene_manager = SceneManager(lang)

    def get_items(self):
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

    def get_heal_items(self):
        heal_items = []
        for item_id in self.scene_manager.get_all_heal_items_ids():
            item_name = self.scene_manager.get_heal_item_data(item_id, self.scene_manager.NAME)
            item_description = self.scene_manager.get_heal_item_data(item_id, self.scene_manager.DESCRIPTION)
            item_heal_amount = self.scene_manager.get_heal_item_data(item_id, self.scene_manager.HEAL_AMOUNT)
            item_value = self.scene_manager.get_heal_item_data(item_id, self.scene_manager.VALUE)

            heal_items.append([item_name, item_description, item_heal_amount, item_value])

        return heal_items
