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

    def show_inv(self):
        for item in self.inventory:
            print(f"{item[0]} x{item[1]}", end=", ")
        if len(self.inventory) == 0:
            print("Inventory: Empty")

    def show_inv_elixirs(self):
        for el in self.elixir_inventory:
            print(f"{el[0]} x{el[1]}", end=", ")

    @staticmethod
    def remove_from_inv(item, inv):
        for it in inv:
            if item[0] in it:
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
                return old_weapon_damage, weapon[1]

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
                return old_armor, armor[1]
