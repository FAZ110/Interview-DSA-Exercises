'''
Given an array of integers nums, find the subarray with the largest 
sum and return the sum.

A subarray is a contiguous non-empty sequence of elements within an 
array.
'''

# EXAMPLES


# Input: nums = [2,-3,4,-2,2,1,-1,4]
# Output: 8

# Input: nums = [-1]
# Output: -1


def maxSubArray(nums):

    current = float('-inf')
    maxi = float('-inf')

    for num in nums:
        if num < 0: # If current num is smaller than 0 we have to check if current is not maxi (what if every num after will be < 0)
            maxi = max(maxi, current)
        
        if current < 0: # it is better to start new subarray
            current = 0
        
        current += num  # add current num
    
    return max(current, maxi)


nums = [2,-3,4,-2,2,1,-1,4]
# nums = [-1]
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))