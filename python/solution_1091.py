import random
from collections import deque, OrderedDict
from typing import List, Dict

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1

        queue: deque[List[int]] = deque() # each element is x,y, length

        n = len(grid)
        visited: Dict[str, int] = {} # point hash -> length

        def get_point_hash(x: int, y: int) -> str:
            return f"{x},{y}"

        queue.append([0,0,1])
        visited[get_point_hash(0,0)] = 1
        while len(queue) > 0:
            # Need to do popleft to simulate the queue behavior
            point: List[int] = queue.popleft()
            x = point[0]
            y = point[1]
            current_length = point[2]

            if x == n-1 and y == n-1:
                return current_length

            move_x = [-1, -1, 0, 1, 1, 1, 0, -1]
            move_y = [0, 1, 1, 1, 0, -1, -1, -1]

            for i in range(len(move_x)):
                new_x = x + move_x[i]
                new_y = y + move_y[i]

                if new_x >= 0 and new_x < n and new_y >= 0 and new_y < n and grid[new_x][new_y] == 0:
                    print(f"new point: {new_x}, {new_y}, len: {current_length}")
                    point_hash = get_point_hash(new_x, new_y)
                    if point_hash not in visited:
                        print(f"add new point: {new_x}, {new_y}, len: {current_length+1}")
                        visited[point_hash] = current_length+1
                        queue.append([new_x, new_y, current_length+1])

        return -1






if __name__ == "__main__":
    # Run the solution code here
    #input = [[0,1],[1,0]]
    #input = [[0,0,0],[1,1,0],[1,1,0]]
    #input = [[0,0,0],[0,0,0],[0,0,0]]
    input = [[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]

    s = Solution()
    print(s.shortestPathBinaryMatrix(input))