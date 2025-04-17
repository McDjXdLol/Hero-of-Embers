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
    PLAYER_CLASSES = [["Human", 100, 10, 10],
                      ["Orc", 125, 35, 10],
                      ["Goblin", 50, 10, 35]]
    # [Name, HP, Armor, Damage, XP Drop]
    ENEMIES = [
        ["Hungry Mugger", 20, 6, 8, 10],  # Pierwszy przeciwnik – testowy
        ["Cult Initiate", 28, 8, 10, 15],  # Początkujący kultysta, lekko groźniejszy
        ["Cultist Priest", 40, 10, 14, 25],  # Wspiera magią, średni poziom
        ["Cultist Sorcerer", 55, 12, 18, 35],  # Potężniejszy magiczny wróg
        ["Taren (High Priest)", 75, 18, 20, 60],  # Boss fabularny, zdradziecki mentor
        ["Shadow Dragon", 120, 25, 28, 100]  # Finalny boss – totalna maszyna śmierci
    ]
