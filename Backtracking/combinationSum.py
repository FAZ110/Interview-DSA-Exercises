'''
You are given an array of distinct integers nums and a target integer target. Your task is to return a list of 
all unique combinations of nums where the chosen numbers sum to target.

The same number may be chosen from nums an unlimited number of times. 
Two combinations are the same if the frequency of each of the chosen numbers is the same, otherwise they are different.

You may return the combinations in any order and the order of the numbers in each combination can be in any order.
'''

# EXAMPLES

# Input:
# nums = [2,5,6,9]
# target = 9

# Output: [[2,2,5],[9]]

# Input:
# nums = [3,4,5]
# target = 16

# Output: [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]

# IDEA
'''
At each index we have 2 choices we can keep adding nums[i] to comb or we can move to
the next idx.

IMPORTANT!
if we add nums[idx] to comb we call rek(comb, comb_sum, idx), without changing idx
because we can add nums[idx] multiple times!!!
'''
def combinationSum(nums, target):
    n = len(nums)

    res = []

    def rek(comb, comb_sum, idx):
        if comb_sum == target and comb not in res:
            res.append(comb[::])
            return
        elif comb_sum > target or idx > n - 1:
            return
        else:
            comb.append(nums[idx])
            comb_sum += nums[idx]
            rek(comb, comb_sum, idx)
            comb.pop()
            comb_sum -= nums[idx]
            rek(comb, comb_sum, idx+1)
    rek([], 0, 0)
    return res


nums = [2,5,6,9]
target = 9

nums = [3,4,5]
target = 16
print(combinationSum(nums, target))
