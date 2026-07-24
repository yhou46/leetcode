import random
from collections import deque, OrderedDict
from typing import Dict, List, Optional, Self

"""
Description: Pacific Atlantic water flow

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.



Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.


Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105
"""
class Solution:

    """
    Thinking process:
    At first, a brute force solution is to do DFS or BFS travsal for each cell and check if it can reach both edges. But each traverse takes m*n time. And we have some duplicated traversal.
    Example:
    [
        [1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4],
    ]

    If we start from (2,2), there are at least 2 paths to Pacific upper edge, 5 -> 4 -> 2 ->2 and 5 -> 3 -> 2 -> 2 and they share the path. So can we remember the results during the travsal?
    It is hard. Why?
    If one node reaches the edge, then the path from start to the node can reach the edge. But we need to remember the path and only update value of the nodes along the path. It is hard unless we remember the path along recursion (has to use DFS in this case).
    Also there is one scenario: what if it reaches the edge but can flow to other direction?
    Example:
    -----Pacific edge------
      3 2
    5 4 1
        1
    ----Atlantic edge------
    In this case, when it reaches 2 at the upper bound, the whole path can reach Pacific, but when it goes down to the middle 1, it cannot reach Pacific. So we need to remember the path when node reaches edge and update all node status along the paths.

    Can we think in a different direction? Instead of starting from each point and find whether it can reach the edges, we start from edges. From edges, we do traverse, and only proceed if heights[adjacent next cell] > heights[current cell], then we build a visited matrix from edges. We can do it twice and find the intersection of 2 visited matrix. that is the result.
    """
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        if m == 0:
            raise ValueError(f"Empty heights: {heights}")
        n = len(heights[0])
        pacific_visited: List[List[bool]] = [[False for _ in range(n)] for _ in range(m)]
        atlantic_visited: List[List[bool]] = [[False for _ in range(n)] for _ in range(m)]

        # Start from pacific edges
        for j in range(n):
            # Visit from Pacific edges
            self.dfs(0, j, heights, pacific_visited)

            # Vist from atlantic edges
            self.dfs(m-1, j, heights, atlantic_visited)

        for i in range(m):
            # Visit from Pacific edges
            self.dfs(i, 0, heights, pacific_visited)

            # Vist from atlantic edges
            self.dfs(i, n-1, heights, atlantic_visited)

        result: List[List[int]] = []
        for i in range(m):
            for j in range(n):
                if pacific_visited[i][j] and atlantic_visited[i][j]:
                    result.append([i, j])
        return result

    def dfs(
        self,
        x: int,
        y: int,
        heights: List[List[int]],
        visited: List[List[bool]],
        ) -> None:

        if visited[x][y]:
            return

        stack: deque[List[int]] = deque()
        stack.append([x,y])
        visited[x][y] = True

        m = len(heights)
        if m == 0:
            raise ValueError(f"Empty heights: {heights}")
        n = len(heights[0])

        while len(stack) > 0:
            point = stack.pop()

            x = point[0]
            y = point[1]

            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]

            for i in range(len(dx)):
                new_x = x + dx[i]
                new_y = y + dy[i]

                if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n and not visited[new_x][new_y]:
                    if heights[new_x][new_y] >= heights[x][y]:
                        stack.append([new_x, new_y])
                        visited[new_x][new_y] = True
        return

if __name__ == "__main__":
    # Run the solution code here
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    s = Solution()

    print(s.pacificAtlantic(heights))