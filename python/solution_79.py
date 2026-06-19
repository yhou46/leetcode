import random
from collections import deque, OrderedDict
from typing import List

"""
Word Search
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        visited: List[List[bool]] = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                match = self.recursion(
                            word,
                            0,
                            i,
                            j,
                            board,
                            visited,
                        )
                if match:
                    return True

        return False

    def recursion(self,
        word: str,
        start: int,
        x: int,
        y: int,
        board: List[List[str]],
        visited:List[List[bool]]) -> bool:

        if board[x][y] != word[start]:
            return False

        # End of string
        if start == len(word)-1:
            return True

        move_x = [-1, 0, 1, 0]
        move_y = [0, 1, 0, -1]

        m = len(board)
        n = len(board[0])

        for i in range(len(move_x)):
            new_x = x + move_x[i]
            new_y = y + move_y[i]

            visited[x][y] = True

            if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n and not visited[new_x][new_y]:
                match = self.recursion(
                    word,
                    start+1,
                    new_x,
                    new_y,
                    board,
                    visited,
                )

                if match:
                    return True
            visited[x][y] = False
        return False

if __name__ == "__main__":
    # Run the solution code here
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]

    word = "SEE"

    s = Solution()
    print(s.exist(board, word))