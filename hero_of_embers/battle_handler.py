import random
import time

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

    def __init__(self, player, enemy, ui):
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
        self.ui.change_text("\n")
        self.ui.change_text("\n")
        self.ui.change_text(f"{self.enemy.name} turn!")
        self.ui.change_text("\n")
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
        self.ui.change_text("\n")
        self.ui.change_text("\n")
        self.ui.change_text(f"{self.player.name} turn")
        while True:
            self.ui.change_text("\n")
            self.ui.change_text("Select option: ")
            self.ui.change_text([
                "1. Normal attack (100% chance)",
                "2. Quick attack (30% chance)",
                "3. Strong attack (20% chance)",
                "4. Heal",
                "5. Check Inventory"
            ])
            try:
                sel = int(self.ui.get_input(0, ""))
                if sel < 1 or sel > 5:
                    self.ui.change_text("The number is incorrect!")
                    continue
                time.sleep(0.5)
                return self.sel_attack(sel)
            except ValueError:
                self.ui.change_text("You have to enter number!")
                continue
        return 0

    def sel_attack(self, move_sel):
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
                self.enemy.deal_damage(self.player.damage)
                self.ui.change_text([
                    f"{self.player.name} dealt {self.player.damage} dmg!",
                    f"{self.enemy.name} HP {self.enemy.hp} Armor: {self.enemy.armor}"
                ])
                return 1
            case 2:
                if random.random() < 0.3:
                    self.enemy.deal_damage(self.player.damage)
                    self.ui.change_text([
                        f"{self.player.name} dealt {self.player.damage} dmg!",
                        f"{self.enemy.name} HP {self.enemy.hp} Armor: {self.enemy.armor}"
                    ])
                    return 0
                else:
                    self.ui.change_text(f"{self.player.name} miss quick attack!")
                    return 1
            case 3:
                if random.random() < 0.2:
                    dmg = self.player.damage * 5
                    self.enemy.deal_damage(dmg)
                    self.ui.change_text([
                        f"{self.player.name} hit strong attack! {self.player.name} dealt {dmg} dmg!",
                        f"{self.enemy.name} HP {self.enemy.hp} Armor: {self.enemy.armor}"
                    ])
                    return 1
                else:
                    self.ui.change_text(f"{self.player.name} miss strong attack!")
                    return 1
            case 4:
                elixirs_in_inv = list(self.player.inventory.elixir_inventory)
                if not elixirs_in_inv:
                    self.ui.change_text(f"{self.player.name} don't have any elixirs in inventory!")
                    return 0
                while True:
                    self.ui.change_text("Choose the elixir:")
                    for eli_nr, eli in enumerate(elixirs_in_inv):
                        self.ui.change_text(f"{eli_nr + 1}. {eli[0]} x{eli[1]}")
                    try:
                        chosen_elixir = self.ui.get_input(0, "")
                        if chosen_elixir < 1 or chosen_elixir > len(elixirs_in_inv):
                            self.ui.change_text("The number is incorrect!")
                        else:
                            break
                    except ValueError:
                        self.ui.change_text("You have to enter the number!")
                chosen_elixir_name = elixirs_in_inv[chosen_elixir - 1][0]
                self.ui.change_text(f"You choose {chosen_elixir_name}")
                self.player.inventory.remove_from_inv(chosen_elixir_name, self.player.inventory.elixir_inventory)
                for elix in Library.HEAL_ITEMS:
                    if chosen_elixir_name in elix:
                        self.player.heal_hp(elix[1])
                        self.ui.change_text(
                            f"{self.player.name} was healed for {elix[1]} hp. {self.player.name} has {self.player.hp} HP!")
                        return 0
            case 5:
                self.ui.change_text("Elixirs: ")
                self.player.inventory.show_inv_elixirs()
                self.ui.change_text("")
                self.ui.change_text("Items: ")
                self.player.inventory.show_inv()
                self.ui.change_text("")
                self.ui.change_text("Weapon: ")
                self.player.inventory.show_equiped_weapons(self.player.inventory.weapon)
                self.ui.change_text("")
                self.ui.change_text("Armor: ")
                self.player.inventory.show_equiped_weapons(self.player.inventory.armor)
                return 0
            case _:
                return 0
        return 1

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
            self.player.give_experience(self.enemy.experience_drop)
            self.player.inventory.wallet += self.enemy.money_drop
            self.ui.change_text(f"You got {self.enemy.money_drop} dragon coins!")
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
