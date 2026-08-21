import random
import heapq
from collections import deque, defaultdict, OrderedDict
from typing import Dict, List, Optional, Self, Tuple

"""
Description: IPO
Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.

Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.

The answer is guaranteed to fit in a 32-bit signed integer.



Example 1:

Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
Output: 4
Explanation: Since your initial capital is 0, you can only start the project indexed 0.
After finishing it you will obtain profit 1 and your capital becomes 1.
With capital 1, you can either start the project indexed 1 or the project indexed 2.
Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
Example 2:

Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
Output: 6


Constraints:

1 <= k <= 105
0 <= w <= 109
n == profits.length
n == capital.length
1 <= n <= 105
0 <= profits[i] <= 104
0 <= capital[i] <= 109
"""
class Solution:
    """
    Apparently we should do the project that has max profix and within our capital for each turn. And each turn will give us more capital that allow us to do more projects.
    So with the start capital w, we should get the max profix of all projects that their capital is equla or less than w.
    Instead of scan the input array again and again to find these candidate, we can just sort the combined array (capital, profit) based on capital. Then we just need to loop it to find all available projects. And among them, we need to max profit one, so we can use a heap to store these candidate and then get the max profit one in O(1) time
    """
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Element is [capital, profit]
        capital_profit_list: List[Tuple[int, int]] = []

        for i in range(len(profits)):
            capital_profit_list.append((capital[i], profits[i]))

        capital_profit_list.sort()

        # Each element is profit
        max_heap: List[int] = []

        count = 0
        index = 0
        current_capital = w
        while count < k:

            # Get all projects that requires capital less than or equal to current capital
            if index < len(capital_profit_list): # important: we need check if index is out of range, or we can put it in while loop
                while capital_profit_list[index][0] <= current_capital:
                    # Python only has min heap so need to negate the value to make it max heap
                    heapq.heappush(max_heap, -1 * capital_profit_list[index][1])
                    index += 1
                    if index >= len(capital_profit_list):
                        break

            # Important: if nothing in heap, it means we cannot proceed, should exit. It should be here since it is possible that we push nothing to heap and heap is initially empty
            if len(max_heap) == 0:
                break
            profit = -1 * heapq.heappop(max_heap)
            current_capital += profit
            count += 1


        return current_capital

if __name__ == "__main__":
    # Run the solution code here
    pass