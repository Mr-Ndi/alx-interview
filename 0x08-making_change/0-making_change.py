#!/usr/bin/python3
"""
A module that contains the function to solves the coin issue
"""


def makeChange(coins, total):
    """
    A function to determine the fewest number of coins
    needed to meet a given amount total. through the following phase:
    - Initialize a list to store the minimum coins
    - needed for each amount up to total
    - Base case: 0 coins are needed to make the total of 0
    - Iterate over each coin
    - Update the mincoin array for each amount from coin to total
    - If mincoin[total] is still infinity, it means total cannot be met
    """
    if total <= 0:
        return 0
    mincoin = [float('inf')] * (total + 1)
    mincoin[0] = 0
    for coin in coins:
        for amount in range(coin, total + 1):
            mincoin[amount] = min(mincoin[amount], mincoin[amount - coin] + 1)
    return mincoin[total] if mincoin[total] != float('inf') else -1
