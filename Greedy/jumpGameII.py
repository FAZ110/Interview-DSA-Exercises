'''
You are given an array of integers nums, where nums[i] represents 
the maximum length of a jump towards the right from index i. 
For example, if you are at nums[i], you can jump to any index i + j 
where:

    j <= nums[i]
    i + j < nums.length

You are initially positioned at nums[0].

Return the minimum number of jumps to reach the last position in 
the array (index nums.length - 1). You may assume there is always 
a valid answer.
'''

# EXAMPLES

# Input: nums = [2,4,1,1,1,1]
# Output: 2

# Input: nums = [2,1,2,1,0]
# Output: 2


def jump(nums):
    n = len(nums)

    P = [float('inf') for _ in range(n)]    # in how many jumps we can reach idx i
    P[0] = 0    # starting point

    for i in range(n):
        for j in range(i+1, i+1+nums[i]):   # range of the jump form i

            if j < n:
                P[j] = min(P[i]+1, P[j])    # min(jump from i, current min form previous idx)
    
    return P[-1]


nums = [2,4,1,1,1,1]
nums = [2,1,2,1,0]
print(jump(nums))