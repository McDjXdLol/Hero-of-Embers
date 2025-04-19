from hero_of_embers.inventory import Inventory


class Player:
    def __init__(self, name, hp, player_class, armor, damage, ui):
        """
        Class that got every information about player. Information like damage, hp, max hp etc.
        :param name: username
        :param hp: player hp amount
        :param player_class: player class
        :param armor: player armor amount
        :param damage: player damage amount
        :param ui: ui class
        :type name: str
        :type hp: int
        :type player_class: str
        :type armor: int
        :type damage: int
        :type ui: hero_of_embers.ui_manager.UI
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
        Function that deal player damage.
        :param amount: amount of damage
        :type amount: int
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
        Function that heal player hp.
        :param amount: amount of heal
        :type amount: int
        """
        if self.hp + amount > self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp += amount

    def kill_player(self):
        """
        Function that is used to kill player
        """
        self.hp = 0
        self.armor = 0
        self.dead = True
        return self.dead

    def give_experience(self, amount):
        """
        Function that is used to give player experience, if player enough give player level
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
        Function that is used to give player legendary boosts after getting a legendary level
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
        Function that is used to give player boosts after getting a level
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
        Function that is used to give player legendary boosts after getting a legendary level
        :param sel: selection of which bonus player wants
        :type sel: int
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
        Function that is used to give player legendary boosts after getting a legendary level
        :param sel: selection of which bonus player wants
        :type sel: int
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

