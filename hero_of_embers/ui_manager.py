from get_language_text import GetTexts


class UI:
    def __init__(self, lang):
        """
        Initialize the UI class to handle text display and user input.

        Attributes
        ----------
        lang : str
            The current language (code)
        """
        self.lang = lang
        self.actually_showing_text = ""
        self.player_input = ""

    def change_text(self, to_what):
        """
        Update the text displayed on the console UI.

        Parameters
        ----------
        to_what : str or list of str
            The text or list of texts to be displayed.
        """
        self.actually_showing_text = to_what
        self.show_on_console()

    def show_on_console(self):
        """
        Display the currently stored text on the console.

        Notes
        -----
        If the stored text is a list, each element is printed on a new line.
        If it's a single string, it's printed directly.
        """
        if isinstance(self.actually_showing_text, list):
            for text_to_show in self.actually_showing_text:
                print(text_to_show)
        else:
            print(self.actually_showing_text)

    def get_input(self, excepted_type, what_to_ask_for=""):
        """
        Prompt the user for input and return the result.

        Parameters
        ----------
        excepted_type : int or str
            Indicates the type of input expected:
            - If int, input should be a number.
            - If str, input can be any text.
        what_to_ask_for : str, optional
            The prompt message shown to the user (default is empty string).

        Returns
        -------
        str or int
            The user input. Returns `0` if an invalid number is entered when expecting an int.
        """
        if isinstance(excepted_type, str):
            self.player_input = input(what_to_ask_for)
        elif isinstance(excepted_type, int):
            while True:
                try:
                    self.player_input = int(input(what_to_ask_for))
                    break
                except ValueError:
                    self.player_input = 0
                    self.change_text(GetTexts.load_texts("ui_enter_number_try_again", self.lang))
        return self.player_input

    @staticmethod
    def clean_print(amount_of_lines):
        """
        Print multiple empty lines to the console for spacing.

        Parameters
        ----------
        amount_of_lines : int
            The number of empty lines to print.
        """
        for _ in range(amount_of_lines):
            print("\n")
