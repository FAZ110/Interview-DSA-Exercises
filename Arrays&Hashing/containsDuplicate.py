'''Given an integer array nums, return true if any value 
appears more than once in the array, otherwise return false.'''

# EXAMPLES

# Input: nums = [1, 2, 3, 3]
# Output: true

# Input: nums = [1, 2, 3, 4]
# Output: false


def hasDuplicate(nums):

    seen = set()

    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False