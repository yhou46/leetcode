import random
from collections import deque, OrderedDict
from typing import Dict, List, Optional, Self

"""
Description: Number of connected component in undirected graph
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.



Example 1:


Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1


Constraints:

1 <= n <= 2000
1 <= edges.length <= 5000
edges[i] = [ai, bi]
ai != bi
There are no repeated edges.
"""
class UnionFind:
    def __init__(self, n) -> None:
        self.parent: List[int] = [ i for i in range(n) ]

        # The depth of root, for optimization
        self.rank: List[int] = [ 0 for _ in range(n) ]

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            # Already same root
            return False

        if self.rank[root_x] > self.rank[root_y]:
            root_x, root_y = root_y, root_x

        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_y] += 1
        self.parent[root_x] = root_y

        return True


    def find(self, x: int) -> int:
        if self.parent[x] != x:
            # Optimization: shrink the depth of tree
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

class Solution:
    """
    Graph related questions:
    3 approaches:

    - Use BFS to traverse the graph. From each node and visit all connected nodes and mark them as visited. Do the count after each BFS

    - Use DFS to traverse the graph. Similar to BFS

    - Use union find. Then count the number of roots for all nodes. Check Union Find for more details
    """
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for edge in edges:
            uf.union(edge[0], edge[1])

        root_set: set[int] = set()

        for i in range(n):
            root_set.add(uf.find(i))

        return len(root_set)

if __name__ == "__main__":
    # Run the solution code here
    pass