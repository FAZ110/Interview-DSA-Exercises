'''
You are given an array of non-negative integers height which 
represent an elevation map. Each value height[i] represents 
the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between 
the bars.
'''


# EXAMPLES

# Input: height = [0,2,0,3,1,0,1,3,2,1]
# Output: 9

def trap(height):
    n = len(height)

    # We keep track of the tallest terrain from the i'th cell to the left/right(not inclusive)
    left = [0 for _ in range(n)]
    right = [0 for _ in range(n)]

    max_seen = 0
    for i in range(n):
        left[i] = max_seen
        max_seen = max(max_seen, height[i])
    
    max_seen = 0
    for i in range(n-1, -1, -1):
        right[i] = max_seen
        max_seen = max(max_seen, height[i])

    # We treat every index individually by checking the highest terrain to the left and right and getting the min of these.
    # After that if value height[i] is smaller than min(left[i], right[i]), then i'th cell can cointain at most cell_height - height[i] water 
    sum_area = 0
    for i in range(n):

        cell_height = min(left[i], right[i])

        if cell_height > height[i]:
            sum_area += cell_height - height[i]
    
    return sum_area




height = [0,2,0,3,1,0,1,3,2,1]
print(trap(height))