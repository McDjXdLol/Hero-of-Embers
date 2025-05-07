from get_language_text import GetTexts
from library import Library


class LevelHandler:
    def __init__(self, player):
        self.player = player
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
        self.player.ui.change_text(GetTexts.load_texts("player_gained_xp", self.player.lang).format(name=self.player.name, amount=amount))

        if self.level == "MAX":
            self.player.ui.change_text(GetTexts.load_texts("player_max_level", self.player.lang))
            return

        self.experience += amount

        while isinstance(self.level, int) and self.level < len(self.experience_to_next_level):
            xp_needed = self.experience_to_next_level[self.level]
            if self.experience >= xp_needed:
                self.experience -= xp_needed
                self.level += 1
                self.player.ui.change_text(GetTexts.load_texts("player_next_level", self.player.lang).format(name=self.player.name))
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
                    self.player.ui.change_text(GetTexts.load_texts("player_max_level_reached", self.player.lang))
                    return
                self.player.ui.change_text(GetTexts.load_texts("player_next_level", self.player.lang).format(name=self.player.name))
                self.select_legendary_boost()
            else:
                return

    def select_legendary_boost(self):
        """
        Prompts the player to select a legendary bonus after reaching legendary levels.
        """
        self.player.ui.change_text(GetTexts.load_texts("player_select_bonus", self.player.lang))
        self.player.ui.change_text(GetTexts.load_texts("player_damage_bonus", self.player.lang))
        self.player.ui.change_text(GetTexts.load_texts("player_hp_bonus", self.player.lang))
        self.player.ui.change_text(GetTexts.load_texts("player_armor_bonus", self.player.lang))
        while True:
            selection = self.player.ui.get_input(0, "")
            if 1 > selection > 3:
                self.player.ui.change_text(GetTexts.load_texts("player_incorrect_number", self.player.lang))
            else:
                self.player.ui.change_text(GetTexts.load_texts("player_selected_bonus", self.player.lang).format(selection=selection))
                self.give_legendary_bonus(selection)
                break

    def select_boost(self):
        """
        Prompts the player to choose a bonus after a regular level-up.
        """
        while True:
            self.player.ui.change_text(GetTexts.load_texts("player_select_bonus2", self.player.lang))
            self.player.ui.change_text(GetTexts.load_texts("player_damage_bonus2", self.player.lang))
            self.player.ui.change_text(GetTexts.load_texts("player_hp_bonus2", self.player.lang))
            self.player.ui.change_text(GetTexts.load_texts("player_armor_bonus2", self.player.lang))
            selection = self.player.ui.get_input(0, "")
            if 1 <= selection <= 3:
                self.player.ui.change_text(GetTexts.load_texts("player_selected_bonus", self.player.lang).format(selection=selection))
                self.give_bonus(selection)
                break
            else:
                self.player.ui.change_text(GetTexts.load_texts("player_incorrect_number_try_again", self.player.lang))

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
                self.player.damage += 15
            case 2:
                self.player.max_hp += 30
                self.player.hp += 30
            case 3:
                self.player.armor += 15
                self.player.max_armor += 15

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
                self.player.damage += 5
            case 2:
                self.player.max_hp += 10
                self.player.hp += 10
            case 3:
                self.player.armor += 5
                self.player.max_armor += 5