'''
You are given an array of integers nums and an integer target.
For each number in the array, you can choose to either add or subtract it to a total sum.

    For example, if nums = [1, 2], one possible sum would be "+1-2=-1".

If nums=[1,1], there are two different ways to sum the input numbers to get a sum of 0: "+1-1" and "-1+1".

Return the number of different ways that you can build the expression such that the total sum equals target.
'''

# EXAMPLES

# Input: nums = [2,2,2], target = 2
# Output: 3


def findTargetSumWays(nums, target):
    n = len(nums)
    total_sum = sum(nums)

    if abs(target) > total_sum:
        return 0
    
    offset = total_sum
    
    # we use the inner array of size 2*total_sum+1 because we have to simulate
    # negative values 
    memo = [[-1 for _ in range(2*total_sum+1)]for _ in range(n)]


    def rek(idx, current):
        if idx == n:
            return 1 if current == target else 0
        
        if memo[idx][current + offset] != -1:   # we processed this outcome before
            return memo[idx][current + offset]
        
        add = rek(idx + 1, current + nums[idx]) # adding
        substract = rek(idx + 1, current - nums[idx]) # substracting

        memo[idx][current + offset] = add + substract # adding number of ways to reach target from both paths
        return memo[idx][current][offset]

    return rek(0,0)