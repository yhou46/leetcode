import random
import heapq
from collections import deque, defaultdict, OrderedDict
from typing import Dict, List, Optional, Self, Tuple

"""
Description: Count complete tree nodes
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.



Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1


Constraints:

The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Naive solution is to do traversal of the tree and count (BFS for example). It requires O(n) time and does not utilize the fact that the tree is complete binary tree.

    We can easily get the count of nodes for all levels, except the last level since all other levels are filled with nodes and each level has 2^d nodes where d is the depth of the tree (assume d is 0 at root). If depth is 1 at root, then each level has 2^(d-1) nodes.

    To find the max depth, we can just go left child until we hit none and the count the depth

    So the problem becomes how to get the node count at last level.
    We can find the start node of last level but cannot find its siblings. And to find the last level n, we need to find the nodes of n-1, and it becomes a BFS traversal.

    One idea is to use BFS to find the count but how we come to this idea:
        - does the problem has a well defined scope? Yes, the count is from 1 to 2^(d-1)
        - Can we check if a count is valid or not?
            - Yes, if we can find the valid node at the last level, then that count is valid

    So assume we label the last level node from 0 to 2^(d-1) -1, how do we find a node that has a specifc index?
    It is a Binary tree, so we need should go from root, assume the last level has total 8 nodes and we want to find the node labeled 5, how do we get that?
    First, we know 0-3 should be in its left tree, then 4-7 must be in root's right children. We can do this trick again and again until we find it or find the Node does not exist.

    After we have the function to check if a count is valid or not, we can use binary search to find the count of last level
    """
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        depth = 0
        node = root
        while node != None:
            depth += 1 # Here single root is depth 1
            node = node.left

        count = 0
        level_count = 1

        # Count the number of node except last level
        for i in range(depth-1):
            count += level_count
            level_count *= 2

        def exist(root: TreeNode, depth: int, index: int) -> bool:
            total = 2 ** (depth-1) - 1

            start = 0
            end = total
            node = root

            while node != None and start < end:
                mid = (start + end) // 2 # Need to check for when end = start + 1, can the loop exit.
                if index <= mid:
                    end = mid
                    node = node.left
                else:
                    start = mid + 1
                    node = node.right
            return node != None

        start = 0
        end = level_count - 1

        while start < end:
            mid = (start + end + 1) // 2 # Need to check for when end = start + 1, can the loop exit. Here start does not proceed, so we must use ceiling to calculate the mid. That is when end = start + 1, mid = end
            if exist(root, depth, mid):
                start = mid
            else:
                end = mid-1
        return count + start + 1

if __name__ == "__main__":
    # Run the solution code here
    pass