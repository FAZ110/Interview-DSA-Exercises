'''
You are given an integer array piles where piles[i] is the number of bananas 
in the ith pile. You are also given an integer h, which represents the number 
of hours you have to eat all the bananas.

You may decide your bananas-per-hour eating rate of k. Each hour, you may 
choose a pile of bananas and eats k bananas from that pile. If the pile has 
less than k bananas, you may finish eating the pile but you can not eat from 
another pile in the same hour.

Return the minimum integer k such that you can eat all the bananas within h 
hours.
'''

# EXAMPLES

# Input: piles = [1,4,3,2], h = 9
# Output: 2

# Input: piles = [25,10,23,4], h = 4
# Output: 25


import math
def minEatingSpeed(piles, h):
    n = len(piles)

    l, r = 1, max(piles) # minimum and maximum speed from the start

    while l <= r:

        mid = (l+r) // 2

        time = 0
        for i in range(n):     # We calculate the time neede to eat all the bananas with the mid speed
            time += max(1, math.ceil(piles[i]/mid)) # minimum time is always 1
        
        if time > h:    # if it takes longer than h we have to increase the speed by moveing the l boundary
            l = mid + 1
        else:   # if it takes less time we move the r boundary to optimize the speed
            r = mid - 1
    
    return l

piles = [1,4,3,2]
h = 9

piles = [25,10,23,4]
h = 4

print(minEatingSpeed(piles, h))



