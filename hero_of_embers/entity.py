class Entity:
    def __init__(self, name, hp, armor, damage):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.armor = armor
        self.max_armor = armor
        self.damage = damage
        self.dead = False

    def deal_damage(self, amount):
        if self.armor >= amount:
            self.armor -= amount
        else:
            remaining_damage = amount - self.armor
            self.armor = 0
            self.hp -= remaining_damage

        if self.hp <= 0:
            return self.kill()
        return False

    def heal_hp(self, amount):
        self.hp = min(self.hp + amount, self.max_hp)

    def kill(self):
        self.hp = 0
        self.armor = 0
        self.dead = True
        return self.dead
