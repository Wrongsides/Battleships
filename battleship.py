from random import randint


def create_board():
    board = []
    for x in range(5):
        board.append(["O"] * 5)
    return board


def print_board(board):
    for row in board:
        print(" ".join(row))


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


def is_int(string):
    if string is None:
        string = ""
    try:
        int(string)
        return True
    except ValueError:
        return False


def get_input(board):
    while True:
        guess_row = input("Guess Row:")
        while not is_int(guess_row):
            print(guess_row + " is not a valid co-ordinate! Please enter 1 - 5")
            guess_row = input("Guess Row:")

        guess_col = input("Guess Col:")
        while not is_int(guess_col):
            print(guess_col + " is not a valid co-ordinate! Please enter 1 - 5")
            guess_col = input("Guess col:")

        guess = {"row": int(guess_row) - 1, "col": int(guess_col) - 1}

        if (guess.get("row") < 0 or guess.get("row") > 4) or (guess.get("col") < 0 or guess.get("col") > 4):
            print("Oops, that's not even in the ocean.")
        elif board[guess.get("row")][guess.get("col")] == "X":
            print("You guessed that one already.")
        else:
            break
    return guess


print("Let's play Battleship!")
board = create_board()
print_board(board)
ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
    print("Turn", turn + 1)

    guess = get_input(board)

    if guess.get("row") == ship_row and guess.get("col") == ship_col:
        print("Congratulations! You sunk my battleship!")
        break
    else:
        print("You missed my battleship!")
        board[guess.get("row")][guess.get("col")] = "X"
        print_board(board)
    if turn == 3:
        print("Game Over")
    turn += 1
