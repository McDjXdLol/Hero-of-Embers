from player import Player
from library import Library
from selection import Selection
from plot_manager import PlotManager
from save_handler import SaveGame, LoadGame

if __name__ == "__main__":
    NICKNAME = Selection.give_nickname()
    CLASS_NR = Selection.class_select()
    CHARACTER_CLASS = Library().PLAYER_CLASSES[CLASS_NR]
    DIFFICULTY = Selection().give_difficulty_stats()
    user = Player(name=NICKNAME, hp=CHARACTER_CLASS[1]+DIFFICULTY[0], armor=CHARACTER_CLASS[2]+DIFFICULTY[1], damage=CHARACTER_CLASS[3]+DIFFICULTY[2], player_class=Library.PLAYER_CLASSES[0])

    PLOT_MANAGER = PlotManager(user)
    while PLOT_MANAGER.select_option():
        print("")
    SaveGame(user, PLOT_MANAGER).save_game()
