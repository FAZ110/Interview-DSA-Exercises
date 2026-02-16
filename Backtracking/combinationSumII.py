'''
You are given an array of integers candidates, which may contain duplicates, and a target integer target. 
Your task is to return a list of all unique combinations of candidates
where the chosen numbers sum to target.

Each element from candidates may be chosen at most once within a 
combination. The solution set must not contain duplicate combinations.

You may return the combinations in any order and the order of the 
numbers in each combination can be in any order.
'''

# EXAMPLES

# Input: candidates = [9,2,2,4,6,1,5], target = 8

# Output: [
#   [1,2,5],
#   [2,2,4],
#   [2,6]
# ]

# Input: candidates = [1,2,3,4,5], target = 7

# Output: [
#   [1,2,4],
#   [2,5],
#   [3,4]
# ]

# IDEA
'''
Very similar to combinationSum, but we can only select a specific element once, so
every time we move to idx+1
'''


def combinationSum2(candidates, target):
    n = len(candidates)
    candidates.sort()   # We have to sort the array to avoid the same results

    res = []

    def rek(comb, comb_sum, idx):
        if comb_sum == target and comb not in res:
            res.append(comb[::])
            return
        elif comb_sum > target or idx > n - 1:
            return
        
        comb.append(candidates[idx])
        comb_sum += candidates[idx]
        rek(comb, comb_sum, idx+1)
        comb.pop()
        comb_sum -= candidates[idx]
        rek(comb, comb_sum, idx+1)
    rek([], 0, 0)
    return res


candidates = [9,2,2,4,6,1,5]
target = 8

candidates = [1,2,3,4,5]
target = 7
print(combinationSum2(candidates, target))
