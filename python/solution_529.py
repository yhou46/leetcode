import random
from collections import deque, OrderedDict
from typing import List, Dict, Optional

"""
Description: Minesweeper
Let's play the minesweeper game (Wikipedia, online game)!

You are given an m x n char matrix board representing the game board where:

'M' represents an unrevealed mine,
'E' represents an unrevealed empty square,
'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),
digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
'X' represents a revealed mine.
You are also given an integer array click where click = [clickr, clickc] represents the next click position among all the unrevealed squares ('M' or 'E').

Return the board after revealing this position according to the following rules:

If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.


Example 1:


Input: board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]
Output: [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
Example 2:


Input: board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]], click = [1,2]
Output: [["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 50
board[i][j] is either 'M', 'E', 'B', or a digit from '1' to '8'.
click.length == 2
0 <= clickr < m
0 <= clickc < n
board[clickr][clickc] is either 'M' or 'E'.
"""
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if len(click) < 2:
            raise ValueError(f"Invalid click len: {len(click)}")
        x = click[0]
        y = click[1]

        if board[x][y] == "M":
            board[x][y] = "X"
            return board

        if board[x][y] == "E":
            # BFS to set the board
            self.bfs(board, click)
            return board

        # Other scenarios, no change
        return board

    def bfs(self, board: List[List[str]], click: List[int]) -> None:
        if len(board) == 0:
            raise ValueError(f"Invalid board size: {len(board)}")
        m = len(board)
        n = len(board[0])

        visited: List[List[bool]] = [[False for _ in range(n)] for _ in range(m)]


        queue: deque[tuple[int, int]] = deque()

        queue.append((click[0], click[1]))
        visited[click[0]][click[1]] = True

        while len(queue) > 0:
            x, y = queue.popleft()

            # 8 directions
            direction_x = [-1, -1, 0, 1, 1,  1,  0, -1]
            direction_y = [ 0,  1, 1, 1, 0, -1, -1, -1]

            # Count adjacent mines for all directions
            adjacent_count = 0
            for i in range(len(direction_x)):
                new_x = x + direction_x[i]
                new_y = y + direction_y[i]

                if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n:
                    if board[new_x][new_y] == "M":
                        adjacent_count += 1
                    """
                    Do not push point to queue here since we do not know the mine count yet
                    """

            # Update board
            if adjacent_count == 0:
                board[x][y] = "B"
            else:
                board[x][y] = f"{adjacent_count}"

            """
            Important: only proceed if the current point is B, if it has a number, we should stop here
            """
            # Push only when the point is B:
            for i in range(len(direction_x)):
                new_x = x + direction_x[i]
                new_y = y + direction_y[i]

                if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n:
                    if not visited[new_x][new_y] and board[x][y] == "B":
                        queue.append((new_x, new_y))
                        visited[new_x][new_y] = True





if __name__ == "__main__":
    # Run the solution code here
    pass