'''
You are given a mxn 2D grid initialized with these three possible values:

    -1 - A water cell that can not be traversed.
    0 - A treasure chest.
    INF - A land cell that can be traversed. We use the integer 
    2^31 - 1 = 2147483647 to represent INF.

Fill each land cell with the distance to its nearest treasure 
chest. If a land cell cannot reach a treasure chest then the 
value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Modify the grid in-place.
'''

# EXAMPLES

# Input: [
#   [2147483647,-1,0,2147483647],
#   [2147483647,2147483647,2147483647,-1],
#   [2147483647,-1,2147483647,-1],
#   [0,-1,2147483647,2147483647]
# ]

# Output: [
#   [3,-1,0,1],
#   [2,2,1,-1],
#   [1,-1,2,-1],
#   [0,-1,3,4]
# ]


# Input: [
#   [0,-1],
#   [2147483647,2147483647]
# ]

# Output: [
#   [0,-1],
#   [1,2]
# ]


# IDEA
'''
We use mutlisource BFS, from every treasure position, we go through 
neighbours and check if we find closer treasure, BFS guarantees that
closest chests will be computed earlier so there is no need to check
distance condition. 
'''

from collections import deque
def islandsAndTreasure(grid):
    n, m = len(grid), len(grid[0])
    INF = 2147483647

    moves = [(0,1), (1,0), (-1,0), (0,-1)]

    queue = deque()

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                queue.append((i, j))    # every treasure (dist 0)
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] == INF: # available cell
                grid[new_x][new_y] = grid[x][y] + 1
                queue.append((new_x, new_y))


grid = [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]


islandsAndTreasure(grid)
for row in grid:
    print(row)