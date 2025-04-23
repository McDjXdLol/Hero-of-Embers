from hero_of_embers.inventory import Inventory
from hero_of_embers.library import Library
from hero_of_embers.entity import Entity

class Player(Entity):
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
        Gives the player experience and handles leveling up when thresholds are reached.

        Parameters
        ----------
        amount : int
            Amount of experience to give.
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

        while isinstance(self.level, int) and self.level < len(self.experience_to_next_level) + len(
                self.experience_to_legendary_level):
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
        Lets the player choose a legendary bonus after leveling up past the regular cap.
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
        Lets the player choose a bonus after leveling up.
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
        Applies the selected legendary bonus to the player.

        Parameters
        ----------
        sel : int
            The selected bonus:
            - 1: +15 Damage
            - 2: +30 HP
            - 3: +15 Armor
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
        Applies the selected regular level-up bonus to the player.

        Parameters
        ----------
        sel : int
            The selected bonus:
            - 1: +5 Damage
            - 2: +10 HP
            - 3: +5 Armor
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
