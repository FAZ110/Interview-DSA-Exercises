'''
You are given an array of integers nums and an integer k. 
There is a sliding window of size k that starts at the left 
edge of the array. The window slides one position to the right 
until it reaches the right edge of the array.

Return a list that contains the maximum element in the window at each step.
'''

# EXAMPLES


# Input: nums = [1,2,1,0,4,2,6], k = 3

# Output: [2,2,4,4,6]

# Explanation:
# Window position            Max
# ---------------           -----
# [1  2  1] 0  4  2  6        2
#  1 [2  1  0] 4  2  6        2
#  1  2 [1  0  4] 2  6        4
#  1  2  1 [0  4  2] 6        4
#  1  2  1  0 [4  2  6]       6


import heapq
def maxSlidingWindow(nums, k):
    n = len(nums)

    heap = []   # We use heap to track the biggest element in the window
    res = [0 for _ in range(n-k+1)]

    for i in range(k):
        heap.append((-nums[i], i))  # We add onto the heap elements and indexes from the starting window
    heapq.heapify(heap) # make a heap
    l = 0

    for r in range(k-1, n):
        heapq.heappush(heap, (-nums[r], r)) # Push current element onto the heap
        while heap[0][1] < l:   # while the biggest element is not viable pop it
            heapq.heappop(heap)

        res[l] = -heap[0][0]
        
        l += 1
    
    return res




nums = [1,2,1,0,4,2,6]
k = 3
print(maxSlidingWindow(nums, k))




# ALTERNATIVE SOLUTION

from collections import deque

def maxSlidingWindow(nums, k):
    q = deque() # Will store INDICES
    res = []
    
    for r in range(len(nums)):
        # 1. Pop smaller values from the back
        # If nums[r] is bigger than the last thing in the queue, 
        # the last thing is useless. Remove it.
        while q and nums[q[-1]] < nums[r]:
            q.pop()
            
        # 2. Add current index
        q.append(r)
        
        # 3. Remove index from the front if it's out of the window
        # The window is [r - k + 1, r]. If q[0] is less than left bound, pop it.
        if q[0] < r - k + 1:
            q.popleft()
            
        # 4. Add to result (only if our window has reached size k)
        if r + 1 >= k:
            res.append(nums[q[0]])
            
    return res
