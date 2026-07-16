import random
from collections import deque, OrderedDict
from typing import Dict, List, Optional, Self

"""
Description: Coin change
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0


Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""
class Solution:
    """
    Thinking:
    if we substract 1 type of coin from the amount, then we shrink the problem to a smaller size.

    Example:
    Input: coins = [1,2,5], amount = 11

    We have 3 coins, if we substract 1,2, 5 from amount, we have 3 sub problems:
    amount 10 with coin 1 used
    amount 9 with coin 2 used
    amount 6 with coin 5 used

    Obviously we can use a recursion to do it. the min coin number of amount is the min value of amount - {each coin value}.

    We need to remember the results to avoid duplicated calulation.

    Recursion with memorization can also be thought like a DP problem:

    dp[i] is the min number of coins that can reach amount of i
    dp[i] = min of dp[i-{coin value}]

    here we can only get dp[{coin}] = 1 as initial value, and other value is -1
    For example, coin has [2,3,5], then dp[1] = -1 since it is smaller than the smallest coin value
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp: List[int] = [ -1 for _ in range(0, amount+1) ]
        dp[0] = 0 # amount 0 need no coins
        for coin in coins:
            if coin < len(dp):
                dp[coin] = 1

        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0 and dp[i-coin] != -1:
                    if dp[i] != -1:
                        dp[i] = min(dp[i], dp[i-coin] + 1)
                    else:
                        dp[i] = dp[i-coin] + 1
            print(f"i: {i}, dp: {dp[i]}")
        return dp[amount]

if __name__ == "__main__":
    # Run the solution code here
    pass