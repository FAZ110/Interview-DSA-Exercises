'''
You are given an integer array coins representing coins of different 
denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount 
representing a target amount of money.

Return the number of distinct combinations that total up to amount. 
If it's impossible to make up the amount, return 0.

You may assume that you have an unlimited number of each coin and 
that each value in coins is unique.
'''

# EXAMPLE

# Input: amount = 4, coins = [1,2,3]
# Output: 4

# Input: amount = 7, coins = [2,4]
# Output: 0


def change(amount, coins):

    dp = [0 for _ in range(amount+1)]
    
    dp[0] = 1
    
    for coin in coins:  # Proces coins first to avoid duplicates etc. [1,2] and [2,1] combinations
        for i in range(coin, amount+1):
            dp[i] += dp[i-coin]
    
    return dp[amount]


amount = 4
coins = [1,2,3]

print(change(amount, coins))