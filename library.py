class Library:
    """
    Class that has every information about classes, items etc.
    """
    # [Name, Amount of damage]
    WEAPONS = [["Wooden Stick", 10],
               ["Stone Sword", 25],
               ["Iron Sword", 40],
               ["Gold Sword", 50],
               ["Eclipse", 70],
               ["Excalibur", 80]]
    # [Name, Amount of Armor]
    ARMORS = [["Clothes", 0],
              ["Wooden Armor", 10],
              ["Knight Armor", 40]]
    #
    HEAL_ITEMS = [
        ["Small Heart Elixir", 10],
        ["Medium Heart Elixir", 20],
        ["Big Heart Elixir", 45],
        ["Small Living Elixir", 60],
        ["Medium Living Elixir", 80],
        ["Big Living Elixir", 100]
    ]
    # [Name, HP, Armor Value, Damage Value]
    PLAYER_CLASSES = [
        ["The Protector (Tank)", 150, 50, 10],
        ["The Fighter (Balanced)", 100, 25, 15],
        ["The Avenger (Damager)", 70, 15, 30]
    ]
    # [Name, HP, Armor, Damage]
    DIFFICULTIES = [
        ["Cushioned Path", 30, 10, 5],
        ["Twisted Road", 0, 0, 0],
        ["Iron Trial", -30, -10, -5]
    ]
    # [Name, HP, Armor, Damage, XP Drop]
    ENEMIES = [
        ["Hungry Mugger", 20, 6, 8, 10],
        ["Cult Initiate", 28, 8, 10, 15],
        ["Cultist Priest", 40, 10, 14, 25],
        ["Cultist Sorcerer", 55, 12, 18, 35],
        ["Taren (High Priest)", 75, 18, 20, 60],
        ["Shadow Dragon", 120, 25, 28, 100]
    ]
