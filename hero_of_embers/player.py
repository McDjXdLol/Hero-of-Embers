from hero_of_embers.inventory import Inventory
from hero_of_embers.library import Library
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
    level : int or str
        Current level of the player or 'MAX' if maximum level reached.
    experience : int or str
        Current experience points or 'MAX' if maximum level reached.
    experience_to_next_level : list
        List of experience thresholds for regular levels.
    experience_to_legendary_level : list
        List of experience thresholds for legendary levels.
    """

    def __init__(self, name, hp, player_class, armor, damage, ui):
        super().__init__(name, hp, armor, damage)
        self.ui = ui
        self.player_class = player_class
        self.inventory = Inventory(ui)
        self.level = 1
        self.experience = 0
        self.experience_to_next_level = Library.XP_NXT_LVL
        self.experience_to_legendary_level = Library.XP_NXT_LG_LVL

    def give_experience(self, amount):
        """
        Grants experience to the player and handles level-ups if thresholds are met.

        Parameters
        ----------
        amount : int
            Amount of experience to add to the player's total.
        """
        self.ui.change_text(f"{self.name} gained {amount} xp!")

        if self.level == "MAX":
            self.ui.change_text("You already got the maximum level!")
            return

        self.experience += amount

        while isinstance(self.level, int) and self.level < len(self.experience_to_next_level):
            xp_needed = self.experience_to_next_level[self.level]
            if self.experience >= xp_needed:
                self.experience -= xp_needed
                self.level += 1
                self.ui.change_text(f"{self.name} got next level!")
                self.select_boost()
            else:
                return

        while isinstance(self.level, int) and self.level < len(self.experience_to_next_level) + len(self.experience_to_legendary_level):
            index = self.level - len(self.experience_to_next_level)
            xp_needed = self.experience_to_legendary_level[index]
            if self.experience >= xp_needed:
                self.experience -= xp_needed
                self.level += 1
                if self.level == len(self.experience_to_next_level) + len(self.experience_to_legendary_level):
                    self.level = "MAX"
                    self.experience = "MAX"
                    self.ui.change_text("You got the maximum level!")
                    return
                self.ui.change_text(f"{self.name} got next level!")
                self.select_legendary_boost()
            else:
                return

    def select_legendary_boost(self):
        """
        Prompts the player to select a legendary bonus after reaching legendary levels.
        """
        self.ui.change_text("Select bonus: ")
        self.ui.change_text("1. Damage +15")
        self.ui.change_text("2. HP +30")
        self.ui.change_text("3. Armor +15")
        while True:
            selection = self.ui.get_input(0, "")
            if 1 > selection > 3:
                self.ui.change_text("The number is incorrect!")
            else:
                self.ui.change_text(f"You selected {selection}")
                self.give_legendary_bonus(selection)
                break

    def select_boost(self):
        """
        Prompts the player to choose a bonus after a regular level-up.
        """
        while True:
            self.ui.change_text("Select bonus: ")
            self.ui.change_text("1. Damage +5")
            self.ui.change_text("2. HP +10")
            self.ui.change_text("3. Armor +5")
            selection = self.ui.get_input(0, "")
            if 1 <= selection <= 3:
                self.ui.change_text(f"You selected {selection}")
                self.give_bonus(selection)
                break
            else:
                self.ui.change_text("The number is incorrect! Try again!")

    def give_legendary_bonus(self, sel):
        """
        Applies the selected legendary level bonus.

        Parameters
        ----------
        sel : int
            The selected bonus:
            - 1: Increase damage by 15.
            - 2: Increase max HP by 30.
            - 3: Increase armor and max armor by 15.
        """
        match sel:
            case 1:
                self.damage += 15
            case 2:
                self.max_hp += 30
                self.hp += 30
            case 3:
                self.armor += 15
                self.max_armor += 15

    def give_bonus(self, sel):
        """
        Applies the selected regular level bonus.

        Parameters
        ----------
        sel : int
            The selected bonus:
            - 1: Increase damage by 5.
            - 2: Increase max HP by 10.
            - 3: Increase armor and max armor by 5.
        """
        match sel:
            case 1:
                self.damage += 5
            case 2:
                self.max_hp += 10
                self.hp += 10
            case 3:
                self.armor += 5
                self.max_armor += 5
