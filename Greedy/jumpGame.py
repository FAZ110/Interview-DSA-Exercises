'''
You are given an integer array nums where each element nums[i] 
indicates your maximum jump length at that position.

Return true if you can reach the last index starting from index 0, 
or false otherwise.
'''

# EXAMPLES

# Input: nums = [1,2,0,1,0]
# Output: true

# Input: nums = [1,2,1,0,1]
# Output: false


def canJump(nums):

    n = len(nums)
    canAchieve = [False for _ in range(n)]  # array to track where we can jump
    canAchieve[0] = True    # start from 0

    for i in range(n):

        if canAchieve[i]:   # if we can jump to i then we can jump to every i+nums[i]

            for j in range(i+1, i+nums[i]+1):   
                if j < n:
                    canAchieve[j] = True
    
    return canAchieve[-1]


nums = [1,2,0,1,0]
nums = [1,2,1,0,1]
print(canJump(nums))