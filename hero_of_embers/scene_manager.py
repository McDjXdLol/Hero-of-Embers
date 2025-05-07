import json
import os


def check_for_file(lang="en"):
    curr_dir = os.path.dirname(__file__)
    data_dir = os.path.join(curr_dir, "data")
    lang_dir = os.path.join(data_dir, "scenes")
    lang_file = os.path.join(lang_dir, f"scenes_{lang}.json")
    return lang_file

class SceneManager:
    def __init__(self, player, ui, lang="en"):

        self.lang = lang
        self.player = player
        self.ui = ui
        self.lang_file = check_for_file(lang)
        try:
            with open(self.lang_file, 'r', encoding='utf-8') as scene_file:
                self.scenes_data = json.load(scene_file)
        except FileNotFoundError:
            print(f"Error: Languages file not found: {self.lang_file}")
            self.scenes_data = {}
        except json.JSONDecodeError:
            print(f"Error: Failed to decode JSON: {self.lang_file}")

        self.current_scene = self.get_starting_scene()

        # Constant Variables
        # -----------------------------------------------------------------
        self.GAME_TITLE = "game_title"
        self.STARTING_SCENE_ID = "starting_scene_id"
        self.NAME = "name"
        self.DESCRIPTION = "description"
        self.TYPE = "type"
        self.VALUE = "value"
        self.HEALTH = "health"
        self.ATTACK = "attack"
        self.LOOT = "loot"
        self.IS_LAST_SCENE = "is_last_scene"
        self.REQUIREMENTS = "requirements"
        self.REQUIREMENTS_FLAGS = "requirements_flags"
        self.REQUIREMENTS_ITEMS = "requirements_items"
        self.ON_ENTER_EFFECTS = "on_enter_effects"
        self.ON_ENTER_EFFECTS_FLAGS = "on_enter_effects_flags"
        self.ON_ENTER_EFFECTS_GIVE_ITEM = "on_enter_effects_give_item"
        self.FLAGS = "flags"
        self.GIVE_ITEM = "give_item"
        self.GO_TO_SCENE = "go_to_scene"
        self.IS_FIGHT = "is_fight"
        self.ENEMY_ID = "enemy_id"
        self.TEXT = "text"
        self.IS_TERMINAL = "is_terminal"
        self.STATS = "stats"
        self.INVENTORY = "inventory"
        self.GOLD = "gold"
        self.PLAYER_DEFAULTS = "player_defaults"
        self.ENEMIES = "enemies"
        self.ITEMS = "items"
        self.ITEM_ID = "item_id"
        self.CHANCE = "chance"
        self.SCENES = "scenes"
        self.FLAG_ID = "flag_id"
        self.HAVE_ITEM = "have_item"
        self.FLAG_IS_SET = "flag_is_set"
        self.CHOICES = "choices"
        self.ID = "id"
        self.EFFECTS = "effects"
        self.SET_FLAG = "set_flag"
        self.SCENE_ID = "scene_id"
        self.START_COMBAT = "start_combat"
        self.ON_WIN = "on_win"
        self.ON_LOSE = "on_lose"
        # -----------------------------------------------------------------

    def get_game_title(self):
        return self.scenes_data.get(self.GAME_TITLE)

    def get_starting_scene(self):
        return self.scenes_data.get(self.STARTING_SCENE_ID)

    def get_starting_inv(self):
        return self.scenes_data.get(self.PLAYER_DEFAULTS, {}).get(self.INVENTORY)

    def get_starting_flags(self):
        return self.scenes_data.get(self.PLAYER_DEFAULTS, {}).get(self.FLAGS)

    def get_starting_hp(self):
        return self.scenes_data.get(self.PLAYER_DEFAULTS, {}).get(self.STATS, {}).get(self.HEALTH)

    def get_starting_cash(self):
        return self.scenes_data.get(self.PLAYER_DEFAULTS, {}).get(self.STATS, {}).get(self.GOLD)

    def get_item_data(self, item_id, type_of_data):
        item = self.scenes_data.get(self.ITEMS, {}).get(item_id, {})
        item.get(type_of_data)

    def get_enemy_data(self, enemy_id, type_of_data):
        enemy = self.scenes_data.get(self.ENEMIES, {}).get(enemy_id, {})
        if type_of_data != self.LOOT:
            enemy.get(type_of_data)
        else:
            items = []
            for item in enemy.get(self.LOOT, []):
                items.append([item.get(self.ITEM_ID, {}), item.get(self.CHANCE)])
            return items
        return []

    def get_scene_data(self, type_of_data):
        scene = self.scenes_data.get(self.SCENES, {}).get(self.current_scene, {})
        match type_of_data:
            case self.NAME:
                return scene.get(self.NAME)
            case self.DESCRIPTION:
                return scene.get(self.DESCRIPTION)
            case self.IS_LAST_SCENE:
                if self.is_terminal_in_scene():
                    return scene.get(self.IS_TERMINAL)
                else:
                    return False
            case self.REQUIREMENTS_FLAGS:
                flags = []
                if self.is_there_scene_requirements():
                    for requirements in scene.get(self.REQUIREMENTS, []):
                        if requirements.get(self.TYPE, {}) == self.FLAG_IS_SET:
                            flags.append(requirements.get(self.FLAG_ID, {}))
                if len(flags) == 0:
                    return None
                else:
                    return flags
            case self.REQUIREMENTS_ITEMS:
                required_items = []
                if self.is_there_scene_requirements():
                    for requirements in scene.get(self.REQUIREMENTS, []):
                        if requirements.get(self.TYPE, {}) == self.HAVE_ITEM:
                            required_items.append(requirements.get(self.ITEM_ID, {}))
                if len(required_items) == 0:
                    return None
                else:
                    return required_items

            case self.ON_ENTER_EFFECTS_FLAGS:
                if self.is_there_scene_on_enter_effects():
                    flags = []
                    for effect in self.get_scene_on_enter_effects():
                        if effect.get(self.TYPE, {}) == self.FLAG_IS_SET:
                            flags.append(effect.get(self.FLAG_ID, {}))
                    if len(flags) == 0:
                        return None
                    else:
                        return flags
                else:
                    return None

            case self.ON_ENTER_EFFECTS_GIVE_ITEM:
                if self.is_there_scene_on_enter_effects():
                    give_items = []
                    for effect in self.get_scene_on_enter_effects():
                        if effect.get(self.TYPE, {}) == self.GIVE_ITEM:
                            give_items.append(effect.get(self.ITEM_ID, {}))
                    if len(give_items) == 0:
                        return None
                    else:
                        return give_items
                else:
                    return None

    def is_terminal_in_scene(self):
        scene = self.scenes_data.get(self.SCENES, {}).get(self.current_scene, {})
        return "is_terminal" in scene and bool(scene[self.IS_TERMINAL])

    def is_there_scene_requirements(self):
        scene = self.scenes_data.get(self.SCENES, {}).get(self.current_scene, {})
        return self.REQUIREMENTS in scene and bool(scene[self.REQUIREMENTS])

    def is_there_scene_on_enter_effects(self):
        scene = self.scenes_data.get(self.SCENES, {}).get(self.current_scene, {})
        return "on_enter_effects" in scene and bool(scene[self.ON_ENTER_EFFECTS])

    def get_scene_on_enter_effects(self):
        if self.is_there_scene_on_enter_effects():
            return self.scenes_data.get(self.SCENES, {}).get(self.current_scene, {}).get(self.ON_ENTER_EFFECTS, {})
        else:
            return []

    def get_scene_choices(self):
        choices = []
        for choice in self.scenes_data.get(self.SCENES, {}).get(self.current_scene, {}).get(self.CHOICES, []):
            choices.append([choice.get(self.ID, {}), choice.get(self.TEXT, {})])
        return choices

    def get_choice_effects(self, choice_id):
        choice = self.scenes_data.get(self.SCENES, {}).get(self.current_scene).get(self.CHOICES).get(choice_id, {})
        return choice.get(self.EFFECTS, [])

    def get_choices_data(self, choice_id, type_of_data):
        match type_of_data:
            case self.FLAGS:
                flags = []
                for effect in self.get_choice_effects(choice_id):
                    if effect.get(self.TYPE, {}) == self.SET_FLAG:
                        flags.append(effect.get(self.FLAG_ID, {}))
                if len(flags) == 0:
                    return None
                else:
                    return flags
            case self.GIVE_ITEM:
                give_items = []
                for effect in self.get_choice_effects(choice_id):
                    if effect.get(self.TYPE, {}) == self.GIVE_ITEM:
                        give_items.append(effect.get(self.ITEM_ID, {}))
                if len(give_items) == 0:
                    return None
                else:
                    return give_items
            case self.GO_TO_SCENE:
                for effect in self.get_choice_effects(choice_id):
                    if effect.get(self.TYPE, {}) == self.GO_TO_SCENE:
                        return effect.get(self.SCENE_ID, {})
                return None
            case self.IS_FIGHT:
                for effect in self.get_choice_effects(choice_id):
                    if effect.get(self.TYPE, {}) == self.START_COMBAT:
                        return True
                return False
            case self.ENEMY_ID:
                for effect in self.get_choice_effects(choice_id):
                    if effect.get(self.TYPE, {}) == self.START_COMBAT:
                        return effect.get(self.ENEMY_ID, None)
                return None

    def get_fight_result_data(self, choice_id, fight_won, type_of_data):
        match type_of_data:
            case self.TEXT:
                for effect in self.get_choice_effects(choice_id):
                    if effect.get(self.TYPE, {}) == self.START_COMBAT:
                        if fight_won:
                            return effect.get(self.ON_WIN, {}).get(self.TEXT, None)
                        elif not fight_won:
                            return effect.get(self.ON_LOSE, {}).get(self.TEXT, None)
                return None
            case self.GO_TO_SCENE:
                for effect in self.get_choice_effects(choice_id):
                    if effect.get(self.TYPE, {}) == self.START_COMBAT:
                        if fight_won:
                            for effects in effect.get(self.ON_WIN, {}).get(self.EFFECTS, []):
                                if effects.get(self.TYPE, {}) == self.GO_TO_SCENE:
                                    return effects.get(self.SCENE_ID, None)
                        elif not fight_won:
                            for effects in effect.get(self.ON_LOSE, {}).get(self.EFFECTS, []):
                                if effects.get(self.TYPE, {}) == self.GO_TO_SCENE:
                                    return effects.get(self.SCENE_ID, None)
                return None
            case self.GIVE_ITEM:
                give_items = []
                for effect in self.get_choice_effects(choice_id):
                    if effect.get(self.TYPE, {}) == self.START_COMBAT:
                        if fight_won:
                            for effects in effect.get(self.ON_WIN, {}).get(self.EFFECTS, []):
                                if effects.get(self.TYPE, {}) == self.GIVE_ITEM:
                                    give_items.append(effects.get(self.ITEM_ID, {}))
                        elif not fight_won:
                            for effects in effect.get(self.ON_LOSE, {}).get(self.EFFECTS, []):
                                if effects.get(self.TYPE, {}) == self.GIVE_ITEM:
                                    give_items.append(effects.get(self.ITEM_ID, {}))

                if len(give_items) == 0:
                    return None
                else:
                    return give_items
            case self.FLAGS:
                flags = []
                for effect in self.get_choice_effects(choice_id):
                    if effect.get(self.TYPE, {}) == self.START_COMBAT:
                        if fight_won:
                            for effects in effect.get(self.ON_WIN, {}).get(self.EFFECTS, []):
                                if effects.get(self.TYPE, {}) == self.SET_FLAG:
                                    flags.append(effects.get(self.FLAG_ID, {}))
                        elif not fight_won:
                            for effects in effect.get(self.ON_LOSE, {}).get(self.EFFECTS, []):
                                if effects.get(self.TYPE, {}) == self.SET_FLAG:
                                    flags.append(effects.get(self.FLAG_ID, {}))
                if len(flags) == 0:
                    return None
                else:
                    return flags
