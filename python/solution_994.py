import random
from collections import deque, defaultdict, OrderedDict
from typing import Dict, List, Optional, Self, Tuple

"""
Description: Rotting oranges
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.



Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""
class Solution:
    """
    The goal is to find the min minute that the state of the grid does not change.
    We can use BFS here: the starting point is all rotting orange point. BFS guarantees that the fresh orange point is visited in minimum steps (step is minute in this question)
    And we should only visit fresh orange point and mark it rotting when visited, so we never revisited same point (no need to visited matrix)
    """
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0:
            return -1
        n = len(grid[0])

        # Each element is x, y, minute
        total_orange = 0
        queue: deque[Tuple[int, int, int]] = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
                if grid[i][j] != 0:
                    total_orange += 1

        result = 0
        while len(queue) > 0:
            x, y, minute = queue.popleft()
            total_orange -= 1

            dir_x = [0, 1, 0, -1]
            dir_y = [-1, 0, 1, 0]

            for i in range(len(dir_x)):
                new_x = x + dir_x[i]
                new_y = y + dir_y[i]
                if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n and grid[new_x][new_y] == 1:
                    new_minute = minute + 1
                    result = max(result, new_minute)
                    queue.append((new_x, new_y, new_minute))
                    grid[new_x][new_y] = 2

        if total_orange != 0:
            return -1
        else:
            return result

if __name__ == "__main__":
    # Run the solution code here
    pass