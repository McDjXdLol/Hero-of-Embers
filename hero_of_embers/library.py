class Library:
    """
    A class that contains static data related to the game, such as weapons, armors,
    healing items, player classes, difficulties, and enemies.

    Attributes
    ----------
    WEAPONS : list of list of str, int
        A list of weapons where each weapon is represented by a name and the associated damage.
    ARMORS : list of list of str, int
        A list of armors where each armor is represented by a name and the associated armor value.
    HEAL_ITEMS : list of list of str, int
        A list of healing items where each item is represented by a name and the amount of health it heals.
    PLAYER_CLASSES : list of list of str, int
        A list of player classes, where each class is represented by a name, health points (HP), armor value,
        and damage value.
    DIFFICULTIES : list of list of str, int
        A list of difficulty levels, where each level is represented by a name, HP adjustment, armor value,
        and damage adjustment.
    ENEMIES : list of list of str, int
        A list of enemies, where each enemy is represented by a name, HP, armor, damage, and XP drop upon defeat.
    """

    # Weapons with their damage values
    WEAPONS = [
        ["Wooden Stick", 10],
        ["Stone Sword", 25],
        ["Iron Sword", 40],
        ["Gold Sword", 50],
        ["Eclipse", 70],
        ["Excalibur", 80]
    ]

    # Armors with their armor values
    ARMORS = [
        ["Clothes", 0],
        ["Wooden Armor", 10],
        ["Knight Armor", 40]
    ]

    # Healing items with the amount of health they restore
    HEAL_ITEMS = [
        ["Small Heart Elixir", 10],
        ["Medium Heart Elixir", 20],
        ["Big Heart Elixir", 45],
        ["Small Living Elixir", 60],
        ["Medium Living Elixir", 80],
        ["Big Living Elixir", 100]
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

    # Enemies with their HP, armor, damage, and XP drop values
    ENEMIES = [
        ["Hungry Mugger", 20, 6, 8, 10],
        ["Cult Initiate", 28, 8, 10, 15],
        ["Cultist Priest", 40, 10, 14, 25],
        ["Cultist Sorcerer", 55, 12, 18, 35],
        ["Taren (High Priest)", 75, 18, 20, 60],
        ["Shadow Dragon", 120, 25, 28, 100]
    ]
