'''
You are given an array nums of integers, which may contain duplicates. 
Return all possible subsets.

The solution must not contain duplicate subsets. You may return 
the solution in any order.
'''

# EXAMPLES

# Input: nums = [1,2,1]
# Output: [[],[1],[1,2],[1,1],[1,2,1],[2]]

# Input: nums = [7,7]
# Output: [[],[7], [7,7]]


def subsetsWithDup(nums):
    n = len(nums)
    nums.sort() # We sort nums to avoid duplicate subsets
                # EXAMPLE: if we have nums = [1,2,1] we would have subset1 = [1,2] and subset2 = [2,1] which are equal, with sorted nums that situation won't happen
    res = []

    def rek(subset, idx):
        if idx == n and subset not in res:
            res.append(subset[::])
            return
        elif subset in res:
            return
        
        subset.append(nums[idx])
        rek(subset, idx+1)
        subset.pop()
        rek(subset, idx+1)
    rek([], 0)

    return(res)

nums = [1,2,1]
print(subsetsWithDup(nums))
