from scene_manager import SceneManager

class GameInit:
    def __init__(self, lang):
        self.scene_manager = SceneManager(lang)

    def get_game_title(self):
        return self.scene_manager.get_game_title()