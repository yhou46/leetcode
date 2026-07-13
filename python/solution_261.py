import random
from collections import deque, OrderedDict
from typing import Dict, List, Optional, Self

"""
Description: Graph valid tree
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.



Example 1:


Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false


Constraints:

1 <= n <= 2000
0 <= edges.length <= 5000
edges[i].length == 2
0 <= ai, bi < n
ai != bi
There are no self-loops or repeated edges.
"""
class Solution:
    """
    A graph is a tree if:
        - no cycles in the graph
        - every node is reachable

    To check if a graph has a cycle, a DFS search can be used and if a node visted before is visited again, then there is a cycle. then use the visited list to check if all nodes are reachable

    Notice that it is a undirected graph and when we create adjacent matrix, node 0 and node 1 are connected in both directions, then we should reset the node1 -> node0 edge to False when visting node0 -> node1, otherwise it outputs wrong results

    Other solutions:
    UnionFind?

    """
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # Create adjacent matrix:
        adjacent_matrix: List[List[bool]] = [[False for _ in range(n)] for _ in range(n)]
        for edge in edges:
            n1 = edge[0]
            n2 = edge[1]
            adjacent_matrix[n1][n2] = True
            adjacent_matrix[n2][n1] = True

        visited: List[bool] = [False for _ in range(n)]
        has_cycle = self.has_cycle_dfs(
            0,
            adjacent_matrix,
            visited,
        )

        if has_cycle:
            return False

        # Check if all nodes are visited
        for flag in visited:
            if not flag:
                return False
        return True


    def has_cycle_dfs(self, node: int, adjacent_matrix: List[List[bool]], visited: List[bool]) -> bool:
        if visited[node]:
            print(f"has cycle: node: {node}")
            return True

        visited[node] = True
        edges = adjacent_matrix[node]

        for i in range(0, len(edges)):
            if edges[i]:
                # Has to reset the edge since it is undirected graph and we already visited node -> i, we reset i -> node to prevent giving wrong is_cycle result.
                adjacent_matrix[i][node] = False

                flag = self.has_cycle_dfs(i, adjacent_matrix, visited)
                if flag:
                    # print(f"has cycle in loop: node: {node}, edge: {i}")
                    return True
        return False

if __name__ == "__main__":
    # Run the solution code here
    pass