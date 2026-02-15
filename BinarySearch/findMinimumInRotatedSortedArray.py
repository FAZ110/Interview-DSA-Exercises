'''
You are given an array of length n which was originally sorted in ascending order. 
It has now been rotated between 1 and n times. For example, 
the array nums = [1,2,3,4,5,6] might become:

    [3,4,5,6,1,2] if it was rotated 4 times.
    [1,2,3,4,5,6] if it was rotated 6 times.

Notice that rotating the array 4 times moves the last four elements of the 
array to the beginning. Rotating the array 6 times produces the original 
array.

Assuming all elements in the rotated sorted array nums are unique, return 
the minimum element of this array.

A solution that runs in O(n) time is trivial, can you write an algorithm 
that runs in O(log n) time?
'''

# EXAMPLES

# Input: nums = [3,4,5,6,1,2]
# Output: 1

# Input: nums = [4,5,0,1,2,3]
# Output: 0

# Input: nums = [4,5,6,7]
# Output: 4

# IDEA

'''
Everytime we check 3 values: nums[l], nums[mid] and nums[r]. 
Always 2/3 of these values will be in the same sorted part of the array
'''

def findMin(nums):

    l,r = 0, len(nums)-1

    while l < r:

        mid = (l+r)//2

        if nums[mid] < nums[r]: # if this is true we know that mid and r are in the sorted part of the array, so we can r = mid (mid can be the smallest element) 
            r = mid 
        else:
            l = mid + 1 # else we know l and mid are in the sorted part 
    
    return nums[l]


nums = [4,5,0,1,2,3]
nums = [3,4,5,6,1,2]
print(findMin(nums))


