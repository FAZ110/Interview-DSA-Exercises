'''
Given an integer array nums, return an array output 
where output[i] is the product of all the elements of nums 
except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n)O(n) time without using 
the division operation?
'''

# EXAMPLES

# Input: nums = [1,2,4,6]

# Output: [48,24,12,8]


# Input: nums = [-1,0,1,2,3]

# Output: [0,-6,0,0,0]


def productExceptSelf(nums):
    n = len(nums)

    prefix = [1]*n      # We store prefix/sufix multipliers (except element at index i)
    sufix = [1]*n

    for i in range(1,n):
        prefix[i] = prefix[i-1]*nums[i-1]   

    for i in range(n-2, -1, -1):
        sufix[i] = sufix[i+1]*nums[i+1]
    
    for i in range(n):
        prefix[i] *= sufix[i]   # finally we calculate the result using these two arrays
    
    return prefix
    
    
nums = [1,2,4,6]
nums = [-1,0,1,2,3]
print(productExceptSelf(nums))
        