'''
Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, 
and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. 
You may return the output and the triplets in any order
'''

# EXAMPLES

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Input: nums = [0,1,1]
# Output: []

# Input: nums = [0,0,0]
# Output: [[0,0,0]]


def threeSum(nums):
    n = len(nums)

    nums.sort()
    res = []
    for i in range(n):

        if nums[i] > 0:     # if the number nums[i] is positive there is no way that the sum will be 0 because it is the smallest number of af all three
            break

        if i > 0 and nums[i] == nums[i-1]:  # skip duplicates
            continue
        

        l,r = i+1, n-1

        while l < r:
            three_sum = nums[i] + nums[l] + nums[r]

            if three_sum > 0:
                r-=1
            elif three_sum < 0:
                l += 1
            else:
                
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1

                while l < r and nums[l] == nums[l-1]:   # skip duplicates
                    l += 1
    
    return res
        

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))
