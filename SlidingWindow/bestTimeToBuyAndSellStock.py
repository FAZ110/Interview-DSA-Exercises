'''
You are given an integer array prices where prices[i] is the 
price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a 
different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to 
not make any transactions, in which case the profit would be 0.
'''

# EXAMPLES

# Input: prices = [10,1,5,6,7,1]
# Output: 6


# Input: prices = [10,8,7,5,2]
# Output: 0

# Idea
# We need to find the largest diff between two numbers on the array,
# such that the value closer to the start is smaller  

def maxProfit(prices):

    n = len(prices)
    max_profit = 0

    l = 0   
    for r in range(1, n):
        if prices[r] <= prices[l]:  # If we find smaller value we change the l (cannot find larger diff from this l anymore)
            l = r
        else:
            max_profit = max(max_profit, prices[r]-prices[l])


    return max_profit

prices = [10,1,5,6,7,1]
# prices = [10,8,7,5,2]
# prices=[1,2]
print(maxProfit(prices))