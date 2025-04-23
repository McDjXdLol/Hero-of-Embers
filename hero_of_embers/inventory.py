from hero_of_embers.library import Library


class Inventory:
    def __init__(self, ui):
        """
        Initializes the inventory for the player.

        Parameters
        ----------
        ui : hero_of_embers.ui_manager.UI
            UI class object to interact with the user.
        """
        self.ui = ui
        self.inventory = []
        self.elixir_inventory = []
        self.weapon = []
        self.armor = []
        self.wallet = 0

    def check_if_can_buy(self, amount):
        if self.wallet < amount:
            return False
        else:
            return True

    def take_from_wallet(self, amount):
        if self.check_if_can_buy(amount):
            self.wallet -= amount
        else:
            self.ui.change_text("You don't have enough dragon coins!")

    @staticmethod
    def add_to_inv(item, inv, amount=1):
        """
        Adds a specified amount of an item to the selected inventory.

        Parameters
        ----------
        item : list
            Item array from Library.
        inv : list
            The inventory to which the item should be added.
        amount : int, optional
            The amount of the item to add (default is 1).
        """
        for it in inv:
            if it[0][0] == item[0] and it[0][1] == item[1]:
                it[1] += amount
                return
        inv.append([item, amount])

    def which_item_to_equip(self, items, equip_function, item_type="item"):
        """
        Generic function to equip a given item type (weapon, armor, etc.).

        Parameters
        ----------
        items : list
            List of items in the player's inventory.
        equip_function : function
            Function used to equip the selected item.
        item_type : str
            Type of item, for display purposes.
        """
        self.ui.change_text(f"Which {item_type} do you want to equip?")
        for i, item in enumerate(items):
            self.ui.change_text(f"{i + 1}. {item}")
        try:
            selected = int(self.ui.get_input(0, ""))
            if selected <= len(items):
                equip_function(items[selected - 1])
                self.remove_from_inv(items[selected - 1], self.inventory)
            else:
                self.ui.change_text("There is no such option!")
        except ValueError:
            self.ui.change_text("You have to enter the number! Try again.")

    def show_inv(self):
        """
        Displays the player's inventory, including weapons, armors, and miscellaneous items.
        """
        inventory_weapons = []
        inventory_armors = []
        inventory_items = []

        for item in self.inventory:
            name = item[0][0]
            added = False

            for w in Library.WEAPONS:
                if name == w[0] and not added:
                    inventory_weapons.append(name)
                    added = True
                    break
            for a in Library.ARMORS:
                if name == a[0] and not added:
                    inventory_armors.append(name)
                    added = True
                    break

            if not added:
                inventory_items.append(item)

        if len(self.weapon) != 0:
            self.ui.change_text(f"Equipped Weapon: {self.weapon[0]}")

        if len(self.armor) != 0:
            self.ui.change_text(f"Equipped Armor: {self.armor[0]}")

        if len(self.inventory) == 0:
            self.ui.change_text("Inventory: Empty")
            return

        self.ui.change_text("Weapons: ")
        for weapon in inventory_weapons:
            self.ui.change_text(f"{weapon}")

        self.ui.change_text("Armors: ")
        for armor in inventory_armors:
            self.ui.change_text(f"{armor}")

        self.ui.change_text("Miscellaneous: ")
        for item in inventory_items:
            item_name = item[0][0]
            item_amount = item[1]
            self.ui.change_text(f"{item_name} x{item_amount}")

        self.ui.change_text(f"Dragon coins: {self.wallet}Ɇ")

        if len(inventory_armors) > 0 or len(inventory_weapons) > 0:
            self.equip_selection(inventory_armors, inventory_weapons)

    def equip_selection(self, inventory_armors, inventory_weapons):
        self.ui.change_text(["Do you want to equip one of them?", "1. Yes", "2. No"])
        try:
            want = int(self.ui.get_input(0, ""))
            if want == 1:
                if len(inventory_armors) > 0 and len(inventory_weapons) > 0:
                    self.ui.change_text(["Do you want to equip:", "1. Weapon", "2. Armor"])
                    try:
                        which_to_equip = int(self.ui.get_input(0, ""))
                        if which_to_equip == 1:
                            self.which_item_to_equip(inventory_weapons, self.equip_weapon, "weapon")
                        elif which_to_equip == 2:
                            self.which_item_to_equip(inventory_armors, self.equip_armor, "armor")
                        else:
                            self.ui.change_text("There is no such option!")
                    except ValueError:
                        self.ui.change_text("You have to enter the number!")
                elif len(inventory_armors) > 0:
                    self.which_item_to_equip(inventory_armors, self.equip_armor, "armor")
                elif len(inventory_weapons) > 0:
                    self.which_item_to_equip(inventory_weapons, self.equip_weapon, "weapon")
            elif want == 2:
                return
            else:
                self.ui.change_text("There is no such option!")
        except ValueError:
            self.ui.change_text("You have to enter the number! Try again.")

    def show_inv_elixirs(self):
        """
        Displays the player's elixirs inventory.

        Notes
        -----
        Each elixir is shown along with the amount.
        """
        for el in self.elixir_inventory:
            self.ui.change_text(f"{el[0]} x{el[1]}")

    @staticmethod
    def remove_from_inv(item_name, inv):
        """
        Removes one item from the selected inventory.

        Parameters
        ----------
        item_name : str
            The name of the item to remove.
        inv : list
            The inventory to remove the item from.
        """
        for it in inv:
            if it[0][0] == item_name:
                it[1] -= 1
                if it[1] <= 0:
                    inv.remove(it)
                break

    @staticmethod
    def check_if_in_inv(item, inv):
        """
        Checks if the player has a specified item in their inventory.

        Parameters
        ----------
        item : str
            The item to check for in the inventory.
        inv : list
            The inventory to check.

        Returns
        -------
        bool
            True if the item is in the inventory, False otherwise.
        """
        for it in inv:
            if it[0][0] == item:
                return True
        return False

    def equip_weapon(self, item_name):
        """
        Equips the selected weapon for the player.

        Parameters
        ----------
        item_name : str
            The name of the weapon to equip.

        Returns
        -------
        tuple or None
            A tuple containing the old weapon's damage and the new weapon's damage,
            or None if the weapon could not be equipped.
        """
        old_weapon_damage = 0
        for weapon in Library.WEAPONS:
            if item_name == weapon[0]:
                if len(self.weapon) > 0:
                    for old_weapon in Library.WEAPONS:
                        if self.weapon[0] == old_weapon[0]:
                            old_weapon_damage = old_weapon[1]
                            self.add_to_inv([self.weapon[0], old_weapon[1]], self.inventory)
                            self.weapon.remove(self.weapon[0])
                            break
                self.weapon.append(item_name)
                self.ui.change_text(f"Weapon equipped: {item_name}")
                return old_weapon_damage, weapon[1]
        return None

    def equip_armor(self, item_name):
        """
        Equips the selected armor for the player.

        Parameters
        ----------
        item_name : str
            The name of the armor to equip.

        Returns
        -------
        tuple or None
            A tuple containing the old armor value and the new armor value,
            or None if the armor could not be equipped.
        """
        old_armor_value = 0
        for armor in Library.ARMORS:
            if item_name == armor[0]:
                if len(self.armor) > 0:
                    for old_armor in Library.ARMORS:
                        if self.armor[0] == old_armor[0]:
                            old_armor_value = old_armor[1]
                            self.add_to_inv([self.armor[0], old_armor[1]], self.inventory)
                            self.armor.remove(self.armor[0])
                            break
                self.armor.append(item_name)
                self.ui.change_text(f"Armor equipped: {item_name}")
                return old_armor_value, armor[1]
        return None
