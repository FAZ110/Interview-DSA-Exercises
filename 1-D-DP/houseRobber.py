'''
You are given an integer array nums where nums[i] represents the 
amount of money the ith house has. The houses are arranged in a 
straight line, i.e. the ith house is the neighbor of the (i-1)th 
and (i+1)th house.

You are planning to rob money from the houses, but you cannot rob 
two adjacent houses because the security system will automatically 
alert the police if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the 
police.
'''

# EXAMPLES

# Input: nums = [1,1,3,3]
# Output: 4

# Input: nums = [2,9,8,3,6]
# Output: 16

# IDEA
'''
We initialize dp array, dp[i] represents maximum money that we can rob 
TO i'th house (including i) while trying to avoid raising the alarm. 
The formula is simple dp[i] = max(dp[i-1], dp[i-2]+nums[i]),
dp[i-1] is the decision to skip current house and take the most money that we
can rob to i-1'th house, dp[i-1]+nums[i] is a decision to include current house and
take the money from dp[i-2] to avoid alarm. 
'''

def rob(nums):
    n = len(nums)

    if n < 3:
        return max(nums)

    dp = [0 for _ in range(n)]

    dp[0] = nums[0]
    dp[1] = max(nums[1], nums[0])
    

    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2]+nums[i])
    
    return dp


nums = [1,1,3,3]
nums = [2,9,8,3,6]
nums=[5,1,2,10,6,2,7,9,3,1]
print(rob(nums))