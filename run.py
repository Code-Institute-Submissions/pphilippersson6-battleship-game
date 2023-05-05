"""
Battleship Game

This is a simple game of the classic battleship!
"""
from random import randint


def initialize_board(rows, cols):
    """
    Initialize an empty battleship board with 'O' for each cell.

    Args:
    rows (int): Number of rows in the board.
    cols (int): Number of columns in the board.

    Returns:
    list: A 2D list representing the empty battleship board.
    """
    board = []
    for _ in range(rows):
        board.append(["O"] * cols)
    return board


def print_boards(player_board, computer_board, computer_guess):
    """
    Prints the player and computer board with with computer's latest guess.

    Args:
    player_board (list): list representing the player's board.
    computer_board (list): list representing the computer's board.
    computer_guess (tuple): A tuple showing the computer's latest guess.
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
    Runs a single game of Battleship.

    Returns:
    None
    """
    while True:
        try:
            rows = int(input("Enter the number of rows (1-10): "))
            cols = int(input("Enter the number of columns (1-10): "))
            if rows < 1 or rows > 10 or cols < 1 or cols > 10:
                print("Please enter values between 1 and 10.")
                continue

            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

    player_board = initialize_board(rows, cols)
    computer_board = initialize_board(rows, cols)
    ship_row = randint(0, len(computer_board) - 1)
    ship_col = randint(0, len(computer_board[0]) - 1)

    print("Let's play Battleship!")
    print_boards(player_board, computer_board, None)

    while True:
        for turn in range(1, 100):
            print(f"\nTurn {turn}")
            while True:
                try:
                    guess_row = int(input(f"Guess Row (0-{rows - 1}): "))
                    if guess_row < 0 or guess_row > rows - 1:
                        print(f"Please enter Row from (0-{rows - 1})")
                        continue
                    guess_col = int(input(f"Guess Col (0-{cols - 1}): "))
                    if guess_col < 0 or guess_col > cols - 1:
                        print(f"Please enter Col from (0-{cols - 1})")
                        continue
                    if player_board[guess_row][guess_col] == "X":
                        print("You guessed that one already. Try again.")
                        continue
                    else:
                        break
                except ValueError:
                    print(f"Please enter a number from 0-{rows - 1}.")

            if guess_row == ship_row and guess_col == ship_col:
                print("Congratulations! You sunk the computer's battleship!")
                break
            else:
                if (guess_row < 0 or guess_row > rows - 1) or (
                    guess_col < 0 or guess_col > cols - 1
                ):
                    print("Oops, that's not even in the ocean.")
                else:
                    print("You missed the computer's battleship!")
                    player_board[guess_row][guess_col] = "X"

            while True:
                comp_guess_row = randint(0, len(computer_board) - 1)
                comp_guess_col = randint(0, len(computer_board[0]) - 1)
                if computer_board[comp_guess_row][comp_guess_col] == "X":
                    continue
                else:
                    break

            if comp_guess_row == ship_row and comp_guess_col == ship_col:
                print("Oh no! The computer sunk your battleship!")
                break
            else:
                if player_board[comp_guess_row][comp_guess_col] == "X":
                    print("The computer guessed that one already.")
                else:
                    print("The computer missed.")
                    player_board[comp_guess_row][comp_guess_col] = "X"
                print_boards(
                    player_board, computer_board,
                    (comp_guess_row, comp_guess_col)
                )

        if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You win!")
            break
        else:
            print("Sorry, you lose. Better luck next time!")
            break


def play():
    """
    Lets you play one more time or quit the game

    Y = play again
    N = quit
    """
    while True:
        play_game()
        while True:
            play_again = input("Do you want to play again? (Y/N): ")
            if play_again.upper() == "Y":
                break
            elif play_again.upper() == "N":
                print("Thanks for playing Battleship!")
                return
            else:
                print("Invalid input. Please enter Y or N.")


if __name__ == "__main__":
    play()
