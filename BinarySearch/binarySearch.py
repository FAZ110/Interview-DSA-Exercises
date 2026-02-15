'''
You are given an array of distinct integers nums, sorted in ascending order, 
and an integer target.

Implement a function to search for target within nums. If it exists, then 
return its index, otherwise, return -1.

Your solution must run in O(logn)O(logn) time.
'''

# EXAMPLES

# Input: nums = [-1,0,2,4,6,8], target = 4
# Output: 3

# Input: nums = [-1,0,2,4,6,8], target = 3
# Output: -1


def search(nums, target):

    l,r = 0, len(nums)-1

    while l <= r:

        mid = (l+r)//2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1 
        else:
            r = mid - 1
    
    return -1

nums = [-1,0,2,4,6,8]
target = 4

nums = [-1,0,2,4,6,8]
target = 3

nums = [-1,0,3,5,9,12]
target = 9

print(search(nums, target))

