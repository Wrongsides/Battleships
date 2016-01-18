from battleships import *


class GameBoard:

    def __init__(self, size):
        self.board = []
        self.size = size
        for x in range(self.size):
            self.board.append(["O"] * self.size)

    def print_board(self):
        for row in self.board:
            print(" ".join(row))

    def random_row(self):
        return randint(0, len(self.board) - 1)

    def random_col(self):
        return randint(0, len(self.board[0]) - 1)

    def update_board(self, guess, value):
        self.board[guess.get("row")][guess.get("col")] = value