class UI:
    def __init__(self):
        self.actually_showing_text = ""
        self.player_input = ""

    def change_text(self, to_what):
        self.actually_showing_text = to_what
        self.show_on_console()

    def show_on_console(self):
        if type(self.actually_showing_text) == list:
            for text_to_show in self.actually_showing_text:
                print(text_to_show)
        else:
            print(self.actually_showing_text)

    def get_input(self, nr_or_text, what_to_ask_for=""):
        if type(nr_or_text) == str:
            self.player_input = input(what_to_ask_for)
        elif type(nr_or_text) == int:
            try:
                self.player_input = int(input(what_to_ask_for))
            except ValueError:
                self.change_text("U have to enter the number! Try again.")
        return self.player_input
