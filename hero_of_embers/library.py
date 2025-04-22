class Library:
    """
    A class that contains static data related to the game, such as weapons, armors,
    healing items, player classes, difficulties, and enemies.

    Attributes
    ----------
    WEAPONS : list of list of str, int, int
        A list of weapons where each weapon is represented by a name, the associated damage,
        and the cost in game currency.
    ARMORS : list of list of str, int, int
        A list of armors where each armor is represented by a name, the associated armor value,
        and the cost in game currency.
    HEAL_ITEMS : list of list of str, int, int
        A list of healing items where each item is represented by a name, the amount of health it heals,
        and the cost in game currency.
    PLAYER_CLASSES : list of list of str, int, int, int
        A list of player classes, where each class is represented by a name, health points (HP), armor value,
        and damage value.
    DIFFICULTIES : list of list of str, int, int, int
        A list of difficulty levels, where each level is represented by a name, HP adjustment, armor value,
        and damage adjustment.
    ENEMIES : list of list of str, int, int, int, int, int
        A list of enemies, where each enemy is represented by a name, HP, armor, damage, XP drop upon defeat,
        and the amount of money dropped upon defeat.
    """

    # Weapons with their damage values, and cost
    WEAPONS = [
        ["Wooden Stick", 10, 15],
        ["Stone Sword", 25, 50],
        ["Iron Sword", 40, 90],
        ["Gold Sword", 50, 130],
        ["Eclipse", 70, 200],
        ["Excalibur", 80, 300]
    ]

    # Armors with their armor values, and cost
    ARMORS = [
        ["Clothes", 0, 0],
        ["Wooden Armor", 10, 40],
        ["Knight Armor", 40, 120]
    ]

    # Healing items with the amount of health they restore, and cost
    HEAL_ITEMS = [
        ["Small Heart Elixir", 10, 15],
        ["Medium Heart Elixir", 20, 30],
        ["Big Heart Elixir", 45, 70],
        ["Small Living Elixir", 60, 90],
        ["Medium Living Elixir", 80, 120],
        ["Big Living Elixir", 100, 150]
    ]

    # Player classes with their HP, armor, and damage values
    PLAYER_CLASSES = [
        ["The Protector (Tank)", 150, 50, 10],
        ["The Fighter (Balanced)", 100, 25, 15],
        ["The Avenger (Damager)", 70, 15, 30]
    ]

    # Difficulty levels with their HP, armor, and damage modifiers
    DIFFICULTIES = [
        ["Cushioned Path", 30, 10, 5],
        ["Twisted Road", 0, 0, 0],
        ["Iron Trial", -30, -10, -5]
    ]

    # Enemies with their HP, armor, damage, XP drop values, and money drop
    ENEMIES = [
        ["Hungry Mugger", 20, 6, 8, 10, 24],
        ["Cult Initiate", 28, 8, 10, 15, 32],
        ["Cultist Priest", 40, 10, 14, 25, 44],
        ["Cultist Sorcerer", 55, 12, 18, 35, 59],
        ["Taren (High Priest)", 75, 18, 20, 60, 78],
        ["Shadow Dragon", 120, 25, 28, 100, 121]
    ]