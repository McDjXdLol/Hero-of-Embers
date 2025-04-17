from library import Library


class Inventory:
    def __init__(self):
        self.inventory = []
        self.elixir_inventory = []
        self.weapon = []
        self.armor = []

    @staticmethod
    def add_to_inv(item, inv, amount=1):
        its_in_in = False
        for it in inv:
            if item in it:
                its_in_in = True
                it[1] += amount

        if not its_in_in:
            inv.append([item, amount])

    @staticmethod
    def show_equiped_weapons(inv):
        for item in inv:
            print(item, end=", ")

    def which_weapon_to_equip(self, inv_weapons):
        print("Which weapon do you want to equip?")
        for weapon_id, weapon in enumerate(inv_weapons):
            print(f"{weapon_id + 1}. {weapon}")
        try:
            selected_weapon = int(input())
            if selected_weapon <= len(inv_weapons):
                print("Equipping")
                self.equip_weapon(inv_weapons[selected_weapon - 1])
                self.remove_from_inv(inv_weapons[selected_weapon - 1], self.inventory)
            else:
                print("There is no such option!")
        except ValueError:
            print("You have to enter the number! Try again.")

    def which_armor_to_equip(self, inv_armors):
        print("Which armor do you want to equip?")
        for armors_id, armors in enumerate(inv_armors):
            print(f"{armors_id + 1}. {armors}")
        try:
            selected_armor = int(input())
            if selected_armor <= len(inv_armors):
                print("Equipping")
                self.equip_armor(inv_armors[selected_armor - 1])
                self.remove_from_inv(inv_armors[selected_armor - 1], self.inventory)
            else:
                print("There is no such option!")
        except ValueError:
            print("You have to enter the number! Try again.")

    def show_inv(self):
        inventory_weapons = []
        inventory_armors = []
        inventory_items = []
        for item in self.inventory:
            last_added = False
            for _ in Library.WEAPONS:
                if item[0] in _ and not last_added:
                    inventory_weapons.append(item[0])
                    last_added = True
                    continue
            for _ in Library.ARMORS:
                if item[0] in _ and not last_added:
                    inventory_armors.append(item[0])
                    last_added = True
                    continue
            if not last_added:
                inventory_items.append(item)
                continue

        if len(self.inventory) == 0:
            print("Inventory: Empty")
            return

        print("Weapons: ")
        for weapon in inventory_weapons:
            print(f"{weapon}")

        print("Armors: ")
        for armor in inventory_armors:
            print(f"{armor}")

        print("Miscellaneous: ")
        for rest in inventory_items:
            print(f"{rest}")

        if len(inventory_armors) > 0 or len(inventory_weapons) > 0:
            print("Do you want to equip one of them?\n1. Yes\n2. No")
            try:
                want = int(input())
                if want == 1:
                    if len(inventory_armors) > 0 and len(inventory_weapons) > 0:
                        print("Do you want to equip:\n1. Weapon\n2. Armor?")
                        try:
                            which_to_equip = int(input())
                            if which_to_equip == 1:
                                self.which_weapon_to_equip(inventory_weapons)
                            elif which_to_equip == 2:
                                self.which_armor_to_equip(inventory_armors)
                            else:
                                print("There is no such option!")
                        except ValueError:
                            print("You have to enter the number!")

                    elif len(inventory_armors) > 0:
                        self.which_armor_to_equip(inventory_armors)

                    elif len(inventory_weapons) > 0:
                        self.which_weapon_to_equip(inventory_weapons)

                elif want == 2:
                    return
                else:
                    print("There is no such option!")
            except ValueError:
                print("You have to enter the number! Try again.")

    def show_inv_elixirs(self):
        for el in self.elixir_inventory:
            print(f"{el[0]} x{el[1]}", end=", ")

    @staticmethod
    def remove_from_inv(item, inv):
        for it in inv:
            if item in it:
                it[1] -= 1
                if it[1] == 0:
                    inv.remove(it)

    @staticmethod
    def check_if_in_inv(item, inv):
        for it in inv:
            if item in it:
                return True
        return False

    def equip_weapon(self, item):
        old_weapon_damage = 0
        for weapon in Library.WEAPONS:
            if item in weapon[0]:
                if not len(self.weapon) == 0:
                    for old_weapon in Library.WEAPONS:
                        if self.weapon[0] in old_weapon:
                            old_weapon_damage = old_weapon[1]
                            self.weapon.remove(self.weapon[0])
                self.weapon.append(item)
                print(f"Weapon equiped: {item}")
                return old_weapon_damage, weapon[1]
            return None
        return None

    def equip_armor(self, item):
        old_armor = 0
        for armor in Library.ARMORS:
            if item in armor[0]:
                if not len(self.armor) == 0:
                    for old_armor in Library.ARMORS:
                        if self.armor[0] in old_armor:
                            old_armor = old_armor[1]
                            self.armor.remove(self.armor[0])
                self.armor.append(item)
                print(f"Armor equiped: {item}")
                return old_armor, armor[1]
            return None
        return None
