import random
from collections import deque, OrderedDict
from typing import List

"""
70.  Climbing stairs
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45
"""
class Solution:
    """
    DP solution:
    dp[i] is the # fo ways from 0 to position i
    Since i can be reached by 1 or 2 steps
    dp[i] = dp[i-1] + dp[i-2], from position 0 to n (n+1 entries)
    dp[0] = 1
    dp[1] = 1
    """
    def climbStairs(self, n: int) -> int:
        dp: List[int] = [1 for _ in range(n+1)]

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

if __name__ == "__main__":
    # Run the solution code here
    pass