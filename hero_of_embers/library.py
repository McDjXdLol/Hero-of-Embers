class Library:
    """
    A class that contains static data related to the game, such as weapons, armors,
    healing items, player classes, difficulties, and enemies.

    Attributes
    ----------
    WEAPONS : list of list of str, int, int, int
        A list of weapons where each weapon is represented by a name, the associated damage,
        the cost in game currency, and the shop drop weight (rarity).
    ARMORS : list of list of str, int, int, int
        A list of armors where each armor is represented by a name, the associated armor value,
        the cost in game currency, and the shop drop weight (rarity).
    HEAL_ITEMS : list of list of str, int, int, int
        A list of healing items where each item is represented by a name, the amount of health it heals,
        the cost in game currency, and the shop drop weight (rarity).
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

    # Weapons: name, damage, cost, drop weight
    WEAPONS = [
        ["Wooden Stick", 10, 15, 40],
        ["Stone Sword", 25, 50, 30],
        ["Iron Sword", 40, 90, 15],
        ["Gold Sword", 50, 130, 10],
        ["Eclipse", 70, 200, 4],
        ["Excalibur", 80, 300, 1]
    ]

    # Armors: name, armor, cost, drop weight
    ARMORS = [
        ["Clothes", 0, 0, 50],
        ["Wooden Armor", 10, 40, 35],
        ["Knight Armor", 40, 120, 15]
    ]

    # Healing items: name, heal amount, cost, drop weight
    HEAL_ITEMS = [
        ["Small Heart Elixir", 10, 15, 40],
        ["Medium Heart Elixir", 20, 30, 30],
        ["Big Heart Elixir", 45, 70, 15],
        ["Small Living Elixir", 60, 90, 10],
        ["Medium Living Elixir", 80, 120, 4],
        ["Big Living Elixir", 100, 150, 1]
    ]

    # Player classes: name, HP, armor, damage
    PLAYER_CLASSES = [
        ["The Protector (Tank)", 150, 50, 10],
        ["The Fighter (Balanced)", 100, 25, 15],
        ["The Avenger (Damager)", 70, 15, 30]
    ]

    # Difficulty levels: name, HP mod, armor mod, damage mod
    DIFFICULTIES = [
        ["Cushioned Path", 30, 10, 5],
        ["Twisted Road", 0, 0, 0],
        ["Iron Trial", -30, -10, -5]
    ]

    # Enemies: name, HP, armor, damage, XP, money
    ENEMIES = [
        ["Hungry Mugger", 20, 6, 8, 10, 24],
        ["Cult Initiate", 28, 8, 10, 15, 32],
        ["Cultist Priest", 40, 10, 14, 25, 44],
        ["Cultist Sorcerer", 55, 12, 18, 35, 59],
        ["Taren (High Priest)", 75, 18, 20, 60, 78],
        ["Shadow Dragon", 120, 25, 28, 100, 121]
    ]
