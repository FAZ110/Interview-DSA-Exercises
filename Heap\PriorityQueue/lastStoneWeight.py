'''
You are given an array of integers stones where stones[i] represents 
the weight of the ith stone.

We want to run a simulation on the stones as follows:

    At each step we choose the two heaviest stones, with weight x 
    and y and smash them togethers
    If x == y, both stones are destroyed
    If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

Continue the simulation until there is no more than one stone 
remaining.

Return the weight of the last remaining stone or return 0 if none 
remain.
'''

# EXAMPLES

# Input: stones = [2,3,6,2,4]
# Output: 1

# Input: stones = [1,2]
# Output: 1

# IDEA
'''
We use heapq (min heap) to track heaviest stones left.
'''

import heapq
def lastStoneWeight(stones):

    heap = []
    for stone in stones:
        heap.append(-stone) # we append -stone because we use min heap not max heap
    
    heapq.heapify(heap)

    while len(heap) > 1:
        first = -heapq.heappop(heap)
        second = -heapq.heappop(heap)

        if first > second:
            new_stone = first-second

            heapq.heappush(heap, -new_stone)
    
    return -heap[0] if len(heap) > 0 else 0


stones = [2,3,6,2,4]
stones = [1,2]
print(lastStoneWeight(stones))