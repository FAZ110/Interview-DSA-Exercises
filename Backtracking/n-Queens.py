'''
The n-queens puzzle is the problem of placing n queens on an n x n 
chessboard so that no two queens can attack each other.

A queen in a chessboard can attack horizontally, vertically, and 
diagonally.

Given an integer n, return all distinct solutions to the n-queens 
puzzle.

Each solution contains a unique board layout where the queen pieces 
are placed. 'Q' indicates a queen and '.' indicates an empty space.

You may return the answer in any order.
'''

# EXAMPLES

# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

# Input: n = 1
# Output: [["Q"]]

def solveNQueens(n):
    res = []
    board = [["."] * n for _ in range(n)]

    # Sets to track "under attack" paths in O(1) time
    cols = set()
    pos_diag = set() # (r + c)
    neg_diag = set() # (r - c)

    def backtrack(r):
        # Base Case: All rows are filled
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return

        for c in range(n):
            # 1. Check if this position is under attack
            if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                continue

            # 2. "Take" the spot
            cols.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            board[r][c] = "Q"

            # 3. Explore the next row
            backtrack(r + 1)

            # 4. "Undo" the choice (Backtrack)
            cols.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            board[r][c] = "."

    backtrack(0)
    return res

# Test for n = 4
print(solveNQueens(4))
