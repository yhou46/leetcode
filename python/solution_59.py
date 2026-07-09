import random
from collections import deque, OrderedDict
from typing import Dict, List, Optional, Self

"""
Description: Spiral matrix 2
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.



Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]


Constraints:

1 <= n <= 20
"""
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix: List[List[int]] = [[0 for _ in range(n)] for _ in range(n)]

        number = 1

        top = 0
        bottom = n-1
        left = 0
        right = n-1

        while left <= right and top <= bottom:

            # left
            for i in range(left, right+1):
                matrix[top][i] = number
                number += 1
            top += 1

            # Down
            for i in range(top, bottom+1):
                matrix[i][right] = number
                number += 1
            right -= 1

            # right
            # If it is m*n then should only do right direction if top < bottom
            for i in range(right, left-1, -1):
                matrix[bottom][i] = number
                number += 1
            bottom -= 1

            # up
            # If it is m*n then should only do up direction if left < right
            for i in range(bottom, top-1, -1):
                matrix[i][left] = number
                number += 1
            left += 1

        return matrix

if __name__ == "__main__":
    # Run the solution code here
    pass