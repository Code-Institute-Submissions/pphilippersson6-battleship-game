from random import randint


def initialize_board(rows, cols):
    """
    Create and initialize a game board.

    Args:
        rows: The number of rows in the board.
        cols: The number of columns in the board.

    Returns:
        A list of lists representing the game board.
    """
    board = []
    for _ in range(rows):
        board.append(["O"] * cols)
    return board


def print_board(board):
    """
    Print the current state of the board.

    Args:
        board: A list of lists representing the game board.

    Returns:
        None
    """
    for row in board:
        print(" ".join(row))


def play_game():
    """
    Play a game of Battleship.

    Returns:
        None
    """
    # initialize the game board
    board = initialize_board(5, 5)

    print("Let's play Battleship!")
    print_board(board)

    # randomly place the battleship
    ship_row = randint(0, len(board) - 1)
    ship_col = randint(0, len(board[0]) - 1)

    # allow the player and the computer to take 4 turns to guess the battleship's location
    for turn in range(4):
        print(f"\nTurn {turn + 1}")

       # player's turn
        try:
            guess_row = int(input("Guess Row (0-4): "))
            guess_col = int(input("Guess Col (0-4): "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You sunk my battleship!")
            break
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print("Oops, that's not even in the ocean.")
            elif board[guess_row][guess_col] == "X":
                print("You guessed that one already.")
            else:
                print("You missed my battleship!")
                board[guess_row][guess_col] = "X"
                # computer's turn
            comp_guess_row = randint(0, len(board) - 1)
            comp_guess_col = randint(0, len(board[0]) - 1)

        if comp_guess_row == ship_row and comp_guess_col == ship_col:
            print("Oh no! The computer sunk your battleship!")
            break
        else:
            if board[comp_guess_row][comp_guess_col] == "X":
                print("The computer guessed that one already.")
            else:
                print("The computer missed your battleship!")
                board[comp_guess_row][comp_guess_col] = "X"

    if turn == 3:
        print("Game Over")

    print_board(board)


if __name__ == "__main__":
    play_game()
