from hero_of_embers.get_language_text import GetTexts

class Inventory:
    def __init__(self, ui, lang):
        """
        Initializes the inventory for the player.

        Parameters
        ----------
        ui : hero_of_embers.ui_manager.UI
            UI class object to interact with the user.
        """
        self.lang = lang
        self.ui = ui
        self.inventory = [[["Supreme Essence of Life" , "A", "elixir", 100, 100], 10], [["TEST-ELIXIR", "A", "elixir", 50, 50], 10]]
        self.damage_from_weapon = 0
        self.armor_from_armor = 0
        self.weapon = []
        self.armor = []
        self.wallet = 0

    def check_if_can_buy(self, amount):
        """
        Checks if the player has enough dragon coins to make a purchase.

        Parameters
        ----------
        amount : int
            The amount of dragon coins required for the purchase.

        Returns
        -------
        bool
            True if the player has enough dragon coins, False otherwise.
        """
        if self.wallet < amount:
            return False
        else:
            return True

    def take_from_wallet(self, amount):
        """
        Deducts the specified amount of dragon coins from the player's wallet.

        Parameters
        ----------
        amount : int
            The amount of dragon coins to deduct from the wallet.
        """
        if self.check_if_can_buy(amount):
            self.wallet -= amount
        else:
            self.ui.change_text(GetTexts.load_texts("inventory_not_enough_coins", self.lang))

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
        if len(inv) == 0:
            inv.append([item, amount])
        else:
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
        self.ui.change_text(GetTexts.load_texts("inventory_choose_equipment", self.lang).format(item_type=item_type))
        for i, item in enumerate(items):
            self.ui.change_text(GetTexts.load_texts("inventory_item_option", self.lang).format(i=i+1, item=item[0][0]))
        try:
            selected = int(self.ui.get_input(0, ""))
            if selected <= len(items):
                equip_function(items[selected - 1])
                self.remove_from_inv(items[selected - 1], self.inventory)
            else:
                self.ui.change_text(GetTexts.load_texts("inventory_no_option", self.lang))
        except ValueError:
            self.ui.change_text(GetTexts.load_texts("inventory_enter_number", self.lang))

    def show_inv(self):
        """
        Displays the player's inventory, including weapons, armors, and miscellaneous items.
        """

        inventory_weapons = []
        inventory_armors = []
        inventory_elixirs = []
        inventory_items = []
        if len(self.inventory) > 0:
            for item in self.inventory:
                item_type = item[0][2]

                if item_type == "weapon":
                    inventory_weapons.append(item)
                elif item_type == "armor":
                    inventory_armors.append(item)
                elif item_type == "elixir":
                    inventory_elixirs.append(item)
                elif item_type == "currency":
                    value = item[0][3]
                    self.wallet += value
                    self.inventory.remove(item)
                else:
                    inventory_items.append(item)



        if len(self.weapon) != 0:
            self.ui.change_text(GetTexts.load_texts("inventory_equipped_weapon", self.lang).format(weapon=""))
            self.ui.change_text(GetTexts.load_texts("inventory_item_name", self.lang).format(name=self.weapon[0][0]))
            self.ui.change_text(GetTexts.load_texts("inventory_item_damage", self.lang).format(damage=self.weapon[0][3]))
            self.ui.change_text(GetTexts.load_texts("inventory_item_value", self.lang).format(value=self.weapon[0][4]))

        if len(self.armor) != 0:
            self.ui.change_text(GetTexts.load_texts("inventory_equipped_armor", self.lang).format(armor=""))
            self.ui.change_text(GetTexts.load_texts("inventory_item_name", self.lang).format(name=self.armor[0][0]))
            self.ui.change_text(GetTexts.load_texts("inventory_item_armor", self.lang).format(damage=self.armor[0][3]))
            self.ui.change_text(GetTexts.load_texts("inventory_item_value", self.lang).format(value=self.armor[0][4]))
            self.ui.change_text(GetTexts.load_texts("inventory_item_amount", self.lang).format(amount=self.armor[1]))


        if self.wallet == 0:
            self.ui.change_text(GetTexts.load_texts("inventory_wallet_empty", self.lang))
        else:
            self.ui.change_text(GetTexts.load_texts("inventory_dragon_coins", self.lang).format(wallet=self.wallet))

        if len(self.inventory) == 0:
            self.ui.change_text(GetTexts.load_texts("inventory_inventory_empty", self.lang))
            return

        self.ui.change_text(GetTexts.load_texts("inventory_weapons", self.lang))
        for weapon in inventory_weapons:
            self.ui.change_text(GetTexts.load_texts("inventory_item_name", self.lang).format(name=weapon[0][0]))
            self.ui.change_text(GetTexts.load_texts("inventory_item_damage", self.lang).format(damage=weapon[0][3]))
            self.ui.change_text(GetTexts.load_texts("inventory_item_value", self.lang).format(value=weapon[0][4]))
            self.ui.change_text(GetTexts.load_texts("inventory_item_amount", self.lang).format(amount=weapon[1]))

        self.ui.change_text(GetTexts.load_texts("inventory_armors", self.lang))
        for armor in inventory_armors:
            self.ui.change_text(GetTexts.load_texts("inventory_item_name", self.lang).format(name=armor[0][0]))
            self.ui.change_text(GetTexts.load_texts("inventory_item_armor", self.lang).format(damage=armor[0][3]))
            self.ui.change_text(GetTexts.load_texts("inventory_item_value", self.lang).format(value=armor[0][4]))
            self.ui.change_text(GetTexts.load_texts("inventory_item_amount", self.lang).format(amount=armor[1]))

        self.ui.change_text(GetTexts.load_texts("inventory_miscellaneous", self.lang))
        for item in inventory_items:
            item_name = item[0][0]
            item_amount = item[1]
            self.ui.change_text(GetTexts.load_texts("inventory_misc_item", self.lang).format(item_name=item_name, item_amount=item_amount))

        if len(inventory_armors) > 0 or len(inventory_weapons) > 0:
            self.equip_selection(inventory_armors, inventory_weapons)

    def equip_selection(self, inventory_armors, inventory_weapons):
        """
        Allows the player to equip a selected item (weapon or armor).

        Parameters
        ----------
        inventory_armors : list
            List of available armor items in the inventory.
        inventory_weapons : list
            List of available weapon items in the inventory.
        """
        self.ui.change_text(GetTexts.load_texts("inventory_equip_one", self.lang))
        want = int(self.ui.get_input(0, ""))
        if want == 1:
            if len(inventory_armors) > 0 and len(inventory_weapons) > 0:
                self.ui.change_text(GetTexts.load_texts("inventory_equip_type", self.lang))
                which_to_equip = int(self.ui.get_input(0, ""))
                if which_to_equip == 1:
                    self.which_item_to_equip(inventory_weapons, self.equip_weapon, "weapon")
                elif which_to_equip == 2:
                    self.which_item_to_equip(inventory_armors, self.equip_armor, "armor")
                else:
                    self.ui.change_text(GetTexts.load_texts("inventory_no_option", self.lang))
            elif len(inventory_armors) > 0:
                self.which_item_to_equip(inventory_armors, self.equip_armor, "armor")
            elif len(inventory_weapons) > 0:
                self.which_item_to_equip(inventory_weapons, self.equip_weapon, "weapon")
        elif want == 2:
            return
        else:
            self.ui.change_text(GetTexts.load_texts("inventory_no_option", self.lang))

    def show_inv_elixirs(self):
        """
        Displays the player's elixirs inventory.

        Notes
        -----
        Each elixir is shown along with the amount.
        """
        for el in self.inventory:
            if el[0][2] == "elixir":
                self.ui.change_text(GetTexts.load_texts("inventory_misc_item", self.lang).format(el=el))

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
        for i, it in enumerate(inv):
            if it[0][0] == item_name:
                it[1] -= 1
                if it[1] <= 0:
                    inv.pop(i)
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

    def equip_weapon(self, item):
        """
        Equips the selected weapon for the player.

        Parameters
        ----------
        item : str
            The name of the weapon to equip.

        Returns
        -------
        tuple or None
            A tuple containing the old weapon's damage and the new weapon's damage,
            or None if the weapon could not be equipped.
        """
        self.damage_from_weapon = item[0][3]
        if len(self.weapon) > 0:
            self.weapon[0] = item[0]
        else:
            self.weapon.append(item[0])

        self.remove_from_inv(item[0][0], self.inventory)

        self.ui.change_text(GetTexts.load_texts("inventory_equipped_weapon", self.lang).format(weapon=item[0][0]))


    def equip_armor(self, item):
        """
        Equips the selected armor for the player.

        Parameters
        ----------
        item : str
            The name of the armor to equip.

        Returns
        -------
        tuple or None
            A tuple containing the old armor value and the new armor value,
            or None if the armor could not be equipped.
        """
        self.armor_from_armor = item[0][3]
        if len(self.armor) > 0:
            self.armor[0] = item[0]
        else:
            self.armor.append(item[0])

        self.remove_from_inv(item[0][0], self.inventory)
        self.ui.change_text(GetTexts.load_texts("inventory_equipped_armor", self.lang).format(armor=item[0][0]))

