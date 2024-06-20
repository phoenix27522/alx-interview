import sys

def makeChange(coins, total):
    '''
    Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    '''
    if total <= 0:
        return 0

    # Create a list to store the minimum number of coins for each value up to total
    dp = [sys.maxsize] * (total + 1)
    dp[0] = 0  # Base case: no coins are needed to make 0

    # Iterate through all amounts from 1 to total
    for i in range(1, total + 1):
        # Try every coin that doesn't exceed the current amount
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still sys.maxsize, it means it's not possible to make the total with given coins
    return dp[total] if dp[total] != sys.maxsize else -1
