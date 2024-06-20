#!/usr/bin/python3
'''Given a pile of coins of different values,
    determine the fewest number of coins needed to meet
    a given amount total.
'''

import sys


def makeChange(coins, total):
    '''
    Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    '''
    # Edge case: If total is 0 or negative, no coins are needed.
    if total <= 0:
        return 0

    # Initialize the table with sys.maxsize, which represents infinity
    table = [sys.maxsize] * (total + 1)
    table[0] = 0  # Base case: 0 coins are needed to make a total of 0

    # Iterate over all amounts from 1 to total
    for i in range(1, total + 1):
        # Try each coin to see if it can contribute to the minimum number of coins
        for coin in coins:
            if coin <= i:
                subres = table[i - coin]
                if subres != sys.maxsize and subres + 1 < table[i]:
                    table[i] = subres + 1

    # If the table entry for 'total' is still sys.maxsize, return -1
    return -1 if table[total] == sys.maxsize else table[total]
