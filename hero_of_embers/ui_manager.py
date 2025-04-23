class UI:
    def __init__(self):
        """
        Initializes the UI class to handle text display and user input.
        """
        self.actually_showing_text = ""
        self.player_input = ""

    def change_text(self, to_what):
        """
        Updates the text displayed on the UI.

        Parameters
        ----------
        to_what : str or list of str
            The text or list of texts to be displayed on the console.
        """
        self.actually_showing_text = to_what
        self.show_on_console()

    def show_on_console(self):
        """
        Displays the current text on the console. If the text is a list, it prints each item.

        Notes
        -----
        The method checks if the text to display is a list or a single string.
        """
        if type(self.actually_showing_text) == list:
            for text_to_show in self.actually_showing_text:
                print(text_to_show)
        else:
            print(self.actually_showing_text)

    def get_input(self, nr_or_text, what_to_ask_for=""):
        """
        Prompts the user for input and returns the input value.

        Parameters
        ----------
        nr_or_text : int or str
            The type of input expected. If int, the user is expected to enter a number.
            If str, a general text input is expected.
        what_to_ask_for : str, optional
            The prompt message shown to the user (default is an empty string).

        Returns
        -------
        str or int
            The user input. If the input is invalid when expecting a number, "invalid" is returned.
        """
        if type(nr_or_text) == str:
            self.player_input = input(what_to_ask_for)
        elif type(nr_or_text) == int:
            try:
                self.player_input = int(input(what_to_ask_for))
            except ValueError:
                self.player_input = "invalid"  # Handle invalid number input
                self.change_text("U have to enter the number! Try again.")
        return self.player_input

    @staticmethod
    def clean_print(amount_of_lines):
        for x in range(0, amount_of_lines):
            print("\n")