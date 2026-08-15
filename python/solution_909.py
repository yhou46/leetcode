import random
from collections import deque, defaultdict, OrderedDict
from typing import Dict, List, Optional, Self, Tuple

"""
Description: Snakes and ladders
You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:

Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
The game ends when you reach the square n2.
A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 are not the starting points of any snake or ladder.

Note that you only take a snake or ladder at most once per dice roll. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
Return the least number of dice rolls required to reach the square n2. If it is not possible to reach the square, return -1.



Example 1:


Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
Output: 4
Explanation:
In the beginning, you start at square 1 (at row 5, column 0).
You decide to move to square 2 and must take the ladder to square 15.
You then decide to move to square 17 and must take the snake to square 13.
You then decide to move to square 14 and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
This is the lowest possible number of moves to reach the last square, so return 4.
Example 2:

Input: board = [[-1,-1],[-1,3]]
Output: 1


Constraints:

n == board.length == board[i].length
2 <= n <= 20
board[i][j] is either -1 or in the range [1, n2].
The squares labeled 1 and n2 are not the starting points of any snake or ladder.
"""
class Solution:
    """
    The 2-D board can actually be flatten to be 1-D array since we only care about the absolute index and snakes and ladders only connect index.

    We need to be careful about the flatten logic.
    Each index can be thought like a node, each index can proceed to next 6 index and among them, if there is snake or ladder, just go directly to the target index.

    Notice that when we arrive using ladder or snake to the target index and target index is itself another ladder, we do not use that ladder/snake. Example:
    [-1, 6, 2, 8, -1, -1, 10, -1, 2, 13, 15, -1, -1, 2, 1, -1]
    The optimal solution is -1(1) -> 10(7) ladder to 13(10) -> -1(16)
    When we arrive at 10, it is a ladder but we do not use that but continue roll the dice


    Notice: we cannot do greedy by going to the largest index (i+6) because of 2 reasons:
        - there are connections (snakes and ladder)
        - Smaller index can be a optimal solution:
            - Example: [-1, 1, 1, 1, 1, -1, 2, 20,... ]
                Assume we need to go 20(index 8) but we cannot go 2 (index 7) since it goes back to index 2, so we have to choose -1 (index 6)
    """
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board.reverse()
        board_1d: List[int] = []
        n = len(board)
        for i in range(n):
            if i % 2 == 0:
                board_1d.extend(board[i])
            else:
                board_1d.extend(reversed(board[i]))
        print(board_1d)

        # Element is index, rollDiceCount
        visited: List[bool] = [False for _ in range(len(board_1d))]
        queue: deque[Tuple[int, int]] = deque()
        queue.append((0, 0))
        visited[0] = True
        destination = n*n -1

        min_count = n*n
        while len(queue) > 0:
            index, count = queue.popleft()
            print(f"poped element: index: {index}, count: {count}")
            if index == n*n -1:
                min_count = min(min_count, count)
                print(f"reached end, count: {count}")
            else:
                range_min = min(index+1, destination)
                range_max = min(index+6, destination)

                for i in range(range_min, range_max+1):
                    # ladder or snake
                    next = board_1d[i]-1 if board_1d[i] != -1 else i

                    if not visited[next]:
                        queue.append((next, count+1))
                        visited[next] = True

        return min_count if min_count != n*n else -1


if __name__ == "__main__":
    # Run the solution code here
    #board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]

    board = [[1,1,-1],[1,1,1],[-1,1,1]]

    board = [[-1,1,2,-1],[2,13,15,-1],[-1,10,-1,-1],[-1,6,2,8]]

    # board = [[-1,10,-1,15,-1],[-1,-1,18,2,20],[-1,-1,12,-1,-1],[2,4,11,18,8],[-1,-1,-1,-1,-1]]

    s = Solution()
    print(s.snakesAndLadders(board))