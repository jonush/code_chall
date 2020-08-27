"""
There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:

In each step, you will choose any 3 piles of coins (not necessarily consecutive).
Of your choice, Alice will pick the pile with the maximum number of coins.
You will pick the next pile with maximum number of coins.
Your friend Bob will pick the last pile.
Repeat until there are no more piles of coins.
Given an array of integers piles where piles[i] is the number of coins in the ith pile.

Return the maximum number of coins which you can have.
"""

def maxCoins(piles):
    max_coins = 0
    max_choices = len(piles) // 3
    
    piles.sort()
    
    for i in range(1, max_choices + 1):
        max_coins += piles[-2 * i]

    # return total of all coins[1]
    return max_coins