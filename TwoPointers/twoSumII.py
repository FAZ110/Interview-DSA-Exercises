'''
Given an array of integers numbers that is sorted in 
non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], 
such that they add up to a given target number target and index1 
< index2. Note that index1 and index2 cannot be equal, therefore 
you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use O(1)O(1) additional space.
'''

# EXAMPLES

# Input: numbers = [1,2,3,4], target = 3
# Output: [1,2]


def twoSum(numbers, target):
    l,r = 0, len(numbers)-1

    current_sum = numbers[l] + numbers[r]

    while l < r:

        if current_sum < target:
            current_sum = current_sum - numbers[l] + numbers[l+1]
            l += 1
        
        elif current_sum > target:
            current_sum = current_sum - numbers[r] + numbers[r-1]
            r -= 1
        
        else:
            return [l+1, r+1]
    

# We have l and r indexes, if the sum of the numbers at these indexes is lower than target we move to l+1(increase the sum), 
# if it is higher we go to r-1(decrease the sum) [!! array is SORTED !!]. At some point we have to get the target sum.

numbers = [1,2,3,4]
target = 3

print(twoSum(numbers, target))