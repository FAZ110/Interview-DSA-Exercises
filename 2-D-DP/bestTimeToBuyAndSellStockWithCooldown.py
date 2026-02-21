'''
You are given an integer array prices where prices[i] is the price 
of NeetCoin on the ith day.

You may buy and sell one NeetCoin multiple times with the following restrictions:

    After you sell your NeetCoin, you cannot buy another one on the next day (i.e., there is a cooldown period of one day).
    You may only own at most one NeetCoin at a time.

You may complete as many transactions as you like.

Return the maximum profit you can achieve.
'''

# EXAMPLES

# Input: prices = [1,3,4,0,4]
# Output: 6

# Input: prices = [1]
# Output: 0


def maxProfit(prices):
    if not prices:
        return 0
    
    hold = float('-inf')    # Profit, when we hold a stock 
    sell = 0                # Profit after sell (force cooldown)
    rest = 0                # Profit when we can buy

    for price in prices:
        prev_hold = hold

        hold = max(hold, rest - price)  # buy or hold

        new_sell = prev_hold + price    # sell what we are holding (prev_hold because we can't sell on the same day)

        rest = max(rest, sell)  # rest after buy or continue resting
        sell = new_sell     # update sell state for next iteration
    
    return max(sell, rest)

