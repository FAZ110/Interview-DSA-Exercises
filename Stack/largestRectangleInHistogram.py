'''
You are given an array of integers heights where heights[i] 
represents the height of a bar. The width of each bar is 1.

Return the area of the largest rectangle that can be formed 
among the bars.
'''

# EXAMPLES

# Input: heights = [7,1,7,2,2,4]
# Output: 8

# Input: heights = [1,3,7]
# Output: 7


# MAIN IDEA
'''
The code maintains a stack of indices with increasing heights; 
as long as bars get taller, they are pushed because their 
rectangle can still extend to the right. When a shorter bar 
is encountered, it acts as a "wall" that ends the rectangle 
for the taller bars on the stack, triggering a pop to calculate 
their area using the current index (right boundary) and the new 
stack top (left boundary) to determine the width. This ensures 
that for every bar, we calculate the maximum possible rectangle 
where that specific bar is the shortest one (the bottleneck).
'''


def largestRectangleArea(heights):
    # Appending 0 forces the stack to empty at the end, 
    # handling the "remaining items" problem automatically.
    heights.append(0)
    n = len(heights)

    stack = []  # stack with increasing heights indicies
    max_area = 0

    for i in range(n):
        
        while stack and heights[stack[-1]] > heights[i]:    #if the current height heights[i] is smaller then we can't extend the bar at idx stack[-1] anymore, so we pop it
            h = heights[stack.pop()] # The height of the rectangle is the bar we just popped
            
            if stack:
                width = i - stack[-1] - 1 # we know that stack[-1] after popping earlier is the furthest we can extend to the left
            else:
                width = i
        
            max_area = max(max_area, h*width)

        stack.append(i)
        
    
    return max_area


heights = [7,1,7,2,2,4]
print(largestRectangleArea(heights))





