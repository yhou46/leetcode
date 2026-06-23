import random
from collections import deque, OrderedDict
from typing import List, Optional, Dict

"""
Description: TBD
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}


Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.



Example 1:


Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
Example 2:


Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.


Constraints:

The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    """
    It can be done through BFS or DFS. Below is a BFS solution.
    """
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node == None:
            return None

        cloned_map: Dict[Node, Node] = {} # Map from original node to cloned nodes
        cloned_map[node] = Node(node.val)

        bfs_queue: deque[Node] = deque()
        # All nodes in the queue are already cloned, but has no neighbors set yet
        bfs_queue.append(node)

        while len(bfs_queue) > 0:
            current_node = bfs_queue.popleft()

            cloned_node = cloned_map[current_node]

            for neighbor in current_node.neighbors:

                # Key part: we do the neighbor clone here instead of doing it when pop from the queue
                # It means all nodes in the queue have already been cloned but their neighbors are not cloned yet
                if neighbor not in cloned_map:
                    cloned_neighbor = Node(neighbor.val)
                    cloned_map[neighbor] = cloned_neighbor
                    bfs_queue.append(neighbor)
                cloned_node.neighbors.append(cloned_map[neighbor])

        return cloned_map[node]

if __name__ == "__main__":
    # Run the solution code here
    node1 = Node(1)
    node_dict = {}
    node_dict[node1] = node1

    node2 = node1
    print(f"{node_dict[node2].val}")