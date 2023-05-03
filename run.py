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

        if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You sunk my battleship!")
            break

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

            if guess_row == ship_row and guess_col == ship_col:
                print("Congratulations! You sunk my battleship!")
                break
            else:
                if (guess_row < 0 or guess_row > 4) or\
                        (guess_col < 0 or guess_col > 4):
                    print("Oops, that's not even in the ocean.")
                elif player_board[guess_row][guess_col] == "X":
                    print("You guessed that one already.")
                else:
                    print("You missed my battleship!")
                    player_board[guess_row][guess_col] = "X"

            # computer's turn
            comp_guess_row = randint(0, len(computer_board) - 1)
            comp_guess_col = randint(0, len(computer_board[0]) - 1)

            if comp_guess_row == ship_row and comp_guess_col == ship_col:
                print("Oh no! The computer sunk your battleship!")
                break
            else:
                if player_board[comp_guess_row][comp_guess_col] == "X":
                    print("The computer guessed that one already.")
                else:
                    print("The computer missed")

            # print current state of the game boards
            print_boards(player_board,
                         computer_board,
                         (comp_guess_row, comp_guess_col))

        # check if the game is over
        if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You won the game!")
        else:
            print("Sorry, you lost the game.")

        # ask if the player wants to play again
        play_again = input("Do you want to play again? (Y/N) ").lower()
        if play_again == "n":
            break

    print("Thanks for playing Battleship!")


if __name__ == '__main__':
    play_game()
