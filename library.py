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
    ENEMIES = [["Wolf", 25, 10, 15, 20],
               ["Grizzly Bear", 35, 5, 20, 25],
               ["Skeleton", 30, 10, 20, 30],
               ["Goblin", 50, 20, 25, 40],
               ["Werewolf", 60, 20, 30, 50],
               ["Elf", 45, 10, 55, 55],
               ["Vampire", 65, 15, 45, 55],
               ["Minotaur", 70, 30, 40, 60],
               ["Cyclop", 70, 50, 40, 60],
               ["Giant Troll", 90, 60, 30, 65],
               ["Wyvern", 90, 50, 40, 80],
               ["Dragon", 150, 250, 50, 100]]
