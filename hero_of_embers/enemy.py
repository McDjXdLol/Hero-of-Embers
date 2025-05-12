from entity import Entity

class Enemy(Entity):
    """
    Represents an enemy entity in the game, inheriting from Entity.

    This class adds experience and money drops to the base Entity class,
    which are granted to the player upon defeating the enemy.

    Attributes
    ----------
    experience_drop : int
        The amount of experience points the enemy drops when defeated.
    """

    def __init__(self, name="Wolf", hp=100, armor=100, damage=15, experience=20):
        """
        Initializes an Enemy instance with specific stats and rewards.

        Parameters
        ----------
        name : str, optional
            The name of the enemy (default is "Wolf").
        hp : int, optional
            The hit points of the enemy (default is 100).
        armor : int, optional
            The armor value of the enemy, reducing incoming damage (default is 100).
        damage : int, optional
            The amount of damage the enemy can inflict (default is 15).
        experience : int, optional
            The experience points granted to the player upon defeat (default is 20).
        """
        super().__init__(name, hp, armor, damage)
        self.experience_drop = experience
