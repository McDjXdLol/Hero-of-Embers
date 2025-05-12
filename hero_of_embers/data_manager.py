import json
import os

# Getting scenes file location
def check_for_file():
    """
    Gets the file path for the scene data based on the language.

    Returns
    -------
    str
        The absolute file path to the scene data file.
    """
    curr_dir = os.path.dirname(__file__)
    data_dir = os.path.join(curr_dir, "data")
    data_file = os.path.join(data_dir, f"game_data.json")
    return data_file

class SceneManager:
    """
    Manages the loading and retrieval of scene data for a game.

    Attributes
    ----------
    lang : str
        The language code for the scene data.
    data_file : str
        The file path to the scene data file.
    scenes_data : dict
        The loaded scene data from the JSON file.
    current_scene : str
        The ID of the current scene.
    GAME_TITLE : str
        Constant key for the game title.
    STARTING_SCENE_ID : str
        Constant key for the starting scene ID.
    NAME : str
        Constant key for scene/item/etc. name.
    DESCRIPTION : str
        Constant key for scene/item/etc. description.
    TYPE : str
        Constant key for the type of element (e.g., item, flag).
    VALUE : str
        Constant key for item value.
    HEALTH : str
        Constant key for health attribute.
    ATTACK : str
        Constant key for attack attribute.
    LOOT : str
        Constant key for loot data.
    IS_LAST_SCENE : str
        Constant key for indicating if a scene is the last one.
    REQUIREMENTS : str
        Constant key for scene requirements.
    REQUIREMENTS_FLAGS : str
        Constant key for required flags.
    REQUIREMENTS_ITEMS : str
        Constant key for required items.
    ON_ENTER_EFFECTS : str
        Constant key for effects when entering a scene.
    ON_ENTER_EFFECTS_FLAGS : str
        Constant key for flags set when entering a scene.
    ON_ENTER_EFFECTS_GIVE_ITEM : str
        Constant key for items given when entering a scene.
    FLAGS : str
        Constant key for flags.
    GIVE_ITEM : str
        Constant key for giving an item.
    GO_TO_SCENE : str
        Constant key for scene transition.
    IS_FIGHT : str
        Constant key for indicating a fight scene.
    ENEMY_ID : str
        Constant key for the enemy ID in a fight.
    TEXT : str
        Constant key for text/dialog.
    IS_TERMINAL : str
        Constant key for terminal state of a scene
    STATS : str
        Constant key for character stats.
    INVENTORY : str
        Constant key for inventory.
    GOLD : str
        Constant key for gold amount.
    PLAYER_DEFAULTS : str
        Constant key for default player settings.
    ENEMIES : str
        Constant key for enemy data.
    ITEMS : str
        Constant key for item data.
     ITEM_ID : str
        Constant key for item ID
    CHANCE : str
        Constant key for chance of drop.
    SCENES : str
        Constant key for scene data.
    FLAG_ID : str
        Constant key for flag ID.
    HAVE_ITEM : str
        Constant key for having an item requirement
    FLAG_IS_SET : str
        Constant key for flag being set requirement
    CHOICES : str
        Constant key for choices in a scene
    ID : str
        Constant key for ID.
    EFFECTS : str
        Constant key for effects.
    SET_FLAG: str
        Constant for setting a flag
    SCENE_ID: str
        Constant for scene ID
    START_COMBAT: str
        Constant for starting combat
    ON_WIN: str
        Constant for on win effects
    ON_LOSE: str
        Constant for on lose effects
    ARMOR: str
        Constant for armor value
    XP_DROP: str
        Constant for experience drop
    HEALING_ITEMS: str
        Constant key for healing items' data.
    HEAL_AMOUNT: str
        Constant key for heal amount.

    """
    def __init__(self, lang="en"):
        """
        Initializes the SceneManager with the specified language and loads scene data.

        Parameters
        ----------
        lang : str, optional
            The language code for the scene data (e.g., 'en', 'pl'). Defaults to 'en'.
        """
        # Setting up language
        self.lang = lang
        self.data_file = check_for_file()

        # Loading scenes file
        try:
            with open(self.data_file, 'r', encoding='utf-8') as scene_file:
                self.scenes_data = json.load(scene_file)
        except FileNotFoundError:
            print(f"Error: Languages file not found: {self.data_file}")
            self.scenes_data = {}
        except json.JSONDecodeError:
            print(f"Error: Failed to decode JSON: {self.data_file}")

        self.STARTING_SCENE_ID = "starting_scene_id"
        self.current_scene = self.get_starting_scene()

        # Constant Variables
        # -----------------------------------------------------------------
        self.GAME_TITLE = "game_title"
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
        self.ARMOR = "armor"
        self.XP_DROP = "xp_drop"
        self.HEALING_ITEMS = "healing_items"
        self.HEAL_AMOUNT = "heal_amount"
        # -----------------------------------------------------------------

    def set_current_scene(self, scene_id):
        """
        Sets the current scene ID.

        Parameters
        ----------
        scene_id : str
            The ID of the scene to set as current.
        """
        self.current_scene = scene_id

    def get_game_title(self):
        """
        Retrieves the game title.

        Returns
        -------
        str
            The title of the game, or None if not found.
        """
        return self.scenes_data.get(self.GAME_TITLE)

    def get_starting_scene(self):
        """
        Retrieves the ID of the starting scene.

        Returns
        -------
        str
            The ID of the starting scene, or None if not found.
        """
        return self.scenes_data.get(self.STARTING_SCENE_ID)

    def get_starting_inv(self):
        """
        Retrieves the starting inventory for the player.

        Returns
        -------
        dict
            The starting inventory, or None if not found.
        """
        return self.scenes_data.get(self.PLAYER_DEFAULTS, {}).get(self.INVENTORY)

    def get_starting_flags(self):
        """
        Retrieves the starting flags for the player.

        Returns
        -------
        dict
            The starting flags, or None if not found.
        """
        return self.scenes_data.get(self.PLAYER_DEFAULTS, {}).get(self.FLAGS)

    def get_starting_cash(self):
        """
        Retrieves the starting cash for the player

        Returns
        -------
        int
            The starting cash, or None if not found
        """
        return self.scenes_data.get(self.PLAYER_DEFAULTS, {}).get(self.STATS, {}).get(self.GOLD)

    def get_all_heal_items_ids(self):
        """
        Retrieves IDs of all healing items.

        Returns
        -------
        list
            List of all healing item IDs.
        """
        return list(self.scenes_data.get(self.HEALING_ITEMS, {}).keys())

    def get_heal_item_data(self, item_id, type_of_data):
        """
        Retrieves data for a specific healing item.

        Parameters
        ----------
        item_id : str
            The ID of the healing item.
        type_of_data : str
            The type of data to retrieve (e.g., 'name', 'heal_amount').

        Returns
        -------
        Any
            The requested data for the healing item, or None if not found.
        """
        item = self.scenes_data.get(self.HEALING_ITEMS, {}).get(item_id, {})
        return item.get(type_of_data)

    def get_all_items_ids(self):
        """
        Retrieves IDs of all items.

        Returns
        -------
        list
            List of all item IDs.
        """
        return list(self.scenes_data.get(self.ITEMS, {}).keys())

    def get_item_data(self, item_id, type_of_data):
        """
        Retrieves data for a specific item.

        Parameters
        ----------
        item_id : str
            The ID of the item.
        type_of_data : str
            The type of data to retrieve (e.g., 'name', 'description').

        Returns
        -------
        Any
            The requested data for the item, or None if not found.
        """
        item = self.scenes_data.get(self.ITEMS, {}).get(item_id, {})
        return item.get(type_of_data)

    def get_enemy_data(self, enemy_id, type_of_data):
        """
        Retrieves data for a specific enemy.

        Parameters
        ----------
        enemy_id : str
            The ID of the enemy.
        type_of_data : str
            The type of data to retrieve (e.g., 'name', 'health').

        Returns
        -------
        Any
            The requested data for the enemy, or None if not found.  Returns
            a list of [item_id, chance] for LOOT.
        """
        enemy = self.scenes_data.get(self.ENEMIES, {}).get(enemy_id, {})
        if type_of_data != self.LOOT:
            return enemy.get(type_of_data, [])
        else:
            items = []
            for item in enemy.get(self.LOOT, []):
                items.append([item.get(self.ITEM_ID, {}), item.get(self.CHANCE)])
            return items

    def get_scene_data(self, type_of_data, scene_id=""):
        """
        Retrieves data for the current scene.

        Parameters
        ----------
        type_of_data : str
            The type of data to retrieve (e.g., 'name', 'description').
        scene_id : str
            The name of scene that will be returned.

        Returns
        -------
        Any
            The requested data for the scene, or None if not found.
        """
        if scene_id == "":
            scene_id = self.current_scene

        scene = self.scenes_data.get(self.SCENES, {}).get(scene_id, {})
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
                if self.is_there_scene_requirements(scene_id):
                    for requirements in scene.get(self.REQUIREMENTS, []):
                        if requirements.get(self.TYPE, {}) == self.FLAG_IS_SET:
                            flags.append(requirements.get(self.FLAG_ID, {}))
                if len(flags) == 0:
                    return None
                else:
                    return flags
            case self.REQUIREMENTS_ITEMS:
                required_items = []
                if self.is_there_scene_requirements(scene_id):
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
        return None

    def is_terminal_in_scene(self) -> bool:
        """
        Checks if the current scene has is_terminal variable.

        Returns
        -------
        bool
            True if the scene has is_terminal variable, False otherwise.
        """
        scene = self.scenes_data.get(self.SCENES, {}).get(self.current_scene, {})
        return "is_terminal" in scene and bool(scene[self.IS_TERMINAL])

    def is_there_scene_requirements(self, scene_id):
        """
        Checks if the current scene has requirements.

        Returns
        -------
        bool
            True if the scene has requirements, False otherwise.
        """
        scene = self.scenes_data.get(self.SCENES, {}).get(scene_id, {})
        return self.REQUIREMENTS in scene and bool(scene[self.REQUIREMENTS])

    def is_there_scene_on_enter_effects(self):
        """
        Checks if the current scene has on-enter effects.

        Returns
        -------
        bool
            True if the scene has on-enter effects, False otherwise.
        """
        scene = self.scenes_data.get(self.SCENES, {}).get(self.current_scene, {})
        return "on_enter_effects" in scene and bool(scene[self.ON_ENTER_EFFECTS])

    def get_scene_on_enter_effects(self):
        """
        Retrieves the on-enter effects for the current scene.

        Returns
        -------
        list
            A list of on-enter effects, or an empty list if there are none.
        """
        if self.is_there_scene_on_enter_effects():
            return self.scenes_data.get(self.SCENES, {}).get(self.current_scene, {}).get(self.ON_ENTER_EFFECTS, {})
        else:
            return []

    def get_scene_choices(self):
        """
        Retrieves the choices for the current scene.

        Returns
        -------
        list
            A list of choices, where each choice is a list of [choice_id, choice_text].
        """
        choices = []
        for choice in self.scenes_data.get(self.SCENES, {}).get(self.current_scene, {}).get(self.CHOICES, []):
            choices.append([choice.get(self.ID, {}), choice.get(self.TEXT, {})])
        return choices

    def get_choice_effects(self, choice_id):
        """
        Retrieves the effects of a specific choice.

        Parameters
        ----------
        choice_id : str
            The ID of the choice.

        Returns
        -------
        list
            A list of effects for the choice.
        """
        choice = self.scenes_data.get(self.SCENES, {}).get(self.current_scene, {}).get(self.CHOICES, {})[choice_id]
        return choice.get(self.EFFECTS, [])

    def get_choices_data(self, choice_id, type_of_data):
        """
        Retrieves data about a specific choice.

        Parameters
        ----------
        choice_id : str
            The ID of the choice.
        type_of_data : str
            The type of data to retrieve (e.g., 'flags', 'go_to_scene').

        Returns
        -------
        Any
            The requested data for the choice, or None if not found.
        """
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
            case _:
                choice = self.scenes_data.get(self.SCENES, {}).get(self.current_scene).get(self.CHOICES)[choice_id]
                return choice.get(type_of_data)

    def get_fight_result_data(self, choice_id, fight_won, type_of_data):
        """
        Retrieves data about the result of a fight.

        Parameters
        ----------
        choice_id : str
            The ID of the choice that initiated the fight.
        fight_won : bool
            Indicates whether the fight was won (True) or lost (False).
        type_of_data : str
            The type of data to retrieve (e.g., 'text', 'go_to_scene').

        Returns
        -------
        Any
            The requested data about the fight result, or None if not found.
        """
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
        return None
