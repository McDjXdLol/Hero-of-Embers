class Enemy:
    def __init__(self, name="Wolf", hp=100, armor=100, damage=15, experience=20):
        """
        Initializes the enemy with specified attributes.

        Parameters
        ----------
        name : str, optional
            Name of the enemy (default is "Wolf").
        hp : int, optional
            Health points of the enemy (default is 100).
        armor : int, optional
            Armor value of the enemy (default is 100).
        damage : int, optional
            Damage value of the enemy (default is 15).
        experience : int, optional
            Experience points dropped after the enemy is defeated (default is 20).

        Attributes
        ----------
        name : str
            Name of the enemy.
        hp : int
            Current health points of the enemy.
        armor : int
            Armor value of the enemy.
        damage : int
            Damage value of the enemy.
        experience : int
            Experience points dropped by the enemy.
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
        Deals damage to the enemy, considering armor and health.

        Parameters
        ----------
        amount : int
            Amount of damage to deal to the enemy.

        Returns
        -------
        bool
            True if the enemy is killed, False otherwise.
        """
        if self.armor >= amount:
            self.armor -= amount
        else:
            remaining_damage = amount - self.armor
            self.armor = 0
            self.hp -= remaining_damage

        if self.hp <= 0:
            return self.kill_enemy()

        return False

    def heal_hp(self, amount):
        """
        Heals the enemy by a specified amount.

        Parameters
        ----------
        amount : int
            Amount of health to heal.

        Notes
        -----
        If the healing amount exceeds the maximum health, the health will be set to the maximum value.
        """
        if self.hp + amount > self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp += amount

    def kill_enemy(self):
        """
        Kills the enemy by setting health and armor to 0.

        Returns
        -------
        bool
            True, indicating the enemy is dead.
        """
        self.hp = 0
        self.armor = 0
        self.dead = True
        return self.dead
