'''
You are given a 2-D matrix grid. Each cell can have one of three 
possible values:

    0 representing an empty cell
    1 representing a fresh fruit
    2 representing a rotten fruit

Every minute, if a fresh fruit is horizontally or vertically 
adjacent to a rotten fruit, then the fresh fruit also becomes 
rotten.

Return the minimum number of minutes that must elapse until there 
are zero fresh fruits remaining. If this state is impossible within 
the grid, return -1.
'''

# EXAMPLES

# Input: grid = [[1,1,0],[0,1,1],[0,1,2]]
# Output: 4

# Input: grid = [[1,0,1],[0,2,0],[1,0,1]]
# Output: -1

# IDEA
'''
We count fresh fruit and add rotten ones to deque (starting points),
then we simulate rotting in the queue by adding neighbours of each one
of the fruit. The last's fruit time is the max_time needed for all fruit to
be rotten at the end.
'''

from collections import deque
def orangesRotting(grid):
    n, m = len(grid), len(grid[0])

    moves = [(0,1), (1,0), (-1,0), (0,-1)]
    queue = deque()

    max_time = 0
    fresh_count = 0

    # counting fresh fruit and adding rotten ones to deque
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                queue.append((i, j, 0))
            elif grid[i][j] == 1:
                fresh_count += 1

    
    if fresh_count == 0:
        return 0
    
    while queue:
        x,y,time = queue.popleft()
        max_time = time

        for dx, dy in moves:
            new_x = x + dx
            new_y = y + dy
            if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] == 1:
                grid[new_x][new_y] = 2
                fresh_count -= 1
                queue.append((new_x, new_y, time+1))   

    return max_time if fresh_count == 0 else -1

grid = [[1,1,0],[0,1,1],[0,1,2]]
grid = [[1,0,1],[0,2,0],[1,0,1]]
grid=[[2,1,1],[0,1,1],[1,0,1]]
print(orangesRotting(grid))