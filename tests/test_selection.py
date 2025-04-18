import unittest
from unittest.mock import MagicMock
from hero_of_embers.library import Library
from hero_of_embers.selection import Selection

class TestSelection(unittest.TestCase):

    def setUp(self):
        self.ui_mock = MagicMock()
        self.selection = Selection(self.ui_mock)

    def test_give_nickname(self):
        self.ui_mock.get_input.return_value = "Hero"
        nickname = self.selection.give_nickname()
        self.assertEqual(nickname, "Hero")
        self.ui_mock.get_input.assert_called_with("str", "Enter username: ")

    def test_class_select(self):
        self.ui_mock.get_input.return_value = 1
        selected_class = self.selection.class_select()
        self.assertEqual(selected_class, 0)
        self.ui_mock.change_text.assert_any_call("Choose class:")
        self.ui_mock.change_text.assert_any_call("1. " + Library.PLAYER_CLASSES[0][0])

    def test_difficulty_select(self):
        self.ui_mock.get_input.return_value = 2
        selected_difficulty = self.selection.difficulty_select()
        self.assertEqual(selected_difficulty, 1)
        self.ui_mock.change_text.assert_any_call("Choose difficulty:")
        self.ui_mock.change_text.assert_any_call("2. " + Library.DIFFICULTIES[1][0])

    def test_give_difficulty_stats(self):
        self.ui_mock.get_input.return_value = 2
        difficulty_stats = self.selection.give_difficulty_stats()
        self.assertEqual(len(difficulty_stats), len(Library.DIFFICULTIES[1]) - 1)

if __name__ == '__main__':
    unittest.main()
