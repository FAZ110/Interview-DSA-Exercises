'''
Given an array of integers nums, return the length of the longest consecutive 
sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 
1 greater than the previous element. The elements do not have to be consecutive in 
the original array.

You must write an algorithm that runs in O(n) time.
'''

# EXAMPLES

# Input: nums = [2,20,4,10,3,4,5]
# Output: 4

# Input: nums = [0,3,2,5,4,6,1,1]
# Output: 7


def longestConsecutive(nums):
    n = len(nums)

    elems = set(nums)       # We build the set for faster lookups
    res = 0

    for i in range(n):
        if nums[i] - 1 not in elems:    # KEY!!!! only if there is not nums[i]-1 in the array the nums[i] can be a\the begining of a sequence 
            start = nums[i]

            cnt = 1
            while start+1 in elems:     # counting using set
                cnt += 1
                start += 1
            
            res = max(res, cnt)
    
    return res


nums = [2,20,4,10,3,4,5]
nums = [0,3,2,5,4,6,1,1]
print(longestConsecutive(nums))



