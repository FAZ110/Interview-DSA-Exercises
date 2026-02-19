'''
Given an integer array nums, find a subarray that has the largest 
product within the array and return it.

A subarray is a contiguous non-empty sequence of elements within an 
array.

You can assume the output will fit into a 32-bit integer.
'''

# EXAMPLES

# Input: nums = [1,2,-3,4]
# Output: 4

# Input: nums = [-2,-1]
# Output: 2

# IDEA
'''
use Kadane's algorithm to properly track max and min values while iterating
through the array
'''

def maxProduct(nums):
    n = len(nums)

    current = nums[0]   # maximum product value until current idx
    current_min = nums[0]   # minimum product value until current idx
    maxi = nums[0]  # store the result

    for i in range(1, n):
        temp = current  # use temp to not use new current value
        current = max(current*nums[i], current_min*nums[i], nums[i])
        current_min = min(temp*nums[i], current_min*nums[i], nums[i])
        
        maxi = max(maxi, current)
    
    return maxi


nums = [1,2,-3,4]
# nums = [-2,-1]
nums=[2,3,-2,4]
# nums = [-4,-3,-2]
print(maxProduct(nums))


