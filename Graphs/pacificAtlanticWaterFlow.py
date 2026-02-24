'''
You are given a rectangular island heights where heights[r][c] 
represents the height above sea level of the cell at coordinate 
(r, c).

The islands borders the Pacific Ocean from the top and left sides, 
and borders the Atlantic Ocean from the bottom and right sides.

Water can flow in four directions (up, down, left, or right) from a 
cell to a neighboring cell with height equal or lower. Water can 
also flow into the ocean from cells adjacent to the ocean.

Find all cells where water can flow from that cell to both the 
Pacific and Atlantic oceans. Return it as a 2D list where each 
element is a list [r, c] representing the row and column of the 
cell. You may return the answer in any order.
'''


# EXAMPLES

# Input: heights = [
#   [4,2,7,3,4],
#   [7,4,6,4,7],
#   [6,3,5,3,6]
# ]

# Output: [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]


# Input: heights = [[1],[1]]

# Output: [[0,0],[1,0]]



def pacificAtlantic(heights):
    n, m = len(heights), len(heights[0])
    moves = [(0,1), (1,0), (-1,0), (0,-1)]

    pacific = set() # cells that reach pacific ocean
    atlantic = set()    # cells that reach atlantic ocean

    def dfs(x, y, ocean):
        ocean.add((x,y))

        for dx, dy in moves:
            new_x = x + dx
            new_y = y + dy

            # borders + not visited yet + higher than parent
            if 0 <= new_x < n and 0 <= new_y < m and (new_x, new_y) not in ocean and heights[new_x][new_y] >= heights[x][y]:
                dfs(new_x, new_y, ocean)

    # adding every border cells
    for i in range(n):
        dfs(i, 0, pacific)
        
    for j in range(m):
        dfs(0, j, pacific)
        
    for i in range(n):
        dfs(i, m-1, atlantic)
        
    for j in range(m):
        dfs(n-1, j, atlantic)
        
    res = []

    # forming result, cell has to be both in pacific and atlantic set
    for elem in pacific:
        if elem in atlantic:
            res.append([elem[0], elem[1]])
        
    return res
    



heights = [
  [4,2,7,3,4],
  [7,4,6,4,7],
  [6,3,5,3,6]
]

print(pacificAtlantic(heights))
