class Enemy:
    """
    Class that is used to create enemy
    """
    def __init__(self, name="Wolf", hp=100, armor=100, damage=15, experience=20):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.armor = armor
        self.damage = damage
        self.dead = False
        self.experience_drop = experience

    def deal_damage(self, amount):
        if (self.hp + self.armor) - amount <= 0:
            return self.kill_enemy()
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

    def kill_enemy(self):
        self.hp = 0
        self.armor = 0
        self.dead = True
        return self.dead