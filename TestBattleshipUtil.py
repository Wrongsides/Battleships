from BattleshipUtil import create_board, print_board, random_row, random_col, get_input, update_board
import unittest
import re


class TestBattleshipUtil(unittest.TestCase):

    board = [['O','O','O','O','O'],['O','O','O','O','O'],['O','O','O','O','O'],['O','O','O','O','O'],['O','O','O','O','O']]

    def test_create_board(self):
        self.assertEqual(create_board(), self.board)

    def test_random_row(self):
        self.assertTrue(re.match('^[0-4]$', str(random_row(self.board))))

    def test_random_col(self):
        self.assertTrue(re.match('^[0-4]$', str(random_col(self.board))))

    def test_update_board(self):
        updated_board = [['X','O','O','O','O'],['O','O','O','O','O'],['O','O','O','O','O'],['O','O','O','O','O'],['O','O','O','O','O']]
        self.assertEqual(update_board({"row": 0, "col": 0}, self.board, "X"), updated_board)

    def test_print_board(self):
        pass

    def test_get_input(self):
        pass