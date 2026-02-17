'''
You are given an integer n representing the number of steps to reach 
the top of a staircase. You can climb with either 1 or 2 steps at a 
time.

Return the number of distinct ways to climb to the top of the staircase.
'''

# EXAMPLES

# Input: n = 2
# Output: 2

# Input: n = 3
# Output: 3


def climbStairs(n):
    if n == 1:
        return 1

    dp = [0 for _ in range(n)]
    dp[0] = 1
    dp[1] = 2

    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[-1]


n = 1
print(climbStairs(n))
