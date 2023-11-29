#!/usr/bin/python3
""" Contains a function that solves the nqueen problem. """


def printBoard(board):
    """ Prints the position of the n queens on the board. """
    res = []
    for a, row in enumerate(board):
        for x, y in enumerate(row):
            if y == 1:
                pos = []
                pos.append(a)
                pos.append(x)
                res.append(pos)
    print(res)


def isPosSafe(board, c, y, n):
    """ Checks if a position on the board is safe. """

    """Check the left side of this pos for queens. """
    for x in range(y):
        if board[c][x] == 1:
            return False

    """Check the top left diagonal of this pos for queens. """
    for a, b in zip(range(c, -1, -1), range(y, -1, -1)):
        if board[a][b] == 1:
            return False

    """Check the bottom left diagonal of this pos for queens. """
    for a, b in zip(range(c, n), range(y, -1, -1)):
        if board[a][b] == 1:
            return False

    return True


def solveBoard(board, y, n):
    """ Tries to find a solution to the n queens problem by
    placing queens and backtracking where a solution does not exist.
    """
    if y >= n:
        printBoard(board)
        return True

    res = False
    for i in range(n):
        if isPosSafe(board, i, y, n):
            board[i][y] = 1

            res = solveBoard(board, y + 1, n) or res

            board[i][y] = 0

    return res


def solve_nQueens(n):
    """ places N non-attacking queens on an N×N chessboard. """

    """ Initialize board of size n. """
    board = [[0 for i in range(n)]
             for j in range(n)]

    if solveBoard(board, 0, n) is False:
        print("No solution.")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
    except Exception:
        print("N must be a number")
        sys.exit(1)
    solve_nQueens(n)
