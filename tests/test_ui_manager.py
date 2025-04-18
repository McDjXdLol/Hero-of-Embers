import unittest
from unittest.mock import patch
from hero_of_embers.ui_manager import UI

class TestUI(unittest.TestCase):

    def setUp(self):
        self.ui = UI()

    def test_change_text(self):
        self.ui.change_text("Test text")
        self.assertEqual(self.ui.actually_showing_text, "Test text")

    @patch('builtins.print')
    def test_show_on_console(self, mock_print):
        self.ui.change_text("Hello World!")
        self.ui.show_on_console()
        mock_print.assert_called_with("Hello World!")

    @patch('builtins.input', return_value="123")
    def test_get_input_number(self, mock_input):
        result = self.ui.get_input(0, "Enter a number: ")
        self.assertEqual(result, 123)
        mock_input.assert_called_with("Enter a number: ")

    @patch('builtins.input', return_value="invalid")
    def test_get_input_invalid_number(self, mock_input):
        result = self.ui.get_input(0, "Enter a number: ")
        self.assertEqual(result, "invalid")
        self.assertEqual(self.ui.actually_showing_text, "U have to enter the number! Try again.")

    @patch('builtins.input', return_value="TestPlayer")
    def test_get_input_string(self, mock_input):
        result = self.ui.get_input("str", "Enter username: ")
        self.assertEqual(result, "TestPlayer")
        mock_input.assert_called_with("Enter username: ")

if __name__ == '__main__':
    unittest.main()
