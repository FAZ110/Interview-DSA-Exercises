'''
Given an array nums of unique integers, return all the possible 
permutations. You may return the answer in any order.
'''

# EXAMPLES

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Input: nums = [7]
# Output: [[7]]

# IDEA
'''
At each step we decide if we take num in our permutation, but there is a condition
that num shouldn't be chosen chosen previously.
'''

def permute(nums):
    n = len(nums)

    res = []

    def rek(permutation, leng):
        if leng == n:
            res.append(permutation[::])
            return
        
        for num in nums:
            if num not in permutation:
                permutation.append(num)
                rek(permutation, leng+1)
                permutation.pop()

    rek([], 0)
    return res

nums = [1,2,3]
nums = [7]
print(permute(nums))