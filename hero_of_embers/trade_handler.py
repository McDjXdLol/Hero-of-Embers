import random

from hero_of_embers.get_language_text import GetTexts
from hero_of_embers.library import Library


class TradeHandler:
    """
    Handles trading interactions between the player and the merchant.

    Provides functionality to buy and sell items, and manages communication
    with the user interface and the player's inventory.

    Attributes
    ----------
    ui : object
        The user interface handler used to display text and receive input.
    player : Player
        The player object involved in the trade.
    weapons : list
        List of available weapon items.
    armors : list
        List of available armor items.
    heal_items : list
        List of available healing items.
    """

    def __init__(self, ui, player):
        """
        Initializes the TradeHandler with UI and player objects.

        Parameters
        ----------
        ui : hero_of_emebrs.ui_manager.py
            Interface for text communication and input.
        player : Player
            The player engaging in trade.
        """
        self.ui = ui
        self.player = player
        self.weapons = Library.WEAPONS
        self.armors = Library.ARMORS
        self.heal_items = Library.HEAL_ITEMS

    def trade(self):
        """
        Opens the trading interface where the player can choose to buy or sell items.

        Displays a merchant's quote and prompts the player to select
        one of the available actions. Redirects to the appropriate buying or selling page.
        """
        self.ui.change_text(random.choice(Library.TRADE_QUOTES))
        self.ui.change_text(GetTexts.load_texts("trade_choose_action"))
        self.ui.change_text(GetTexts.load_texts("trade_buy"))
        self.ui.change_text(GetTexts.load_texts("trade_sell"))
        self.ui.change_text(GetTexts.load_texts("trade_exit"))
        selection = self.ui.get_input(0, "")
        match selection:
            case 1:
                self.buying_page()
                self.ui.change_text(random.choice(Library.SELL_QUOTES))
            case 2:
                self.selling_page()
                self.ui.change_text(random.choice(Library.AFTER_SELL_QUOTES))
            case 3:
                self.ui.change_text(random.choice(Library.NO_PURCHASE_QUOTES))
                return
            case _:
                self.ui.change_text(GetTexts.load_texts("trade_no_option"))

    def sell_item(self, item, price):
        """
        Sells an item from the player's inventory.

        Parameters
        ----------
        item : list
            The item to be sold. Format: [[name, dmg, cost, drop_weight], quantity]
        price : int
            The dragon coin amount received for selling the item.
        """
        name = item[0][0]
        if item in self.player.inventory.inventory:
            self.player.inventory.wallet += price
            self.player.inventory.remove_from_inv(name, self.player.inventory.inventory)
            self.ui.change_text(GetTexts.load_texts("trade_sold_item").format(name=name, price=price))
        else:
            self.ui.change_text(GetTexts.load_texts("trade_item_not_owned"))

    def buy(self, item):
        """
        Buys an item and adds it to the player's inventory.

        Parameters
        ----------
        item : list
            The item to buy, in the format [name, dmg, cost, drop_weight].
        """
        self.ui.change_text(GetTexts.load_texts("trade_bought_item").format(item=item))
        self.player.inventory.take_from_wallet(item[0][2])
        self.player.inventory.add_to_inv(item[0], self.player.inventory.inventory, 1)

    def selling_page(self):
        """
        Displays the selling interface where the player can sell items from their inventory.

        Shows each item with quantity and half of its purchase cost.
        Handles user input and processes the sale accordingly.
        """
        self.ui.change_text(GetTexts.load_texts("trade_what_to_sell"))
        inventory = self.player.inventory.inventory

        for idx, inv_item in enumerate(inventory):
            item_data = inv_item[0]
            quantity = inv_item[1]
            name = item_data[0]
            cost = item_data[2]
            price = cost // 2
            self.ui.change_text(GetTexts.load_texts("trade_enter_number_sell").format(idx=idx,quantity=quantity,name=name,price=price))

        self.ui.change_text("Enter the number of the item to sell or 0 to cancel:")

        choice = int(self.ui.get_input(0, ""))
        if choice == 0:
            return
        elif 0 < choice <= len(inventory):
            inv_item = inventory[choice - 1]
            item_data = inv_item[0]
            price = item_data[2] // 2
            self.sell_item(inv_item, price)
        else:
            self.ui.change_text(GetTexts.load_texts("trade_no_such_item"))

    def buying_page(self):
        """
        Displays the shop interface where the player can buy random items.

        Items are randomly selected from weapons, armors, and healing items
        based on their weight. The player can buy items if they have enough
        dragon coins, or exit the shop.

        Returns
        -------
        bool
            True if the player made a valid action, False if the input was invalid.
        """
        while True:
            random_weapon = random.choices(Library.WEAPONS, weights=[w[3] for w in Library.WEAPONS])
            self.ui.change_text(GetTexts.load_texts("trade_weapon_option").format(random_weapon=random_weapon))

            random_armor = random.choices(Library.ARMORS, weights=[a[3] for a in Library.ARMORS])
            self.ui.change_text(GetTexts.load_texts("trade_armor_option").format(random_armor=random_armor))

            random_heal_item = random.choices(Library.HEAL_ITEMS, weights=[h[3] for h in Library.HEAL_ITEMS])
            self.ui.change_text(GetTexts.load_texts("trade_heal_item_option").format(random_heal_item=random_heal_item))

            self.ui.change_text(GetTexts.load_texts("trade_exit_shop"))
            ina = self.ui.get_input(0, "")

            if ina > 0:
                match ina:
                    case 1:
                        if self.player.inventory.check_if_can_buy(random_weapon[0][2]):
                            self.buy(random_weapon)
                            return True
                        else:
                            self.ui.change_text(GetTexts.load_texts("trade_no_enough_coins"))
                            return False
                    case 2:
                        if self.player.inventory.check_if_can_buy(random_armor[0][2]):
                            self.buy(random_armor)
                            return True
                        else:
                            self.ui.change_text(GetTexts.load_texts("trade_no_enough_coins"))
                            return False
                    case 3:
                        if self.player.inventory.check_if_can_buy(random_heal_item[0][2]):
                            self.buy(random_heal_item)
                            return True
                        else:
                            self.ui.change_text(GetTexts.load_texts("trade_no_enough_coins"))
                            return False
                    case 4:
                        self.ui.change_text(random.choice(Library.NO_PURCHASE_QUOTES))
                        return True
                    case _:
                        self.ui.change_text(GetTexts.load_texts("trade_invalid_option"))
                        return False
            if ina < 5:
                return True
            else:
                self.ui.change_text(GetTexts.load_texts("trade_no_option_retry"))
