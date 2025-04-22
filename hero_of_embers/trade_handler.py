import random

from library import Library

class TradeHandler:
    def __init__(self, ui, player):
        self.ui = ui
        self.player = player
        self.weapons = Library.WEAPONS
        self.armors = Library.ARMORS
        self.heal_items = Library.HEAL_ITEMS

    def buy(self, item):
        self.ui.change_text(f"You bought: {item[0][3]}")
        self.player.inventory.take_from_wallet(item[0][3])
        self.player.inventory.add_to_inv(item[0], self.player.inventory.inventory, 1)

    def trade(self):
        self.ui.change_text("You're my last client. When you leave, I’ll disappear. At least for now")
        self.buying_page()

    def buying_page(self):
        while True:
            try:
                # Print random weapon
                random_weapon = random.choices(Library.WEAPONS, weights=[w[3] for w in Library.WEAPONS])
                self.ui.change_text(f"1. {random_weapon[0][0]} x{random_weapon[0][3]}Ɇ")
                # Print random armor
                random_armor = random.choices(Library.ARMORS, weights=[a[3] for a in Library.ARMORS])
                self.ui.change_text(f"2. {random_armor[0][0]} x{random_armor[0][3]}Ɇ")
                # Print random heal item
                random_heal_item = random.choices(Library.HEAL_ITEMS, weights=[h[3] for h in Library.HEAL_ITEMS])
                self.ui.change_text(f"3. {random_heal_item[0][0]} x{random_heal_item[0][3]}Ɇ")
                self.ui.change_text("4. Exit shop")
                ina = int(input())
                if ina > 0:
                    match ina:
                        case 1:
                            if self.player.inventory.check_if_can_buy(random_weapon[0][3]):
                                self.buy(random_weapon)
                                return True
                            else:
                                self.ui.change_text("You don't have enough dragon coins!")
                        case 2:
                            if self.player.inventory.check_if_can_buy(random_armor[0][3]):
                                self.buy(random_armor)
                                return True
                            else:
                                self.ui.change_text("You don't have enough dragon coins!")
                        case 3:
                            if self.player.inventory.check_if_can_buy(random_heal_item[0][3]):
                                self.buy(random_heal_item)
                                return True
                            else:
                                self.ui.change_text("You don't have enough dragon coins!")
                        case 4:
                            self.ui.change_text("Go now, before the Hollow Hand returns.")
                        case _:
                            self.ui.change_text("Are you trying to steal something! GO AWAY!")
                if ina < 5:
                    return True
                else:
                    self.ui.change_text("There is no such option! Try again!")
            except ValueError:
                self.ui.change_text("You have to enter the number!")

