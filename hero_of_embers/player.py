from hero_of_embers.inventory import Inventory


class Player:
    def __init__(self, name, hp, player_class, armor, damage, ui):
        """
        Class that stores all information about the player such as HP, damage, armor, level, etc.

        Parameters
        ----------
        name : str
            Username of the player.
        hp : int
            Initial health points of the player.
        player_class : str
            Chosen class of the player.
        armor : int
            Initial amount of armor.
        damage : int
            Base damage dealt by the player.
        ui : hero_of_embers.ui_manager.UI
            Instance of the UI manager to handle user interface updates.
        """
        self.ui = ui
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_armor = armor
        self.armor = armor
        self.damage = damage
        self.player_class = player_class
        self.dead = False
        self.inventory = Inventory(ui)
        self.level = 1
        self.experience = 0
        self.experience_to_next_level = [0, 50, 120, 210, 320, 450, 600, 770, 960, 1170, 1400]
        self.experience_to_legendary_level = [2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000]

    def deal_damage(self, amount):
        """
        Applies damage to the player, reducing armor first, then health.

        Parameters
        ----------
        amount : int
            Amount of damage to apply.

        Returns
        -------
        bool
            True if the player dies, otherwise False.
        """
        if (self.hp + self.armor) - amount <= 0:
            return self.kill_player()
        else:
            if self.armor - amount < 0:
                self.hp += self.armor - amount
                self.armor = 0
            else:
                self.armor -= amount
            return False

    def heal_hp(self, amount):
        """
        Heals the player's HP without exceeding max HP.

        Parameters
        ----------
        amount : int
            Amount of HP to heal.
        """
        if self.hp + amount > self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp += amount

    def kill_player(self):
        """
        Kills the player by setting HP and armor to 0.

        Returns
        -------
        bool
            Always returns True to indicate the player is dead.
        """
        self.hp = 0
        self.armor = 0
        self.dead = True
        return self.dead

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
            try:
                sel = int(input(""))
                if 1 > sel > 3:
                    self.ui.change_text("The number is incorrect!")
                else:
                    self.ui.change_text(f"You selected {sel}")
                    self.give_legendary_bonus(sel)
                    break
            except ValueError:
                self.ui.change_text("You have to enter the number!")

    def select_boost(self):
        """
        Lets the player choose a bonus after leveling up.
        """
        while True:
            self.ui.change_text("Select bonus: ")
            self.ui.change_text("1. Damage +5")
            self.ui.change_text("2. HP +10")
            self.ui.change_text("3. Armor +5")
            try:
                sel = int(input(""))
                if 1 <= sel <= 3:
                    self.ui.change_text(f"You selected {sel}")
                    self.give_bonus(sel)
                    break
                else:
                    self.ui.change_text("The number is incorrect! Try again!")
            except ValueError:
                self.ui.change_text("You have to enter the number!")

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
