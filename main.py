from player import Player
from library import Library
from selection import Selection
from plot_manager import PlotManager
from save_handler import SaveGame, LoadGame
from ui_manager import UI
import os


if __name__ == "__main__":
    ui = UI()
    if os.path.exists("savegame.json"):
        user = Player(name="", hp=0, armor=0,
                      damage=0, player_class=[], ui=ui)
        PLOT_MANAGER = PlotManager(user, ui)
        LoadGame(user, PLOT_MANAGER).load_data()
    else:
        SELECTION = Selection(ui)
        NICKNAME = SELECTION.give_nickname()
        CLASS_NR = SELECTION.class_select()
        CHARACTER_CLASS = Library().PLAYER_CLASSES[CLASS_NR]
        DIFFICULTY = SELECTION.give_difficulty_stats()
        user = Player(name=NICKNAME, hp=CHARACTER_CLASS[1] + DIFFICULTY[0], armor=CHARACTER_CLASS[2] + DIFFICULTY[1],
                      damage=CHARACTER_CLASS[3] + DIFFICULTY[2], player_class=Library.PLAYER_CLASSES[0], ui=ui)
        PLOT_MANAGER = PlotManager(user, ui)
    while PLOT_MANAGER.select_option():
        print("")
    if not user.dead:
        SaveGame(user, PLOT_MANAGER).save_game()
