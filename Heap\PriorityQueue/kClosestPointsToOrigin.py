'''
You are given an 2-D array points where points[i] = [xi, yi] 
represents the coordinates of a point on an X-Y axis plane. 
You are also given an integer k.

Return the k closest points to the origin (0, 0).

The distance between two points is defined as the Euclidean 
distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).

You may return the answer in any order.
'''

# EXAMPLES

# Input: points = [[0,2],[2,2]], k = 1
# Output: [[0,2]]

# Input: points = [[0,2],[2,0],[2,2]], k = 2
# Output: [[0,2],[2,0]]

# IDEA
'''
Calculate the distance from each point to (0,0) and create a heap,
pop k elements from the heap while maintaining the structure 
'''

import heapq, math
def kClosest(points, k):
    heap = []

    for x,y in points:
        dist = math.sqrt(x**2 + y**2)

        heap.append((dist, x, y))
    
    heapq.heapify(heap)
    res = []

    for _ in range(k):
        _, x, y = heapq.heappop(heap)
        
        res.append([x, y])
    return res


points = [[0,2],[2,0],[2,2]]
k = 2

points=[[3,3],[5,-1],[-2,4]]
k=2

print(kClosest(points, k))
