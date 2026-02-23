'''
Given a 2D grid grid where '1' represents land and '0' represents 
water, count and return the number of islands.

An island is formed by connecting adjacent lands horizontally or 
vertically and is surrounded by water. You may assume water is 
surrounding the grid (i.e., all the edges are water). 
'''

# EXAMPLES

# Input: grid = [
#     ["0","1","1","1","0"],
#     ["0","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]
#   ]
# Output: 1


# Input: grid = [
#     ["1","1","0","0","1"],
#     ["1","1","0","0","1"],
#     ["0","0","1","0","0"],
#     ["0","0","0","1","1"]
#   ]
# Output: 4

# IDEA

'''
We go through every cell and if we find grid[i][j] == "1", then we run
dfs in that cell which will mark every indirectly connected cell with grid[i][j],
so we will catch whole island and we won't count it multiple times.
'''



def numIslands(grid):
    n = len(grid)
    m = len(grid[0])

    moves = [(0,1), (1,0), (-1,0), (0,-1)]

    res = 0

    def dfs(x, y):
        grid[x][y] = "0"    # marking


        for dx,dy in moves:
            new_x, new_y = x+dx, y+dy
            if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] == "1":
                dfs(new_x, new_y)   # dfs on neighbours
        
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "1":   # new island
                res += 1
                dfs(i, j)
    
    return res


grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]


grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
print(numIslands(grid))