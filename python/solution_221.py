import random
import heapq
from collections import deque, defaultdict, OrderedDict
from typing import Dict, List, Optional, Self, Tuple

"""
Description: Maximam square
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.



Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Example 2:


Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.
"""
class Solution:
    """
    dp[i][j] max side length that a squaure whose bottom right is at i,j
    dp[i][j] =
        - if matrix[i][j] == 0, dp[i][j] = 0
        - if matrix[i][j] == 1, dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

    dp[0][0] = matrix[0][0]
    dp[0][j] = matrix[0][j]
    dp[i][0] = matrix[i][0]

    Why dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1] ?
    Example:
    [
        1, 1
        0, 1
    ]
    Bottom right dp[i][j] depends on it previous dp[i-1][j-1] but also dp[i-1][j] and dp[i][j-1]
    If dp[i-1][j-1] is 3*3, dp[i][j] could be 4*4 only when cell of [i][j-1], [i][j-2], [i][j-3] are 1 and cell [i-1][j], [i-2][j], [i-3][j] are also 1, which is equivalent to dp[i-1][j] and dp[i][j-1]
    """
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        dp: List[List[int]] = [ [0 for _ in range(n)] for _ in range(m) ]

        max_side = 0
        for j in range(n):
            dp[0][j] = 1 if matrix[0][j] == "1" else 0
            max_side = max(max_side, dp[0][j])

        for i in range(m):
            dp[i][0] = 1 if matrix[i][0] == "1" else 0
            max_side = max(max_side, dp[i][0])


        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_side = max(max_side, dp[i][j])
        print(dp)
        return max_side * max_side

if __name__ == "__main__":
    # Run the solution code here
    pass