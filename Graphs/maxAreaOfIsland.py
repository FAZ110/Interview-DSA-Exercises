'''
You are given a matrix grid where grid[i] is either a 0 (representing water) 
or 1 (representing land).

An island is defined as a group of 1's connected horizontally or 
vertically. You may assume all four edges of the grid are surrounded 
by water.

The area of an island is defined as the number of cells within the 
island.

Return the maximum area of an island in grid. If no island exists, 
return 0.
'''

# EXAMPLES

# Input: grid = [
#   [0,1,1,0,1],
#   [1,0,1,0,1],
#   [0,1,1,0,1],
#   [0,1,0,0,1]
# ]

# Output: 6

# IDEA
'''
Everytime we have a cell with 1 we perform dfs where we hold variable 
current_cell_area to correctly calculate the area of an island
'''


def maxAreaOfIsland(grid):
    n = len(grid)
    m = len(grid[0])

    moves = [(0,1), (1,0), (-1,0), (0,-1)]

    max_area = 0

    def dfs(x, y):

        grid[x][y] = 0
        current_cell_area = 1

        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] == 1:
                current_cell_area += dfs(new_x, new_y) # adding each cell in the island
        return current_cell_area    # return island area
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                area = dfs(i ,j)
                max_area = max(area, max_area)
    
    return max_area


grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]

print(maxAreaOfIsland(grid))