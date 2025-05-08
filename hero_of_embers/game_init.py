from scene_manager import SceneManager

class GameInit:
    """
    Initializes the game and manages game-related data using the SceneManager.

    This class provides methods to retrieve game information, such as the game title,
    based on data managed by the SceneManager.

    Attributes
    ----------
    scene_manager : SceneManager
        An instance of the SceneManager class, used to access game data.
    """
    def __init__(self, lang):
        """
        Initializes the GameInit class with a SceneManager instance.

        Parameters
        ----------
        lang : str
            The language code (e.g., 'en', 'fr') to be used by the SceneManager.
        """
        self.scene_manager = SceneManager(lang)

    def get_game_title(self):
        """
        Retrieves the title of the game.

        This method fetches the game title from the SceneManager.

        Returns
        -------
        str
            The title of the game.
        """
        return self.scene_manager.get_game_title()
