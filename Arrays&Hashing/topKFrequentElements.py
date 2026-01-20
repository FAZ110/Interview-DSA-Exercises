'''
Given an integer array nums and an integer k, return the k 
most frequent elements within the array.

The test cases are generated such that the answer is always 
unique.

You may return the output in any order.
'''

# EXAMPLES

# Input: nums = [1,2,2,3,3,3], k = 2
# Output: [2,3]

# Input: nums = [7,7], k = 1
# Output: [7]


def topKFrequent(nums, k):
    count = {}

    for number in nums:
        count[number] = count.get(number, 0) + 1    # Count the frequency of every number
    
    elements = [[freq, num] for num, freq in count.items()] # get the data to an array

    elements.sort() # sort in ascending order

    res = []

    for _ in range(k):
        res.append(elements.pop()[1])   # lastly pop last element each time (k times) and add it to the output array
    
    return res


nums = [1,2,2,3,3,3]
k = 2

print(topKFrequent(nums, k))