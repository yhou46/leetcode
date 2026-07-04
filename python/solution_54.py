import random
from collections import deque, OrderedDict
from typing import List, Dict, Optional

"""
Description: TBD
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result: List[int] = []

        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])

        """
        Idea is moving point x,y, but easy to have bugs
        Scenario:
            matrix is 1 * m
            matrix is n * 1
            matrix is 1 * 1
        """
        x = 0
        y = 0

        while m > 0 and n > 0:
            print(f"m: {m}, n: {n}, x: {x}, y: {y}")

            # right
            for _ in range(0,n):
                print(f"x: {x}, y: {y}")
                result.append(matrix[x][y])

                # Notice that whether to put y += 1 before or after the append. When going left, initial x,y should be processed first. If put y+=1 after append, then need to move y back since y is invalid at the end of loop
                y += 1
            # Back one step since y is n if enters the loop
            y -= 1


            # down
            for _ in range(0, m-1):
                x = x + 1
                print(f"x: {x}, y: {y}")
                result.append(matrix[x][y])


            # left
            # If m is 1: 1 row, then we should not go left since it is already covered by the right loop
            if m > 1:
                for _ in range(0, n-1):
                    y = y - 1
                    print(f"x: {x}, y: {y}")
                    result.append(matrix[x][y])


            # up
            # If n is 1 column, then we should not go up since it is coverd by the down loop
            if n > 1:
                for _ in range(0, m-2):
                    x = x - 1
                    print(f"x: {x}, y: {y}")
                    result.append(matrix[x][y])



            m = m - 2
            n = n - 2
            y = y + 1

        return result

    def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:

        """
        A different idea, use 4 guards for the point range, instead of moving point
        Comparing to moving point, no need to do back step but still need special check for 1 row and 1 col check when doing left and up turn
        """
        top = 0
        bottom = len(matrix) # bottom is exclusive
        if bottom == 0:
            return []

        left = 0
        right = len(matrix[0]) # right is exclusive

        result: List[int] = []

        while left < right and top < bottom:
            # right
            for j in range(left, right):
                result.append(matrix[top][j])

            top += 1

            # Down
            for i in range(top, bottom):
                result.append(matrix[i][right-1])
            right -= 1

            # left
            # Still need the guard to handle one row case
            if top < bottom:
                for j in range(right-1, left-1, -1):
                    result.append(matrix[bottom-1][j])
                bottom -= 1

            # up
            # Still need the guard to handle one col case
            if left < right:
                for i in range(bottom-1, top-1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result

    """
    Given the spiral order list and matrix dimension m and n, return the original matrix
    """
    def returnMatrix(self, input: List[int], m: int, n: int) -> List[List[int]]:


        top = 0
        bottom = m # bottom is exclusive
        if bottom == 0:
            return []

        left = 0
        right = n # right is exclusive

        new_matrix = [[0 for _ in range(right)] for _ in range(bottom)]
        pos = 0


        while left < right and top < bottom:
            # right
            for j in range(left, right):
                new_matrix[top][j] = input[pos]
                pos += 1

            top += 1

            # Down
            for i in range(top, bottom):
                new_matrix[i][right-1] = input[pos]
                pos += 1
            right -= 1

            # left
            # Still need the guard to handle one row case
            if top < bottom:
                for j in range(right-1, left-1, -1):
                    #result.append(matrix[bottom-1][j])
                    new_matrix[bottom-1][j] = input[pos]
                    pos += 1
                bottom -= 1

            # up
            # Still need the guard to handle one col case
            if left < right:
                for i in range(bottom-1, top-1, -1):
                    # result.append(matrix[i][left])
                    new_matrix[i][left] = input[pos]
                    pos += 1


                left += 1

        return new_matrix

if __name__ == "__main__":
    # Run the solution code here
    s = Solution()
    # input = [
    #     [1,2,3],
    #     [4,5,6],
    #     [7,8,9],
    # ]

    # input = [
    #     [1,2],
    #     [3,4],
    #     [5,6],
    # ]

    input = [
        [1],
        [2],
        [3],
    ]

    # input = [
    #     [1,2,3]
    # ]

    result = s.spiralOrder2(input)
    print(s.returnMatrix(result, len(input), len(input[0])))