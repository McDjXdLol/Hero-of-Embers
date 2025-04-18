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
        if self.armor >= amount:
            # Jeśli armor jest większy lub równy obrażeniom, po prostu zmniejszamy armor
            self.armor -= amount
        else:
            # Jeśli armor nie wystarcza, wyczerpujemy armor, a reszta trafia do HP
            remaining_damage = amount - self.armor
            self.armor = 0  # Armor jest wyczerpany
            self.hp -= remaining_damage  # Reszta obrażeń trafia w HP

        # Jeśli po tym HP wroga spadło do 0 lub poniżej, wróg umiera
        if self.hp <= 0:
            return self.kill_enemy()

        return False

    def heal_hp(self, amount):
        if self.hp + amount > self.max_hp:
            self.hp = self.max_hp  # Jeśli leczenie przekroczy max_hp, ustawiamy hp na max_hp
        else:
            self.hp += amount  # Jeśli nie, po prostu dodajemy zdrowie

    def kill_enemy(self):
        self.hp = 0
        self.armor = 0
        self.dead = True
        return self.dead
