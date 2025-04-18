from hero_of_embers.player import Player
from hero_of_embers.library import Library
from hero_of_embers.selection import Selection
from hero_of_embers.plot_manager import PlotManager
from hero_of_embers.save_handler import SaveGame, LoadGame
from hero_of_embers.ui_manager import UI
import os


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
    4. Progress through the plot options and save progress when the game ends.

    Returns
    -------
    None
    """
    ui = UI()

    # Load saved game data if it exists
    if os.path.exists("hero_of_embers/savegame.json"):
        user = Player(name="", hp=0, armor=0,
                      damage=0, player_class="", ui=ui)
        PLOT_MANAGER = PlotManager(user, ui)
        LoadGame(user, PLOT_MANAGER).load_data()
    else:
        # No saved game, start a new one
        SELECTION = Selection(ui)
        NICKNAME = SELECTION.give_nickname()
        CLASS_NR = SELECTION.class_select()
        CHARACTER_CLASS = Library().PLAYER_CLASSES[CLASS_NR]
        DIFFICULTY = SELECTION.give_difficulty_stats()

        # Create new player based on selection
        user = Player(name=NICKNAME, hp=CHARACTER_CLASS[1] + DIFFICULTY[0],
                      armor=CHARACTER_CLASS[2] + DIFFICULTY[1],
                      damage=CHARACTER_CLASS[3] + DIFFICULTY[2],
                      player_class=Library.PLAYER_CLASSES[0], ui=ui)
        PLOT_MANAGER = PlotManager(user, ui)

    # Main game loop where the player selects plot options
    while PLOT_MANAGER.select_option():
        print("")  # Placeholder for any additional output or actions in the loop

    # Save the game if the player is still alive
    if not user.dead:
        SaveGame(user, PLOT_MANAGER).save_game()


if __name__ == "__main__":
    main()