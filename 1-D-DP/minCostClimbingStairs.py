'''
You are given an array of integers cost where cost[i] is the cost of taking a step from 
the ith floor of a staircase. After paying the cost, you can step 
to either the (i + 1)th floor or the (i + 2)th floor.

You may choose to start at the index 0 or the index 1 floor.

Return the minimum cost to reach the top of the staircase, i.e. 
just past the last index in cost.
'''

# EXAMPLES

# Input: cost = [1,2,3]
# Output: 2

# Input: cost = [1,2,1,2,1,1,1]
# Output: 4

# IDEA
'''
For every step we just add the cost of climbing on that step and 
min(cost[i-1], cost[i-2]) to decide if it is better to climb
using 2 steps or 1 step.
'''

def minCostClimbingStairs(cost):
    n = len(cost)

    for i in range(2,n):
        cost[i] = cost[i] + min(cost[i-1], cost[i-2])
    
    return min(cost[-1], cost[-2])


cost = [1,2,3]
cost = [1,2,1,2,1,1,1]
print(minCostClimbingStairs(cost))