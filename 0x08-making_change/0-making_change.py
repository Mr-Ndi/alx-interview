#!/usr/bin/python3
"""
A module that contains the function to solves the coin issue
"""


def makeChange(coins, total):
    """
    A function to determine the fewest number of coins
    needed to meet a given amount total.
    """
    if total <= 0:
        return 0
    # Initialize a list to store the minimum coins
    # needed for each amount up to total
    mincoin = [float('inf')] * (total + 1)
    mincoin[0] = 0  # Base case: 0 coins are needed to make the total of 0

    # Iterate over each coin
    for coin in coins:
        # Update the dp array for each amount from coin to total
        for amount in range(coin, total + 1):
            mincoin[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, it means total cannot be met
    return dp[total] if dp[total] != float('inf') else -1
