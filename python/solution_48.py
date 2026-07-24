from typing import List
"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.


"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        if length > 0 and len(matrix[0]) != length:
            raise ValueError("matrix is not square")
        x = 0
        n = length
        while(n > 1):
            # for (x, x) and n, need to swap:
            # (x, x), (x, x+n-1), (x+n-1, x+n-1), (x+n-1, x)
            for i in range (0, n-1):
                temp = matrix[x][x+i]
                matrix[x][x+i] = matrix[x+n-1-i][x]
                print(f"temp: {temp}")

                temp2 = matrix[x+i][x+n-1]
                matrix[x+i][x+n-1] = temp
                print(f"temp2: {temp2}")

                temp3 = matrix[x+n-1][x+n-1-i]
                matrix[x+n-1][x+n-1-i] = temp2
                print(f"temp3: {temp3}")

                matrix[x+n-1-i][x] = temp3
            x += 1
            n -= 2


if __name__ == "__main__":
    s = Solution()
    input = [
        [2,29,20,26,16,28],
        [12,27,9,25,13,21],
        [32,33,32,2,28,14],
        [13,14,32,27,22,26],
        [33,1,20,7,21,7],
        [4,24,1,6,32,34],
    ]

    expected = [
        [7,4,1],
        [8,5,2],
        [9,6,3],
    ]

    s.rotate(input)
    print(input)