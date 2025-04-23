class Library:
    """
    A class that contains static data related to the game, such as weapons, armors,
    healing items, player classes, difficulties, and enemies.

    Attributes
    ----------
    TRADE_QUOTES: list of str
        A list of quotes that trading guy uses.
    XP_NXT_LVL : list of int
        A list of experience nedded for each level.
    XP_NXT_LG_LVL: list of int
        A list of experience nedded for each legendary level.
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

    AFTER_SELL_QUOTES = [
        "Ah, fine craftsmanship! Shame to part with it. For you, I mean.",
        "I'll take it off your hands... for a fairish price.",
        "One adventurer’s trash is a merchant’s treasure.",
        "I’ve seen worse. Much worse. Sold worse too.",
        "This reeks of goblin blood. I like it.",
        "I’ll resell this in two towns over for triple. Pleasure doing business!",
        "You're sure you don't want to keep it? No? Great!",
        "Hmm. Slightly cursed, possibly haunted. I’ll take it!",
        "Does it come with a sob story? No? Even better.",
        "It’s not *worth* much, but I *like* you.",
        "Looks like it’s been through hell. Perfect!",
        "I hope it doesn’t bite. Again.",
        "Another piece of history I’ll pretend is rare.",
        "I’ll polish it and call it ‘legendary’.",
        "That’ll go straight to my 'mystery pile'.",
        "Good deal. For me, at least.",
    ]

    NO_PURCHASE_QUOTES = [
        "Browsin’ for fun, eh?",
        "Look with your eyes, not with your pockets?",
        "Next time, try bringing *money*.",
        "Was it something I said? Or everything I showed?",
        "Come back when your purse stops echoing.",
        "No coin, no crime. Yet.",
        "I feed my imps with these missed sales, you know.",
        "It’s fine. I’ll just starve in silence.",
        "Window shopping won’t save the realm.",
        "Tell your friends. Especially the rich ones.",
        "Don’t worry. I didn’t want to sell anything anyway.",
        "Did you just rob me of *hope*?",
        "Another customer with royal taste and peasant pockets.",
        "Leaving empty-handed... and hearted.",
        "At least my wares got some attention. Sniff.",
        "You sure you’re not cursed to be broke?",
    ]

    # Trade quotes
    TRADE_QUOTES = [
        "You're my last client. When you leave, I’ll disappear. At least for now.",
        "Gold talks, friend. But sometimes... silence is more expensive.",
        "Everything has a price. Even the things you never meant to sell.",
        "You don’t ask where I got it. I don’t ask what you’ll do with it.",
        "Buy or sell quickly... I’ve got other shadows to meet.",
        "My goods are rare, my time is rarer. Choose wisely.",
        "Even the gods used to bargain. Just not with me.",
        "One man’s trash is another demon’s artifact. Interested?",
        "If you're here for a blessing, you're in the wrong tent.",
        "Prices may rise. People may fall. That's trade for you.",
        "Today’s deal might save your life. Or end it. Fun, huh?",
        "The Hollow Hand never trades... but I do.",
        "Whispers told me you’d come. They also told me you’re broke.",
        "I once sold a soul by mistake. Still waiting for a refund.",
        "No refunds. No regrets. Only deals.",
        "A blade, a potion, a whisper... take your pick.",
    ]

    SELL_QUOTES = [
        "A fair trade... for me, at least.",
        "I’ll find a buyer. Or a summoner.",
        "Ah, excellent condition! Or was...",
        "Another piece of history in my hands.",
        "You won’t miss it... probably.",
        "I’m sure this won’t be cursed. Sure.",
        "One man’s regret is another’s profit.",
        "It practically screamed *sell me*.",
        "This? Oh, it’ll fetch a story or two.",
        "You just made someone's nightmare come true.",
        "A fine choice. I’ll triple the price later.",
        "What a shame to part with it... for you.",
        "You sell, I scheme. Everyone wins.",
        "Hope it wasn’t too important.",
        "This belonged to a hero once. Maybe.",
        "Perfect! I was missing just this piece... for the ritual.",
    ]

    # XP nedded to next level
    XP_NXT_LVL = [0, 50, 120, 210, 320, 450, 600, 770, 960, 1170, 1400]

    # XP nedded to next legendary level
    XP_NXT_LG_LVL = [2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000]

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
        ["Clothes", 1, 5, 50],
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
