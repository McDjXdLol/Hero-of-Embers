import random
import time
from library import Library


class BattleHandler:
    """
    Class that handles the battles.
    """

    def __init__(self, player, enemy, ui):
        self.ui = ui
        self.player = player
        self.enemy = enemy

    def start_battle(self):
        to_return = [f"    {self.player.name}", f"HP:{self.player.hp}", f"Armor: {self.player.armor}",
                     f"Damage: {self.player.damage}", f"    {self.enemy.name}", f"HP: {self.enemy.hp}",
                     f"Armor: {self.enemy.armor}", f"Damage: {self.enemy.damage}"]
        return to_return

    def enemy_turn(self):
        self.ui.change_text("\n")
        self.ui.change_text("\n")
        self.ui.change_text(f"{self.enemy.name} turn!")
        self.ui.change_text("\n")
        self.player.deal_damage(self.enemy.damage)
        time.sleep(0.5)
        self.ui.change_text([f"{self.enemy.name} dealt {self.enemy.damage} dmg!",
                             f"{self.player.name} HP: {self.player.hp} Armor: {self.player.armor}"])
        return 0

    def player_turn(self):
        self.ui.change_text("\n")
        self.ui.change_text("\n")
        self.ui.change_text(f"{self.player.name} turn")
        while True:
            self.ui.change_text("\n")
            self.ui.change_text("Select option: ")
            self.ui.change_text([
                "1. Normal attack (100% chance)", "2.Quick attack (30% chance)", "3. Strong attack (20% chance)",
                "4. Heal", "5. Check Inventory"])
            try:
                sel = int(self.ui.get_input(0, ""))
                if sel < 1:
                    self.ui.change_text("The number is incorrect!")
                    continue

                elif sel > 5:
                    self.ui.change_text("The number is incorrect!")
                    continue

                else:
                    time.sleep(0.5)
                    return self.sel_attack(sel)

            except ValueError:
                self.ui.change_text("You have to enter number!")
                continue

    def sel_attack(self, attack_sel):
        match attack_sel:
            case 1:
                self.enemy.deal_damage(self.player.damage)
                self.ui.change_text([
                    f"{self.player.name} dealt {self.player.damage} dmg!", f"{self.enemy.name} HP {self.enemy.hp} Armor: {self.enemy.armor}"])
                return 1
            case 2:
                if random.random() < 0.3:
                    self.enemy.deal_damage(self.player.damage)
                    self.ui.change_text([
                        f"{self.player.name} dealt {self.player.damage} dmg!", f"{self.enemy.name} HP {self.enemy.hp} Armor: {self.enemy.armor}"])
                    return 0
                else:
                    self.ui.change_text(f"{self.player.name} miss quick attack!")
                    return 1
            case 3:
                if random.random() < 0.2:
                    self.enemy.deal_damage(self.player.damage * 5)
                    self.ui.change_text([
                        f"{self.player.name} hit strong attack! {self.player.name} dealt {self.player.damage * 5} dmg!", f"{self.enemy.name} HP {self.enemy.hp} Armor: {self.enemy.armor}"])
                    return 1
                else:
                    self.ui.change_text(f"{self.player.name} miss strong attack!")
                    return 1
            case 4:
                elixirs_in_inv = []
                for elixir in self.player.inventory.elixir_inventory:
                    elixirs_in_inv.append(elixir)
                if len(elixirs_in_inv) == 0:
                    self.ui.change_text(f"{self.player.name} don't have any elixirs in inventory!")
                    return 0
                else:
                    while True:
                        self.ui.change_text("Choose the elixir:")
                        for eli_nr, eli in enumerate(elixirs_in_inv):
                            self.ui.change_text(f"{eli_nr + 1}. {eli[0]} x{eli[1]}")
                        try:
                            chosen_elixir = self.ui.get_input(0, "")
                            if chosen_elixir < 1:
                                self.ui.change_text("The number is incorrect!")
                            elif chosen_elixir > len(elixirs_in_inv):
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
        return 1

    def battle(self):
        self.ui.change_text(self.start_battle())
        whos_next = random.randint(0, 1)
        while not self.player.dead and not self.enemy.dead:
            if whos_next == 0:
                # Player turn
                whos_next = self.player_turn()
            else:
                # Enemy turn
                whos_next = self.enemy_turn()
        if self.player.dead:
            return False
        elif self.enemy.dead:
            self.player.give_experience(self.enemy.experience_drop)
            self.player.armor += int(self.player.max_armor / 2)
            if self.enemy.experience_drop >= 25:
                dropping_item = Library.HEAL_ITEMS[random.randint(3, len(Library.HEAL_ITEMS) - 1)]
                amount = random.randint(1, 3)
            else:
                dropping_item = Library.HEAL_ITEMS[random.randint(0, 3)]
                amount = random.randint(1, 4)
            self.player.inventory.add_to_inv(dropping_item[0], self.player.inventory.elixir_inventory, amount=amount)
            return True
        else:
            return False
