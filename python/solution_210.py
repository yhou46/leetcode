import random
from collections import deque, defaultdict, OrderedDict
from typing import Dict, List, Optional, Self, Tuple

"""
Description: Course schedule 2
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]


Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
"""
class Solution:
    """
    This problem is exactly a topology sort problem where each course is a node and each prerequisite is a edge. The goal is to find a valid topogoly sort order.

    Or it can be solved by DFS
    """
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degrees: List[int] = [0 for _ in range(numCourses)]
        graph: List[List[bool]] = [[False for _ in range(numCourses)] for _ in range(numCourses)]

        for edge in prerequisites:
            in_degrees[ edge[0] ] += 1
            graph[edge[1]][edge[0]] = True

        queue: deque[int] = deque()

        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)

        result: List[int] = []
        while len(queue) > 0:
            node = queue.popleft()
            result.append(node)

            for i in range(numCourses):
                if graph[node][i]:
                    in_degrees[i] -= 1
                    if in_degrees[i] == 0:
                        queue.append(i)

        # Detect loop
        if len(result) < numCourses:
            return []
        else:
            return result

if __name__ == "__main__":
    # Run the solution code here
    pass