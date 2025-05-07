import os

from library import Library
from player import Player
from plot_manager import PlotManager
from save_handler import SaveGame, LoadGame
from selection import Selection
from ui_manager import UI
from get_language_text import GetTexts

def main():
    """
    Main function that initializes the game, loads or creates a new save game,
    and handles the plot progression.

    This function checks if a save game exists. If it does, it loads the save data
    and continues the plot from where the user left off. If no save game is found,
    it prompts the user to select a character class and difficulty, and then starts
    a new game.

    Game flow:
    -----------
    1. Check if a save game exists.
    2. If save game exists, load the saved data.
    3. If no save game exists, prompt the user to create a new character.

    Returns
    -------
    None
    """
    GetTexts().get_texts()
    LANGUAGE = Selection(UI("en"), "en").select_language()
    ui = UI(LANGUAGE)

    # Load saved game data if it exists
    if os.path.exists("hero_of_embers/savegame.json"):
        user = Player(name="", hp=0, armor=0,
                      damage=0, player_class="", ui=ui, lang="en")
        PLOT_MANAGER = PlotManager(user, ui, "en")
        LoadGame(user, PLOT_MANAGER).load_data()
    else:
        # No saved game, start a new one
        SELECTION = Selection(ui, LANGUAGE)
        NICKNAME = SELECTION.give_nickname()
        CLASS_NR = SELECTION.class_select()
        CHARACTER_CLASS = Library().PLAYER_CLASSES[CLASS_NR]
        DIFFICULTY = SELECTION.give_difficulty_stats()

        # Create new player based on selection
        user = Player(name=NICKNAME, hp=CHARACTER_CLASS[1] + DIFFICULTY[0],
                      armor=CHARACTER_CLASS[2] + DIFFICULTY[1],
                      damage=CHARACTER_CLASS[3] + DIFFICULTY[2],
                      player_class=Library.PLAYER_CLASSES[0], ui=ui, lang=LANGUAGE)
        PLOT_MANAGER = PlotManager(user, ui, LANGUAGE)
    return PLOT_MANAGER.select_option()

if __name__ == "__main__":
    # Main game loop
    while main():
        print("")
