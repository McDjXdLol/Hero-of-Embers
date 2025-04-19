from hero_of_embers.library import Library


class Selection:
    def __init__(self, ui):
        """
        Selection class used for initializing game start procedures
        such as nickname input, class selection, and difficulty choice.

        Parameters
        ----------
        ui : hero_of_embers.ui_manager.UI
            UI class instance responsible for user interaction.
        """
        self.ui = ui

    def give_nickname(self):
        """
        Prompt the player to enter a nickname.

        Returns
        -------
        str
            The nickname entered by the player.
        """
        return self.ui.get_input("str", "Enter username: ")

    def class_select(self):
        """
        Prompt the player to select a class from available options.

        Returns
        -------
        int
            Index of the selected class in `Library.PLAYER_CLASSES`.
        """
        self.ui.change_text("Choose class:")
        for class_nr, classes in enumerate(Library.PLAYER_CLASSES):
            self.ui.change_text(f"{class_nr + 1}. {classes[0]}")
        while True:
            try:
                class_nr_input = self.ui.get_input(0, "")
                if class_nr_input > len(Library.PLAYER_CLASSES):
                    self.ui.change_text("The number is incorrect!")
                elif class_nr_input <= 0:
                    self.ui.change_text("The number is incorrect!")
                else:
                    break
            except ValueError:
                self.ui.change_text("You have to enter the number! Try again.")
        return class_nr_input - 1

    def difficulty_select(self):
        """
        Prompt the player to select a difficulty level.

        Returns
        -------
        int
            Index of the selected difficulty in `Library.DIFFICULTIES`.
        """
        self.ui.change_text("Choose difficulty:")
        for diff_nr, diff in enumerate(Library.DIFFICULTIES):
            self.ui.change_text(f"{diff_nr + 1}. {diff[0]}")
        while True:
            try:
                diff_nr_input = self.ui.get_input(0, "")
                if diff_nr_input > len(Library.DIFFICULTIES):
                    self.ui.change_text("The number is incorrect!")
                elif diff_nr_input <= 0:
                    self.ui.change_text("The number is incorrect!")
                else:
                    break
            except ValueError:
                self.ui.change_text("You have to enter the number! Try again.")
        return diff_nr_input - 1

    def give_difficulty_stats(self):
        """
        Get difficulty stats based on the player's chosen difficulty level.

        Returns
        -------
        list
            A list of stats corresponding to the selected difficulty level,
            excluding the name of the difficulty.
        """
        diff_nr = self.difficulty_select()
        difficulty_stats = []
        for stat_nr, stat in enumerate(Library.DIFFICULTIES[diff_nr]):
            if stat_nr == 0:
                pass
            else:
                difficulty_stats.append(stat)
        return difficulty_stats
