from inventory import Inventory


class Player:
    """
    Class that got every information about player. Information like damage, hp, max hp etc.
    """

    def __init__(self, name="No Name", hp=100, player_class="Human", armor=0, damage=0):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_armor = armor
        self.armor = armor
        self.damage = damage
        self.player_class = player_class
        self.dead = False
        self.inventory = Inventory()
        self.level = 1
        self.experience = 0
        self.experience_to_next_level = [0, 50, 120, 210, 320, 450, 600, 770, 960, 1170, 1400]
        self.experience_to_legendary_level = [2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000]

    def deal_damage(self, amount):
        if (self.hp + self.armor) - amount <= 0:
            return self.kill_player()
        else:
            if self.armor - amount < 0:
                self.hp += self.armor - amount
                self.armor = 0
            else:
                self.armor -= amount
            return False

    def heal_hp(self, amount):
        if self.hp + amount > self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp += amount

    def kill_player(self):
        self.hp = 0
        self.armor = 0
        self.dead = True
        return self.dead

    def give_experience(self, amount):
        print(f"{self.name} gained {amount} xp!")
        if type(self.level) == int:
            if self.level < len(self.experience_to_next_level):
                if self.experience + amount > self.experience_to_next_level[self.level]:
                    self.experience = (self.experience + amount) - self.experience_to_next_level[self.level]
                    self.level += 1
                    print(f"{self.name} got next level!")
                    self.select_boost()
                else:
                    self.experience += amount
            elif self.level < len(self.experience_to_next_level) + len(self.experience_to_legendary_level):
                if self.experience + amount > self.experience_to_next_level[self.level-len(self.experience_to_next_level)-1]:
                    self.experience = (self.experience + amount) - self.experience_to_next_level[self.level-len(self.experience_to_next_level)-1]
                    self.level += 1
                    print(f"{self.name} got next level!")
                    self.select_legendary_boost()
                else:
                    self.experience += amount
            else:
                self.experience = "MAX"
                self.level = "MAX"
                print("You got the maximum level!")
        else:
            print("You already got the maximum level!")


    def select_legendary_boost(self):
        print("Select bonus: ")
        print("1. Damage +15")
        print("2. HP +30")
        print("3. Armor +15")
        while True:
            try:
                sel = int(input(""))
                if 1 > sel > 3:
                    print("The number is incorrect!")
                else:
                    print(f"You selected {sel}")
                    self.give_legendary_bonus(sel)
                    break
            except ValueError:
                print("You have to enter the number!")

    def select_boost(self):
        while True:
            print("Select bonus: ")
            print("1. Damage +5")
            print("2. HP +10")
            print("3. Armor +5")
            try:
                sel = int(input(""))
                if 1 <= sel <= 3:
                    print(f"You selected {sel}")
                    self.give_bonus(sel)
                    break
                else:
                    print("The number is incorrect! Try again!")
            except ValueError:
                print("You have to enter the number!")

    def give_legendary_bonus(self, sel):
        match sel:
            case 1:
                self.damage += 15
            case 2:
                self.max_hp += 30
                self.hp += 30
            case 3:
                self.armor += 15
                self.max_armor += 15

    def give_bonus(self, sel):
        match sel:
            case 1:
                self.damage += 5
            case 2:
                self.max_hp += 10
                self.hp += 10
            case 3:
                self.armor += 5
                self.max_armor += 5


if __name__ == "__main__":
    gracz = Player("name", 100, "Human", 100, 0)
    gracz.deal_damage(20)
    while type(gracz.level) == int :
        gracz.give_experience(50)
        if type(gracz.level) == int:
            try:
                xp = gracz.experience_to_next_level[gracz.level]
            except IndexError:
                xp = gracz.experience_to_legendary_level[gracz.level - len(gracz.experience_to_next_level) - 1]
        else:
            xp = gracz.level
        print(f"""
        Name: {gracz.name}
        MAX HP: {gracz.max_hp}
        HP: {gracz.hp}
        Armor: {gracz.armor}
        Damage: {gracz.damage}
        Class: {gracz.player_class}
        Player Dead: {gracz.dead}
        Inventory: {gracz.inventory.inventory}
        Level: {gracz.level}
        Experience: {gracz.experience}
        Experience to next level: {xp}
        """)