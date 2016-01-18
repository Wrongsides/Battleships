from BattleshipUtil import create_board, print_board, random_row, random_col, get_input, update_board

print("Let's play Battleship!")

board = create_board()

print_board(board)

ship = {"row": random_row(board), "col": random_col(board)}

for turn in range(4):
    print("Turn", turn + 1)

    guess = get_input(board)

    if guess.get("row") == ship.get("row") and guess.get("col") == ship.get("col"):
        print("Congratulations! You sunk my battleship!")
        break
    else:
        print("You missed my battleship!")
        board = update_board(guess, board, "X")
        print_board(board)
    if turn == 3:
        print("Game Over")
    turn += 1