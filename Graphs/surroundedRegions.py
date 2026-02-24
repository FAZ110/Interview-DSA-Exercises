'''
You are given a 2-D matrix board containing 'X' and 'O' characters.

If a continous, four-directionally connected group of 'O's is 
surrounded by 'X's, it is considered to be surrounded.

Change all surrounded regions of 'O's to 'X's and do so in-place 
by modifying the input board.


Explanation: Note that regions that are on the border are 
not considered surrounded regions.
'''

# EXAMPLES

# Input: board = [
#   ["X","X","X","X"],
#   ["X","O","O","X"],
#   ["X","O","O","X"],
#   ["X","X","X","O"]
# ]

# Output: [
#   ["X","X","X","X"],
#   ["X","X","X","X"],
#   ["X","X","X","X"],
#   ["X","X","X","O"]
# ]

# IDEA
'''
We will try to mark every achievable spots with "O" from edges by using dfs
and mark them by "S" (safe), then loop through the board and changed all remaining
"O" to "X" and every "S" to "O".
'''

def solve(board):
    n, m = len(board), len(board[0])

    moves = [(0,1), (1,0), (-1,0), (0,-1)]

    if not board or not board[0]:
        return

    def dfs(x, y):

        board[x][y] = "S"

        for dx,dy in moves:
            new_x = x + dx
            new_y = y + dy

            if 0 <= new_x < n and 0 <= new_y < m and board[new_x][new_y] == "O":
                dfs(new_x, new_y)
    
    for i in range(n):
        if board[i][0] == "O":
            dfs(i, 0)
        if board[i][m-1] == "O":
            dfs(i, m-1)
    
    for j in range(m):
        if board[0][j] == "O":
            dfs(0, j)
        if board[n-1][j] == "O":
            dfs(n-1, j)
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == "O":
                board[i][j] = "X"
            elif board[i][j] == "S":
                board[i][j] = "O"





board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","O","O","X"],
  ["X","X","X","O"]
]

solve(board)

print(board)


    




