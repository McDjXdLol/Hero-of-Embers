import random
import time

from hero_of_embers.get_language_text import GetTexts
from hero_of_embers.library import Library


class BattleHandler:
    """
    Handles combat interactions between the player and enemies.

    Parameters
    ----------
    player : hero_of_embers.player.Player
        The player character object.
    enemy : hero_of_embers.enemy.Enemy
        The enemy character object.
    ui : hero_of_embers.ui_manager.UI
        UI manager instance for user interactions.
    """

    def __init__(self, player, enemy, ui, lang):
        """
        Initializes the battle handler with player, enemy, and UI.

        Parameters
        ----------
        player : hero_of_embers.player.Player
            The player character object.
        enemy : hero_of_embers.enemy.Enemy
            The enemy character object.
        ui : hero_of_embers.ui_manager.UI
            The UI manager for displaying information and handling user input.
        """
        self.lang = lang
        self.ui = ui
        self.player = player
        self.enemy = enemy

    def battle_information(self):
        """
        Get current stats of the player and the enemy.

        Returns
        -------
        list of str
            A list of strings displaying stats for both player and enemy.
        """
        return [
            f"    {self.player.name}",
            f"HP:{self.player.hp}",
            f"Armor: {self.player.armor}",
            f"Damage: {self.player.damage}",
            f"    {self.enemy.name}",
            f"HP: {self.enemy.hp}",
            f"Armor: {self.enemy.armor}",
            f"Damage: {self.enemy.damage}"
        ]

    def enemy_turn(self):
        """
        Execute the enemy's turn in combat.

        Returns
        -------
        int
            Always returns 0 to indicate player goes next.
        """
        self.ui.clean_print(2)
        self.ui.change_text(GetTexts.load_texts("battle_enemy_turn", self.lang).format(name=self.enemy.name))
        self.ui.clean_print(1)
        self.player.deal_damage(self.enemy.damage)
        time.sleep(0.5)
        self.ui.change_text([
            f"{self.enemy.name} dealt {self.enemy.damage} dmg!",
            f"{self.player.name} HP: {self.player.hp} Armor: {self.player.armor}"
        ])
        return 0

    def player_turn(self):
        """
        Handle the player's turn selection.

        Returns
        -------
        int
            0 if the enemy should go next, 1 if the player goes again.
        """
        self.ui.clean_print(2)
        self.ui.change_text(GetTexts.load_texts("battle_player_turn", self.lang).format(name=self.player.name))
        while True:
            self.ui.clean_print(1)
            self.ui.change_text(GetTexts.load_texts("battle_select_option", self.lang))
            self.ui.change_text([
                "1. Normal attack (100% chance)",
                "2. Quick attack (30% chance)",
                "3. Strong attack (20% chance)",
                "4. Heal",
                "5. Check Inventory"
            ])
            sel = int(self.ui.get_input(0, ""))
            if sel < 1 or sel > 5:
                self.ui.change_text(GetTexts.load_texts("battle_incorrect_number", self.lang))
                continue
            else:
                time.sleep(0.5)
                return self.attack_selection(sel)
        return 0

    def normal_attack(self):
        """
        Perform a normal attack on the enemy.

        Returns
        -------
        int
            1 if enemy goes next, 0 if player goes again.
        """
        self.enemy.deal_damage(self.player.damage)
        self.ui.change_text([
            f"{self.player.name} dealt {self.player.damage} dmg!",
            f"{self.enemy.name} HP {self.enemy.hp} Armor: {self.enemy.armor}"
        ])
        return 1

    def quick_attack(self):
        """
        Perform a quick attack on the enemy with a 30% chance of success.

        Returns
        -------
        int
            0 if the enemy goes next, 1 if the player goes again.
        """
        if random.random() < 0.3:
            self.enemy.deal_damage(self.player.damage)
            self.ui.change_text([
                f"{self.player.name} dealt {self.player.damage} dmg!",
                f"{self.enemy.name} HP {self.enemy.hp} Armor: {self.enemy.armor}"
            ])
            return 0
        else:
            self.ui.change_text(GetTexts.load_texts("battle_missed_quick_attack", self.lang).format(name=self.player.name))
            return 1

    def strong_attack(self):
        """
        Perform a strong attack on the enemy with a 20% chance of success.

        Returns
        -------
        int
            1 if enemy goes next, 0 if player goes again.
        """
        if random.random() < 0.2:
            dmg = self.player.damage * 5
            self.enemy.deal_damage(dmg)
            self.ui.change_text([
                f"{self.player.name} hit strong attack! {self.player.name} dealt {dmg} dmg!",
                f"{self.enemy.name} HP {self.enemy.hp} Armor: {self.enemy.armor}"
            ])
            return 1
        else:
            self.ui.change_text(GetTexts.load_texts("battle_missed_strong_attack", self.lang).format(name=self.player.name))
            return 1

    def choose_elixir(self):
        """
        Allows the player to choose an elixir from their inventory.

        Returns
        -------
        int
            0 if player should proceed to the enemy's turn, or repeat the player's turn.
        """
        elixirs_in_inv = list(self.player.inventory.elixir_inventory)
        if not elixirs_in_inv:
            self.ui.change_text(GetTexts.load_texts("battle_no_elixir", self.lang).format(name=self.player.name))
            return 0
        while True:
            self.ui.change_text(GetTexts.load_texts("battle_choose_elixir", self.lang))
            for eli_nr, eli in enumerate(elixirs_in_inv):
                self.ui.change_text(GetTexts.load_texts("battle_elixir_option", self.lang).format(eli_nr=eli_nr+1, eli=eli))
            chosen_elixir = self.ui.get_input(0, "")
            if chosen_elixir < 1 or chosen_elixir > len(elixirs_in_inv):
                self.ui.change_text(GetTexts.load_texts("battle_incorrect_number_elixir", self.lang))
            else:
                break
        chosen_elixir_name = elixirs_in_inv[chosen_elixir - 1][0]
        self.ui.change_text(GetTexts.load_texts("battle_chosen_elixir", self.lang).format(chosen_elixir_name=chosen_elixir_name))
        self.player.inventory.remove_from_inv(chosen_elixir_name, self.player.inventory.elixir_inventory)
        for elix in Library.HEAL_ITEMS:
            if chosen_elixir_name in elix:
                self.player.heal_hp(elix[1])
                self.ui.change_text(
                    f"{self.player.name} was healed for {elix[1]} hp. {self.player.name} has {self.player.hp} HP!"
                )
                return 0
        return 0

    def attack_selection(self, move_sel):
        """
        Process the selected player move.

        Parameters
        ----------
        move_sel : int
            Selected move number (1-5).

        Returns
        -------
        int
            1 if enemy goes next, 0 if player goes again.
        """
        match move_sel:
            case 1:
                return self.normal_attack()
            case 2:
                return self.quick_attack()
            case 3:
                return self.strong_attack()
            case 4:
                return self.choose_elixir()
            case 5:
                self.player.inventory.show_inv()
                return 0
            case _:
                return 0

    def battle(self):
        """
        Main battle loop handler.

        Returns
        -------
        bool
            True if the player wins, False if the enemy wins.
        """
        self.ui.change_text(self.battle_information())
        whos_next = random.randint(0, 1)
        while not self.player.dead and not self.enemy.dead:
            if whos_next == 0:
                whos_next = self.player_turn()
            else:
                whos_next = self.enemy_turn()
        if self.player.dead:
            return False
        elif self.enemy.dead:
            self.player.level_handler.give_experience(self.enemy.experience_drop)
            self.player.inventory.wallet += self.enemy.money_drop
            self.ui.change_text(GetTexts.load_texts("battle_enemy_money_drop", self.lang).format(money_drop=self.enemy.money_drop))
            self.player.armor += int(self.player.max_armor / 2)
            if self.enemy.experience_drop >= 25:
                dropping_item = Library.HEAL_ITEMS[random.randint(3, len(Library.HEAL_ITEMS) - 1)]
                amount = random.randint(1, 3)
            else:
                dropping_item = Library.HEAL_ITEMS[random.randint(0, 3)]
                amount = random.randint(1, 4)
            self.player.inventory.add_to_inv(dropping_item[0], self.player.inventory.elixir_inventory, amount=amount)
            return True
        return False
