'''
You are given an integer array nums where nums[i] represents the amount of 
money the ith house has. The houses are arranged in a circle, i.e. the 
first house and the last house are neighbors.

You are planning to rob money from the houses, but you cannot rob two 
adjacent houses because the security system will automatically alert 
the police if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the 
police.
'''

# EXAMPLES

# Input: nums = [3,4,3]
# Output: 4

# Input: nums = [2,9,8,3,6]
# Output: 15

# IDEA
'''
We use 2 arrays, in the first one we include the first house(so last one is excluded),
in the seconf one is the opposite. By doing that we simulate both scenarios.
'''


def rob(nums):
    n = len(nums)

    if n < 3:
        return max(nums)

    first_include = [0]*n
    last_include = [0]*n


    first_include[0], first_include[1] = nums[0], max(nums[0], nums[1])
    last_include[1] = nums[1]

    for i in range(2, n):
        first_include[i] = max(first_include[i-1], first_include[i-2]+nums[i])
        last_include[i] = max(last_include[i-1], last_include[i-2]+nums[i])
    
    return max(first_include[-2], last_include[-1]) # In the first array we want second to last element (because the last one is excluded)


        
nums = [2,9,8,3,6]
print(rob(nums))
