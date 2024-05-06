#!/usr/bin/python3

def print_board(board):
    """Print the tic-tac-toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Check if there is a winner."""
    for row in board:
        if row[0] != " " and all(cell == row[0] for cell in row):
            return True

    for col in range(len(board[0])):
        if board[0][col] != " " and all(board[row][col] == board[0][col] for row in range(len(board))):
            return True

    if board[0][0] != " " and all(board[i][i] == board[0][0] for i in range(len(board))):
        return True

    if board[0][2] != " " and all(board[i][2-i] == board[0][2] for i in range(len(board))):
        return True

    return False

def tic_tac_toe():
    """Play a game of tic-tac-toe."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if not (0 <= row < 3 and 0 <= col < 3):
                raise ValueError("Invalid row or column value. Please enter 0, 1, or 2.")
            if board[row][col] == " ":
                board[row][col] = player
                if check_winner(board):
                    print_board(board)
                    print("Player " + player + " wins!")
                    break
                if all(cell != " " for row in board for cell in row):
                    print_board(board)
                    print("It's a tie!")
                    break
                player = "O" if player == "X" else "X"
            else:
                print("That spot is already taken! Try again.")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    tic_tac_toe()
