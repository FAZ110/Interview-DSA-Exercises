'''
Given an integer array nums, return the length of the longest strictly 
increasing subsequence.
A subsequence is a sequence that can be derived from the given 
sequence by deleting some or no elements without changing the 
relative order of the remaining characters.

For example, "cat" is a subsequence of "crabt".
'''


# EXAMPLES

# Input: nums = [9,1,4,2,3,3,7]
# Output: 4

# Input: nums = [0,3,1,3,2,3]
# Output: 4

# IDEA

'''
Initialize dp with 1's, dp[i] will represent the longest strictly
increasing subsequence which ends at nums[i]
'''

def lengthOfLIS(nums):
    n = len(nums)

    dp = [1 for _ in range(n)]
    
    for i in range(1, n):   # for every number in nums
        best = 1
        for j in range(i):  # we iterate through every number before it and check for potential extensions

            if nums[j] < nums[i]:   # extension condition
                best = max(best, dp[j]+1)
        dp[i] = best    # longest extension
    
    return max(dp)


nums = [9,1,4,2,3,3,7,1]
# nums = [0,3,1,3,2,3]
print(lengthOfLIS(nums))




