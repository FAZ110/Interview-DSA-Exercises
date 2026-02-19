'''
Return true if you can partition the array into two subsets, 
subset1 and subset2 where sum(subset1) == sum(subset2). 
Otherwise, return false.
'''

# EXAMPLES

# Input: nums = [1,2,3,4]
# Output: true

# Input: nums = [1,2,3,4,5]
# Output: false


def canPartition(nums):
    total = sum(nums)

    if total % 2 == 1: return False
    target = total // 2

    dp = [False]*(target+1)
    dp[0] = True

    for num in nums:

        for i in range(target, num-1, -1):
            if dp[i-num]:
                dp[i] = True
        
        if dp[target]: return True
    
    return dp[target]



nums = [1,2,3,4]
print(canPartition(nums))