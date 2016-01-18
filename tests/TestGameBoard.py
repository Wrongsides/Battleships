from battleships import *
from battleships.GameBoard import GameBoard
import unittest


class TestGameBoard(unittest.TestCase):

    board_5_by_5 = [['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]
    game_board = GameBoard(5)

    def test_create_board(self):
        self.assertEqual(self.game_board.board, self.board_5_by_5)

    def test_random_row(self):
        self.assertTrue(re.match('^[0-4]$', str(self.game_board.random_row())))

    def test_random_col(self):
        self.assertTrue(re.match('^[0-4]$', str(self.game_board.random_col())))

    def test_update_board(self):
        updated_board = [['X', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]
        self.game_board.update_board({"row": 0, "col": 0}, "X")
        self.assertEqual(self.game_board.board, updated_board)

    def test_print_board(self):
        pass
