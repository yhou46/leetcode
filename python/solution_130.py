import random
import heapq
from collections import deque, defaultdict, OrderedDict
from typing import Dict, List, Optional, Self, Tuple

"""
Description: Surrounded regions
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. Such regions are completely enclosed by 'X' cells.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.



Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:


In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:

Input: board = [["X"]]

Output: [["X"]]



Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
"""
class Solution:
    """
    We want to modify "O" that is surrounded and to find if a point is surrounded, we need to do traversal from a "O" and see if we hit any borders.

    Or we do it in the opposite way: we check borders and if it is a "O", we traverse from that point and mark all connected points to be visited. After checking all 4 borders, we can just traverse the board and if it is a "O" and not visited before (in the border traversal), then it is surrounded

    """
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return
        n = len(board[0])

        visited: List[List[bool]] = [[False for _ in range(n)] for _ in range(m)]

        # First and last row:
        for j in range(n):
            if board[0][j] == "O":
                self.bfs(
                    0,
                    j,
                    board,
                    visited,
                )

            if board[m-1][j] == "O":
                self.bfs(
                    m-1,
                    j,
                    board,
                    visited,
                )
        #print(visited)

        # First and last column
        for i in range(m):
            if board[i][0] == "O":
                self.bfs(
                    i,
                    0,
                    board,
                    visited,
                )
            if board[i][n-1] == "O":
                self.bfs(
                    i,
                    n-1,
                    board,
                    visited,
                )

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and not visited[i][j]:
                    board[i][j] = "X"
        return

    def bfs(self, x: int, y: int, board: List[List[str]], visited: List[List[bool]]) -> None:
        if visited[x][y]:
            return

        m = len(board)
        if m == 0:
            return
        n = len(board[0])

        x_direction = [-1, 1, 0, 0]
        y_direction = [0, 0, -1, 1]

        queue: deque[Tuple[int, int]] = deque()

        queue.append((x, y))
        visited[x][y] = True
        while len(queue) > 0:
            x, y = queue.popleft()

            for i in range(len(x_direction)):
                new_x = x + x_direction[i]
                new_y = y + y_direction[i]

                if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n \
                    and not visited[new_x][new_y] and board[new_x][new_y] == "O":
                    queue.append((new_x, new_y))
                    visited[new_x][new_y] = True
        return

if __name__ == "__main__":
    # Run the solution code here
    pass