from battleships.Controller import Controller
from battleships.GameBoard import GameBoard
import unittest


class TestController(unittest.TestCase):

    board = GameBoard(5)
    controller = Controller(board)

    def test_is_int(self):
        self.assertFalse(self.controller.check_int("hello"))
        self.assertTrue(self.controller.check_int("3"))

    def test_get_input(self):
        pass