def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col, n):
    # Check column and diagonals
    for i in range(col):
        if board[row][i] == "Q":
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False
    return True

def solve_n_queens(board, col, n):
    if col >= n:
        return True
    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = "Q"  # Place queen
            if solve_n_queens(board, col + 1, n):
                return True
            board[row][col] = "."  # Backtrack
    return False

def n_queens(n):
    board = [["."] * n for _ in range(n)]
    board[0][0] = "Q"  # Place the first queen at (0, 0)
    if solve_n_queens(board, 1, n):  # Start solving from column 1
        print("Solution found:")
        print_board(board)
    else:
        print("No solution exists")

# Example usage
n = 5
n_queens(n)