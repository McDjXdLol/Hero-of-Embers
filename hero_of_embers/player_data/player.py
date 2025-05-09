from inventory import Inventory
from level_handler import LevelHandler
from hero_of_embers.entity import Entity

class Player(Entity):
    """
    Represents the player character in the game.

    Inherits from Entity and extends it with player-specific features such as
    inventory, leveling system, and experience tracking.

    Attributes
    ----------
    ui : object
        Interface for communication with the player (text-based).
    player_class : str
        The class chosen by the player (e.g., Warrior, Mage).
    inventory : Inventory
        Player's inventory management system.
    """

    def __init__(self, name, hp, player_class, armor, damage, ui, lang):
        super().__init__(name, hp, armor, damage)
        self.lang = lang
        self.ui = ui
        self.player_class = player_class
        self.inventory = Inventory(ui, self.lang)
        self.level_handler = LevelHandler(self)
