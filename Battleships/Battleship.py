from battleships.GameBoard import GameBoard
from battleships.Controller import Controller

print("Let's play Battleship!")

board = GameBoard(5)
control = Controller(board)

board.print_board()

ship = {"row": board.random_row(), "col": board.random_col()}

for turn in range(4):
    print("Turn", turn + 1)

    guess = control.get_input()

    if guess.get("row") == ship.get("row") and guess.get("col") == ship.get("col"):
        print("Congratulations! You sunk my battleship!")
        break
    else:
        print("You missed my battleship!")
        board.update_board(guess, "X")
        board.print_board()
    if turn == 3:
        print("Game Over")
    turn += 1