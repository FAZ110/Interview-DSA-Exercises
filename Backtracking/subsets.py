'''
Given an array nums of unique integers, return all possible subsets 
of nums.

The solution set must not contain duplicate subsets. You may return the solution 
in any order.
'''

# EXAMPLES

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Input: nums = [7]
# Output: [[],[7]]

# IDEA
# At every index in nums we have a choice either we INCLUDE nums[i] in the subset
# or we EXCLUDE it. Number of subsets is 2^len(nums).

def subsets(nums):
    n = len(nums)
    res = []

    def rek(subset, idx):
        if idx == n:
            res.append(subset[::])
            return
        
        subset.append(nums[idx])
        rek(subset, idx+1)
        subset.pop()
        rek(subset, idx+1)
        
    rek([], 0)
    return res
        


nums = [1,2,3]
print(subsets(nums))


