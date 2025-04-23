class Entity:
    """
    A base class representing a generic entity with combat stats.

    This class is used as a foundation for characters like enemies and the player.
    It manages health, armor, damage, and alive/dead status.

    Attributes
    ----------
    name : str
        The name of the entity.
    hp : int
        The current hit points (health) of the entity.
    max_hp : int
        The maximum hit points of the entity.
    armor : int
        The current armor points of the entity.
    max_armor : int
        The maximum armor points of the entity.
    damage : int
        The amount of damage the entity can deal.
    dead : bool
        Flag indicating whether the entity is dead.
    """

    def __init__(self, name, hp, armor, damage):
        """
        Initializes an Entity with the given name, health, armor, and damage.

        Parameters
        ----------
        name : str
            The name of the entity.
        hp : int
            Initial and maximum hit points of the entity.
        armor : int
            Initial and maximum armor value of the entity.
        damage : int
            The damage value that the entity can deal.
        """
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.armor = armor
        self.max_armor = armor
        self.damage = damage
        self.dead = False

    def deal_damage(self, amount):
        """
        Applies incoming damage to the entity, reducing armor first, then HP.

        Parameters
        ----------
        amount : int
            The amount of damage to apply.

        Returns
        -------
        bool
            True if the entity is killed by this damage, otherwise False.
        """
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
        """
        Heals the entity's HP, not exceeding the maximum HP.

        Parameters
        ----------
        amount : int
            The amount of HP to restore.
        """
        self.hp = min(self.hp + amount, self.max_hp)

    def kill(self):
        """
        Instantly kills the entity by setting HP and armor to zero.

        Returns
        -------
        bool
            Always returns True, indicating the entity is now dead.
        """
        self.hp = 0
        self.armor = 0
        self.dead = True
        return self.dead
