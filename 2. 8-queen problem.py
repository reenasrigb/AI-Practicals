def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_queen(board, col):
    if col >= len(board):
        return True
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_queen(board, col + 1):
                return True
            board[i][col] = 0
    return False

def solve_8_queens():
    board = [[0 for _ in range(8)] for _ in range(8)]
    if not solve_queen(board, 0):
        print("No solution exists")
        return False
    print_board(board)
    return True

def print_board(board):
    for row in board:
        print(row)

solve_8_queens()
