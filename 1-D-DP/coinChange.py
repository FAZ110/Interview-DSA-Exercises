'''
You are given an integer array coins representing coins of different 
denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount 
representing a target amount of money.

Return the fewest number of coins that you need to make up the exact 
target amount. If it is impossible to make up the amount, return -1.

You may assume that you have an unlimited number of each coin.
'''

# EXAMPLES

# Input: coins = [1,5,10], amount = 12
# Output: 3

# Input: coins = [2], amount = 3
# Output: -1

# Input: coins = [1], amount = 0
# Output: 0

# IDEA
'''
If we have some value under dp[i-coin] then we can use coin to move
to dp[i], we will have value+1 there
'''


def coinChange(coins, amount):

    n = len(coins)

    if n == 0:
        return -1
    if amount < 1:
        return 0

    dp = [float('inf')]*(amount+1)

    for coin in coins:  # setup the starting point
        if -1<coin<amount+1:
            dp[coin] = 1
        
    for i in range(amount+1):   # main loop
        for coin in coins:
            if -1 < i - coin < amount+1: # checking boundaries restrictions
                dp[i] = min(dp[i], dp[i-coin] + 1)
        
    return -1 if dp[-1] == float('inf') else dp[-1]



coins = [1,5,10]
amount = 12
print(coinChange(coins, amount))
