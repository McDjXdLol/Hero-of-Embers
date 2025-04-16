from player import Player
from library import Library
from selection import Selection
from plot_manager import PlotManager

if __name__ == "__main__":
    NICKNAME = Selection.giveNickname()
    CLASS_NR = Selection.ClassSelect()
    CHARACTER_CLASS = Library().PLAYER_CLASSES[CLASS_NR]
    user = Player(name=NICKNAME, hp=CHARACTER_CLASS[1]*5, armor=CHARACTER_CLASS[2], damage=CHARACTER_CLASS[3], player_class=Library.PLAYER_CLASSES[0])
    PLOT_MAGNAGER = PlotManager(user)
    while PLOT_MAGNAGER.select_option():
        print("")

