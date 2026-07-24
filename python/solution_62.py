import random
from collections import deque, OrderedDict
from typing import List

"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.


"""
class Solution:
    """
    DB solltion:

    d[i][j] is # of paths from 0,0 to i,j
    d[i][j+1] = d[i][j] + d[i-1][j+1]
    d[i+1][j] = d[i][j] + d[i+1][j-1]
    d[i+1][j+1] = d[i][j+1] + d[i+1][j]

    In theory, we need a m*n table. But from calculation, to calculate d[i+1][j+1]
    we only need its previous value (d[i][j+1]) and element before it.
    So in theory, we only need 1*n table and reusing previous value
    """
    def uniquePaths(self, m: int, n: int) -> int:
        dp: List[int] = [1 for _ in range(n)]

        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j-1]

        return dp[n-1]

if __name__ == "__main__":
    # Run the solution code here
    pass