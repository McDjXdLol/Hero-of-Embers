import random
import time
from library import Library


class BattleHandler:
    """
    Class that handles the battles.
    """

    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start_battle(self):
        to_return = f"""    {self.player.name}
HP:{self.player.hp}
Armor: {self.player.armor}
Damage: {self.player.damage}

    {self.enemy.name}
HP: {self.enemy.hp}
Armor: {self.enemy.armor}
Damage: {self.enemy.damage}"""
        return to_return

    def enemy_turn(self):
        print(f"\n\n{self.enemy.name} turn!\n")
        self.player.deal_damage(self.enemy.damage)
        time.sleep(0.5)
        print(f"{self.enemy.name} dealt {self.enemy.damage} dmg! \n{self.player.name} HP: {self.player.hp} Armor: {self.player.armor}")
        return 0

    def player_turn(self):
        print(f"\n\n{self.player.name} turn")
        while True:
            print("\nSelect option: ")
            print("1. Normal attack (100% chance)\n2.Quick attack (30% chance)\n3. Strong attack (20% chance)\n4. Heal\n5. Check Inventory")
            try:
                sel = int(input())
                if sel < 1:
                    print("The number is incorrect!")
                    continue
                elif sel > 5:
                    print("The number is incorrect!")
                    continue
                else:
                    time.sleep(0.5)
                    return self.sel_attack(sel)
            except ValueError:
                print("You have to enter number!")
                continue

    def sel_attack(self, attack_sel):
        match attack_sel:
            case 1:
                self.enemy.deal_damage(self.player.damage)
                print(
                    f"{self.player.name} dealt {self.player.damage} dmg!\n{self.enemy.name} HP {self.enemy.hp} Armor: {self.enemy.armor}")
                return 1
            case 2:
                if random.random() < 0.3:
                    self.enemy.deal_damage(self.player.damage)
                    print(
                        f"{self.player.name} dealt {self.player.damage} dmg!\n{self.enemy.name} HP {self.enemy.hp} Armor: {self.enemy.armor}")
                    return 0
                else:
                    print(f"{self.player.name} miss quick attack!")
                    return 1
            case 3:
                if random.random() < 0.2:
                    self.enemy.deal_damage(self.player.damage * 5)
                    print(
                        f"{self.player.name} hit strong attack! {self.player.name} dealt {self.player.damage * 5} dmg!\n{self.enemy.name} HP {self.enemy.hp} Armor: {self.enemy.armor}")
                    return 1
                else:
                    print(f"{self.player.name} miss strong attack!")
                    return 1
            case 4:
                elixirs_in_inv = []
                for elixir in Library.HEAL_ITEMS:
                    if self.player.inventory.check_if_in_inv(elixir[0], self.player.inventory.elixir_inventory):
                        for item_nr, item in enumerate(self.player.inventory.elixir_inventory):
                            elixirs_in_inv.append([item_nr, item])
                if len(elixirs_in_inv) == 0:
                    print(f"{self.player.name} don't have any elixirs in inventory!")
                    return 0
                else:
                    while True:
                        print("Choose the elixir:")
                        for eli in elixirs_in_inv:
                            print(f"{eli[0]+1}. {eli[1][0]} x{eli[1][1]}")
                        try:
                            chosen_elixir = int(input())
                            if chosen_elixir < 1:
                                print("The number is incorrect!")
                            elif chosen_elixir > len(elixirs_in_inv):
                                print("The number is incorrect!")
                            else:
                                break
                        except ValueError:
                            print("You have to enter the number!")
                    chosen_elixir_name = elixirs_in_inv[chosen_elixir-1][1]
                    print(f"You choose {chosen_elixir_name[0]}")
                    self.player.inventory.remove_from_inv(chosen_elixir_name, self.player.inventory.elixir_inventory)
                    for elix in Library.HEAL_ITEMS:
                        if chosen_elixir_name[0] in elix:
                            self.player.heal_hp(elix[1])
                            print(f"{self.player.name} was healed for {elix[1]} hp. {self.player.name} has {self.player.hp} HP!")
                            return 0
            case 5:
                print("Elixirs: ", end="")
                self.player.inventory.show_inv_elixirs()
                print()
                print("Items: ", end="")
                self.player.inventory.show_inv()
                print()
                print("Weapon: ", end="")
                self.player.inventory.show_equiped_weapons(self.player.inventory.weapon)
                print()
                print("Armor: ", end="")
                self.player.inventory.show_equiped_weapons(self.player.inventory.armor)
                return 0


    def battle(self):
        print(self.start_battle())
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
            self.player.armor += int(self.player.max_armor/4)
            return True
        else:
            return False
