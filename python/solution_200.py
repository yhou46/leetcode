import random
from collections import deque, OrderedDict
from typing import List, Optional

"""
Description: Number of islands
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])

        count = 0
        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j] == "1":
                    count += 1
                    # Mark all connected points to 0
                    self.bfs(i, j, grid)
        return count

    # BFS and mark 0
    def bfs(self, x:int, y:int, grid: List[List[str]]) -> None:
        if grid[x][y] != "1":
            return

        m = len(grid)
        if m == 0:
            return None
        n = len(grid[0])

        x_direction = [-1, 1, 0, 0]
        y_direction = [0, 0, -1, 1]

        queue: deque[tuple[int, int]] = deque()

        queue.append((x,y))
        grid[x][y] = "0"


        while len(queue) > 0:
            point: tuple[int, int] = queue.popleft()
            for i in range(0,len(x_direction)):
                new_x = point[0] + x_direction[i]
                new_y = point[1] + y_direction[i]

                if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n and grid[new_x][new_y] == "1":
                    queue.append((new_x, new_y))
                    grid[new_x][new_y] = "0"
        return


if __name__ == "__main__":
    # Run the solution code here
    pass