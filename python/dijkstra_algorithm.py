import random
import heapq
from collections import deque, defaultdict, OrderedDict
from typing import Dict, List, Optional, Self, Tuple

"""
Dijkstra algorithm is can be used to find shortest path from all nodes to a start node but it has limitations:
    - All path weight should not be negative

Dijkstra finds shortest paths from a single start node to every other node, using a greedy strategy with a min-priority queue:

Maintain a distances[] array: best known distance to each node so far (∞, or -1 here, until discovered).
Start with distances[start] = 0, push (0, start) into a min-heap keyed by distance.
Repeatedly pop the entry with the smallest distance. That's node at line 27.
Relax every outgoing edge from node: for each neighbor i, if going through node gives a shorter path than what's currently recorded (distance + weight < distances[i]), update distances[i] and push (new_dist, i) (lines 32–39).
Repeat until the heap is empty.
The greedy step is: always expand the closest unfinished node next.

Why it's correct:

The whole proof rests on one claim: the first time a node is popped from the heap, the distance it's popped with is already its true shortest distance.

Proof sketch (by induction on pop order): Suppose this holds for every node popped before some node v is popped with distance d. Suppose for contradiction the true shortest distance to v is actually d' < d, via some path start → ... → u → v. Since all edge weights are non-negative, every prefix of that path is also ≤ d' in length, so in particular u's true shortest distance is ≤ d' < d. By the induction hypothesis, u was already popped (and finalized) at its true distance before v was — because the heap always pops smaller distances first, and u's finalized distance is smaller than d. But if u was already finalized, its edge to v was already relaxed (step 4), which would have set distances[v] ≤ d' < d and pushed that better value onto the heap. The heap pops smallest-first, so that better (d', v) entry would have come out before (d, v). Contradiction — so no shorter path can exist; d was already optimal.

This is exactly why non-negative weights are essential: the argument depends on "every prefix of a shortest path is at most as long as the full path," which fails the moment a negative edge can make a longer-looking prefix cheaper later. That's also why the weight != -1 sentinel for "no edge" in this code (from earlier in our conversation) is a reasonable convention only because Dijkstra already assumes weights ≥ 0 — a legitimate negative weight was never going to be valid input here anyway.

Tying back to this file's implementation: this is exactly what the earlier distance > distances[node] check (line 29) leverages — since the first pop of a node is provably optimal, any later pop of that same node (a stale heap duplicate) must be safely skippable, because it can't possibly still improve on the already-optimal value.
"""
class DijkstraAlgorithm:
    """
    Given a 2 D matrix n*n, graph[i][j] is the weight of edge from vertex i to j, total number of nodes is n
    Return the shortest path from all nodes to the start node, negative 1 means not connected
    Return:
    First list[i] is the shortest path weight from start to i
    Second List[i] is the node path from start to i, [1,3,4] means start is 1 and shortest path to 4 is 1 -> 3 -> 4
    """
    @staticmethod
    def shortest_path(graph: List[List[int]], start: int) -> Tuple[List[int], List[List[int]]]:

        n = len(graph)

        # (distance, node)
        pq: List[Tuple[int, int]] = [(0, start)]
        distances: List[int] = [-1 for _ in range(n)]
        distances[start] = 0

        previous_nodes: List[int] = [0 for _ in range(n)]

        while len(pq) > 0:
            distance, node = heapq.heappop(pq)

            if distances[node] != -1 and distance > distances[node]:
                continue

            for i in range(n):
                weight = graph[node][i]
                if weight != -1:
                    new_dist = distance + weight
                    if distances[i] < 0 or new_dist < distances[i]:
                        distances[i] = new_dist
                        previous_nodes[i] = node
                        heapq.heappush(pq, (new_dist, i))

        # construct path
        paths: List[List[int]] = [[] for _ in range(n)]
        paths[start] = [start]
        for i in range(n):
            if i != start:
                # Only check reachable nodes
                if distances[i] != -1:
                    current = i
                    path: List[int] = []
                    while current != start:
                        path.append(current)
                        current = previous_nodes[current]
                    path.append(start)
                    path.reverse()
                    paths[i] = path



        return (distances, paths)

if __name__ == "__main__":
    graph: List[List[int]] = [
        [0, 2, -1],
        [-1, 0, 3],
        [-1, -1, 0]
    ]

    graph = [
        [0, 1],
        [1, 0],
    ]

    graph = [
        [0, -1, -1],
        [-1, 0, -1],
        [-1, -1, 0],
    ]

    graph = [
        [0, 5, 0],
        [-1, 0, -1],
        [-1, 0, 0],
    ]

    s = DijkstraAlgorithm()

    distances, paths = s.shortest_path(graph, 0)
    print(f"distances: {distances}")
    print(f"path: {paths}")