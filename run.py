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


def print_boards(player_board, computer_board, computer_guess):
    """
    Print the current state of both game boards and the computer's guess.

    Args:
        player_board: A list of lists representing the player's game board.
        computer_board: A list of lists representing the computer's game board.
        computer_guess: A tuple representing the computer's guess.

    Returns:
        None
    """
    print("Player board:")
    for row in player_board:
        print(" ".join(row))

    print("\nComputer board:")
    for i, row in enumerate(computer_board):
        if i == computer_guess[0]:
            row[computer_guess[1]] = "X"
        print(" ".join(row))


def play_game():
    """
    Play a game of Battleship.

    Returns:
        None
    """
    # initialize the game board
    player_board = initialize_board(5, 5)
    computer_board = initialize_board(5, 5)

    print("Let's play Battleship!")
 print_boards(player_board, computer_board, None)

 # randomly place the battleship
    ship_row = randint(0, len(computer_board) - 1)
    ship_col = randint(0, len(computer_board[0]) - 1)

    # allow the player and computer to take 4 turns
     for turn in range(4):
        print(f"\nTurn {turn + 1}")

        # player's turn
try:
    guess_row = int(input("Guess Row (0-4): "))
    guess_col = int(input("Guess Col (0-4): "))
    except ValueError:
         print("Please enter a valid integer.")
         continue