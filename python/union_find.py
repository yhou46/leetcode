from typing import List

"""
Union-Find (also called Disjoint Set Union, or DSU) is a data structure that keeps track of a collection of elements partitioned into disjoint groups. It supports two operations, both extremely fast:

find(x) — Which group does x belong to?
union(x, y) — Merge the group containing x with the group containing y.

Each group is represented as a tree, where every node points to a parent, and the root of the tree is the group's "representative." Two elements are in the same group if and only if they trace up to the same root.
Group A:  1 → 2 → 3 (root)
Group B:  4 → 5 (root)

find(1) walks 1 → 2 → 3, returns 3.
find(4) walks 4 → 5, returns 5.
union(1, 4) finds both roots and hooks one under the other: now everyone points (eventually) to a single root.
"""
class UnionFind:
    # n means n nodes, each node is represented by a number: 0,1,2... n-1
    def __init__(self, n: int) -> None:

        # parent means what is the parent of a node
        # parent[i] means the parent of node: i, which is another node
        # By default, each node is the parent of itself initially
        # The root node is represented by the fact that the parent of it is itself: parent[i] = i. At the beginning, all nodes are root
        self.parent: List[int] = [ i for i in range(n)]

        # The upper bound of the depth of a tree node.
        # rank[i] means the upper bound of the depth of the tree that roots at i. If i is not root, then rank[i] is meaning less.
        # the real depth of the tree is smaller than rank[i]
        self.rank: List[int] = [0 for i in range(n)]

    # Returns false if x and y already connected, true if x and y were not connected but connected now
    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        # Assign the root of lower rank to the root of higher rank
        if self.rank[root_x] > self.rank[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_x] = root_y
        if self.rank[root_x] == self.rank[root_y]:

            # Only increase rank when 2 trees are same rank
            self.rank[root_y] += 1
        return True

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


if __name__ == "__main__":
    uf = UnionFind(5)

    # Initially every node is its own root
    print("find(0) -> expected: 0, actual:", uf.find(0))
    print("find(4) -> expected: 4, actual:", uf.find(4))

    # Union two disjoint nodes
    print("union(0,1) -> expected: True, actual:", uf.union(0, 1))
    print("find(0) == find(1) -> expected: True, actual:", uf.find(0) == uf.find(1))

    # Unioning already-connected nodes returns False
    print("union(0,1) again -> expected: False, actual:", uf.union(0, 1))

    # Chain more unions and check transitive connectivity
    print("union(1,2) -> expected: True, actual:", uf.union(1, 2))
    print("find(0) == find(2) -> expected: True, actual:", uf.find(0) == uf.find(2))

    # Nodes 3 and 4 are still separate from the 0-1-2 group
    print("find(3) == find(0) -> expected: False, actual:", uf.find(3) == uf.find(0))
    print("union(3,4) -> expected: True, actual:", uf.union(3, 4))
    print("find(3) == find(4) -> expected: True, actual:", uf.find(3) == uf.find(4))

    # Merge the two groups
    print("union(2,4) -> expected: True, actual:", uf.union(2, 4))
    print("find(0) == find(3) -> expected: True, actual:", uf.find(0) == uf.find(3))


