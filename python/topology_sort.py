import random
from collections import deque, OrderedDict, defaultdict
from typing import Dict, List, Optional, Self

"""
Description: Topology sort

What is topological sort?
Topological sort is a linear ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge u → v, node u comes before node v in the ordering.
Think of it as: "If A must happen before B, then A appears earlier in the list than B."
Real-world intuition
The classic example is course prerequisites:

To take Algorithms, you need Data Structures.
To take Data Structures, you need Intro to Programming.
To take Machine Learning, you need Linear Algebra and Algorithms.

A topological sort produces a valid order to take these courses: e.g., Intro to Programming → Data Structures → Linear Algebra → Algorithms → Machine Learning.
Other examples:

Build systems (compile file A before file B if B imports A).
Task scheduling with dependencies.
Spreadsheet formula evaluation (compute cells in the right order).
Package managers (install dependencies before dependents).

Two hard requirements

Directed graph — edges have direction (u → v means u must come before v).
Acyclic — no cycles. If A depends on B and B depends on A, no valid ordering exists.

If a cycle exists, topological sort is impossible. A good implementation detects this and reports it.
"""


"""
Algorithm 1: Kahn's algorithm (BFS-based, using in-degrees)
Idea: Repeatedly remove nodes that have no incoming edges. Anything with zero dependencies can go next.
Steps:

Compute the in-degree (number of incoming edges) of every node.
Put all in-degree-0 nodes into a queue.
Pop a node, add it to the result. For each of its neighbors, decrement their in-degree. If a neighbor's in-degree hits 0, enqueue it.
Repeat until the queue is empty.
If the result contains all n nodes, you have a valid ordering. Otherwise, a cycle exists.
"""
# n: the number of nodes
# edges: [i, j] means edges from node i to node j
def topology_sort_bfs(n: int, edges: List[List[int]]) -> List[int]:
    # Important, in_degree_map must include all nodes, even the ones without any edges connected.
    # Those isolated nodes should have in-degree as zero
    in_degree_map: List[int] = [0 for _ in range(n)]
    adjacent_matrix: List[List[bool]] = [[False for _ in range(n)] for _ in range(n)]

    for edge in edges:
        u = edge[0]
        v = edge[1]
        in_degree_map[v] += 1
        adjacent_matrix[u][v] = True

    result: List[int] = []
    queue: deque[int] = deque()

    for i in range(len(in_degree_map)):
        if in_degree_map[i] == 0:
            queue.append(i)

    while len(queue) > 0:
        node = queue.popleft()
        result.append(node)

        for i in range(len(adjacent_matrix[node])):
            if adjacent_matrix[node][i]:
                in_degree_map[i] -= 1
                if in_degree_map[i] == 0:
                    queue.append(i)

    if len(result) < n:
        raise ValueError(f"Input graph has cycles: number of nodes: {n}, edges: {edges}")

    return result

def topology_sort_dfs(n: int, edges: List[List[int]]) -> List[int]:

    # 0: means not visited at all, 1: means on going dfs, 2: means already added to matrix
    visited: List[int] = [0 for _ in range(n)]

    adjacent_matrix: List[List[bool]] = [[False for _ in range(n)] for _ in range(n)]
    for edge in edges:
        u = edge[0]
        v = edge[1]
        adjacent_matrix[u][v] = True

    result: List[int] = []

    # If we want a flag like has_cycle passed in the recursion function and value being updated. We can use nonlocal inside the child function's definition:
    # like:
    #
    # def topology_sort_dfs:
    #   has_cycle = False
    #   def dfs(...):
    #       nonlocal has_cycle
    #
    # In this case, inside dfs, has_cycle is the one defined outside the function.



    def dfs(node: int, adjacent_matrix: List[List[bool]], visited: List[int], result: List[int]) -> None:
        visited[node] = 1
        for i in range(0, len(adjacent_matrix[node])):
            if adjacent_matrix[node][i]:
                if visited[i] == 1:
                    raise ValueError(f"Input graph has cycles: number of nodes: {n}, edges: {edges}")
                if visited[i] == 0:
                    dfs(i, adjacent_matrix, visited, result)

        # Important: need to append after all recursion, make sure the start node is added at the end
        result.append(node)
        visited[node] = 2

    for i in range(n):
        if visited[i] == 0:
            dfs(i, adjacent_matrix, visited, result)

    # Why reverse?
    # Because when we start at any node i, we can find the path start from i to all its connected node path, but there could be other node j that points to i.
    # the result during recursion dfs, has node i added to the end, means the order is like: [all_nodes_after_i, i], then when we visited j, j is added after i. The entire result is in reversed ordering
    result.reverse()
    return result


if __name__ == "__main__":
    # Run the solution code here

    # Simple chain: 0 -> 1 -> 2 -> 3
    result = topology_sort_dfs(4, [[3, 2], [2, 1], [1, 0]])
    print("chain -> expected: [3, 2, 1, 0], actual:", result)

    # Diamond shape: 0 -> {1, 2} -> 3
    # Note: DFS-based order differs from Kahn's/BFS order, but both are valid
    # topological orders (0 before 1 and 2; 1 and 2 before 3).
    result = topology_sort_dfs(4, [[0, 1], [0, 2], [1, 3], [2, 3]])
    print("diamond -> expected: [0, 2, 1, 3], actual:", result)

    # No edges at all: every node is independently a root, any order is valid
    result = topology_sort_dfs(3, [])
    print("no edges -> expected: [2, 1, 0], actual:", result)

    # Disconnected: chain 0 -> 1 -> 2 plus isolated nodes 3, 4
    result = topology_sort_dfs(5, [[0, 1], [1, 2]])
    print("disconnected -> expected: [4, 3, 0, 1, 2], actual:", result)

    # Cycle should raise ValueError
    try:
        topology_sort_dfs(3, [[0, 1], [1, 2], [2, 0]])
        print("cycle -> expected: ValueError raised, actual: no error raised")
    except ValueError as e:
        print("cycle -> expected: ValueError raised, actual: ValueError raised (", e, ")")
