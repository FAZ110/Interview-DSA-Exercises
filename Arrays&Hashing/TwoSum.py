'''
Given an array of integers nums and an integer target, return the indices 
i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j 
that satisfy the condition.

Return the answer with the smaller index first. 
'''

# EXAMPLES

# Input: nums = [3,4,5,6], target = 7
# Output: [0,1]


# Input: nums = [4,5,6], target = 10
# Output: [0,2]

# Input: nums = [5,5], target = 10
# Output: [0,1]


def twoSum(nums, target):
    n = len(nums)

    seen = {}

    for i in range(n):
        if target - nums[i] in seen:            # If values target - nums[i] is present earlier in the array then we have found an answer
            return [seen[target-nums[i]], i]
        else:
            seen[nums[i]] = i       # If we do not have an answer for now, we memorize the index of the current value
    