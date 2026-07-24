import random
from collections import deque, OrderedDict
from typing import List, Optional

"""
Description: Best time to buy and sell stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""
class Solution:
    """
    If we only do one transaction, the goal is to find the max price and min price where max price must appear after min price.
    When we loop the price list, if we keep the min price so far, then we can use current price - min_price, update the profix if it is larger. It natuarally satisfy the condition that max price appear after min price
    """
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        result = 0
        min_price = prices[0]

        for i in range(1, len(prices)):
            result = max(prices[i] - min_price, result)
            min_price = min(min_price, prices[i])

        return result

if __name__ == "__main__":
    # Run the solution code here
    pass