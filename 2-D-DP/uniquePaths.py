'''
There is an m x n grid where you are allowed to move either down 
or to the right at any point in time.

Given the two integers m and n, return the number of possible 
unique paths that can be taken from the top-left corner of the 
grid (grid[0][0]) to the bottom-right corner (grid[m - 1][n - 1]).

You may assume the output will fit in a 32-bit integer.
'''

# EXAMPLES

# Input: m = 3, n = 6
# Output: 21

# Input: m = 3, n = 3
# Output: 6

# IDEA
'''
because we are able to move either down or right, we can set the 
first column and first row to 1's. In the main loop we look up and left
and add those values, this is in how many ways we can go on grid[i][j] 

grid[i][j] = grid[i-1][j] + grid[i][j-1]
'''

def uniquePaths(m, n):

    dp = [[0 for _ in range(n)] for _ in range(m)]
    
    for j in range(n):
        dp[0][j] = 1
    
    for i in range(m):
        dp[i][0] = 1

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
  
    return dp[-1][-1]


m = 3
n = 6

m = 3
n = 3
print(uniquePaths(m, n))