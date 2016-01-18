from battleships import *


class Controller:

    def __init__(self, game_board):
        self.game_board = game_board

    def check_int(self, string):
        if re.match('^\d+$', string):
            return True
        else:
            return False

    def get_input(self):
        while True:
            guess_row = input("Guess Row:")
            while not self.check_int(guess_row):
                print(guess_row + " is not a valid co-ordinate! Please enter 1 - 5")
                guess_row = input("Guess Row:")

            guess_col = input("Guess Col:")
            while not self.check_int(guess_col):
                print(guess_col + " is not a valid co-ordinate! Please enter 1 - 5")
                guess_col = input("Guess col:")

            guess = {"row": int(guess_row) - 1, "col": int(guess_col) - 1}

            if (guess.get("row") < 0 or guess.get("row") > 4) or (guess.get("col") < 0 or guess.get("col") > 4):
                print("Oops, that's not even in the ocean.")
            elif self.game_board.board[guess.get("row")][guess.get("col")] == "X":
                print("You guessed that one already.")
            else:
                break
        return guess
