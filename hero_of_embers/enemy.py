class Enemy:
    def __init__(self, name="Wolf", hp=100, armor=100, damage=15, experience=20):
        """
        Class that handles enemy information.
        :param name: name of enemy
        :param hp: amount of hp
        :param armor: amount of armor
        :param damage: amount of damage
        :param experience: amount of experience that enemy drop after killing him
        :type name: str
        :type hp: int
        :type armor: int
        :type damage: int
        :type experience: int
        """
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.armor = armor
        self.damage = damage
        self.dead = False
        self.experience_drop = experience

    def deal_damage(self, amount):
        """
        Function that is used to deal enemy damage
        :param amount: amount of damage to deal
        :type amount: int
        """
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
        """
        Function that is used to heal enemy
        :param amount: amount of heal
        :type amount: int
        """
        if self.hp + amount > self.max_hp:
            self.hp = self.max_hp  # Jeśli leczenie przekroczy max_hp, ustawiamy hp na max_hp
        else:
            self.hp += amount  # Jeśli nie, po prostu dodajemy zdrowie

    def kill_enemy(self):
        """
        Function that is used to kill enemy
        """
        self.hp = 0
        self.armor = 0
        self.dead = True
        return self.dead
