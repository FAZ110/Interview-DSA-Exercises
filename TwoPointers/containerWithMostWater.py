'''
You are given an integer array heights where heights[i] 
represents the height of the ithith bar.

You may choose any two bars to form a container. Return the 
maximum amount of water a container can store.
'''

# EXAMPLES

# Input: height = [1,7,2,5,4,7,3,6]
# Output: 36

# Input: height = [2,2,2]
# Output: 4


def maxArea(heights):

    n = len(heights)

    l,r = 0,n-1

    max_area = (r-l)*min(heights[l], heights[r])    # Initial area

    while l < r:

        if heights[l] > heights[r]:     # We move the smaller side into the middle 
            r-=1
        else:
            l += 1
        

        new_area = (r-l)*min(heights[l], heights[r])
        max_area = max(max_area, new_area)

    return max_area


height = [1,7,2,5,4,7,3,6]
height = [2,2,2]


print(maxArea(height))