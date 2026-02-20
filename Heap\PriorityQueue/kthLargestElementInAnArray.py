'''
Given an unsorted array of integers nums and an integer k, return 
the kth largest element in the array.

By kth largest element, we mean the kth largest element in the 
sorted order, not the kth distinct element.

Follow-up: Can you solve it without sorting?
'''

# EXAMPLES

# Input: nums = [2,3,1,5,4], k = 2
# Output: 4

# Input: nums = [2,3,1,1,5,5,4], k = 3
# Output: 4

import heapq
def findKthLargest(nums, k):

    heap = []

    for num in nums:
        heap.append(-num)
    
    heapq.heapify(heap)

    for _ in range(k-1):
        heapq.heappop(heap)
    
    return -heapq.heappop(heap)


nums = [2,3,1,1,5,5,4]
k = 3

print(findKthLargest(nums, k))