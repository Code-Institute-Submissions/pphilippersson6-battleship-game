"""
Battleship Game

This is a simple game of the classic battleship!
"""

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
        if computer_guess is not None and i == computer_guess[0]:
            row[computer_guess[1]] = "X"
        print(" ".join(row))


def play_game():
    """
    Play a game of Battleship.

    Returns:
        None
    """
    # prompt the player to enter the number of rows and columns
    while True:
        try:
            rows = int(input("How many rows do you want to play? (1-10): "))
            cols = int(input("How many columns do you want to play? (1-10): "))
            if rows < 1 or rows > 10 or cols < 1 or cols > 10:
                print("Please enter values between 1 and 10.")
                continue
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

    # initialize the game board
    player_board = initialize_board(rows, cols)
    computer_board = initialize_board(rows, cols)

    # randomly place the battleship
    ship_row = randint(0, len(computer_board) - 1)
    ship_col = randint(0, len(computer_board[0]) - 1)

    print("Let's play Battleship!")
    print_boards(player_board, computer_board, None)

    # allow the player and computer to take 4 turns
    for turn in range(4):
        print(f"\nTurn {turn + 1}")

        # player's turn
        while True:
            try:
                guess_row = int(input(f"Guess Row (0-{rows - 1}): "))
                if guess_row < 0 or guess_row > rows - 1:
                    print(f"Please enter Row from (0-{rows - 1})")
                    continue
                guessc = int(input(f"Guess Col (0-{cols - 1}): "))

                if guessc < 0 or guessc > cols - 1:
                    while True:
                        print(f"Please enter Col from (0-{cols - 1})")
                        guessc = int(input(f"Guess Col (0-{cols - 1}): "))
                        if guessc < 0 or guessc > cols - 1:
                            continue
                        else:
                            break

                if player_board[guess_row][guessc] == "X":
                    print("You guessed that one already. Please try again.")
                    continue
                else:
                    break
            except ValueError:
                print(f"Please enter a number from 0-{rows - 1}.")
                continue

        if guess_row == ship_row and guessc == ship_col:
            print("Congratulations! You sunk my battleship!")
            break
        else:
            if (guess_row < 0 or guess_row > rows - 1) or (
                guessc < 0 or guessc > cols - 1
            ):
                print("Oops, that's not even in the ocean.")
            else:
                print("You missed my battleship!")
                player_board[guess_row][guessc] = "X"

        # computer's turn
        comp_guess_row = randint(0, len(computer_board) - 1)
        cguess = randint(0, len(computer_board[0]) - 1)

        if comp_guess_row == ship_row and cguess == ship_col:
            print("Oh no! The computer sunk your battleship!")
            break
        else:
            if player_board[comp_guess_row][cguess] == "X":
                print("The computer guessed that one already.")
            else:
                print("The computer missed")
                player_board[comp_guess_row][cguess] = "X"

        # print current state of the game boards
        print_boards(player_board, computer_board, (comp_guess_row, cguess))

    # check if the game is over
    if guess_row == ship_row and guessc == ship_col:
        print("Congratulations! You win!")
    else:
        print("Sorry, you lose. Better luck next time!")


def play():
    """
    Play Battleship until the player quits.

    Returns:
        None
    """
    while True:
        play_game()
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == "n":
            break
    print("Thanks for playing Battleship!")


if __name__ == "__main__":
    play()
