import random
from collections import deque, OrderedDict
from typing import List, Optional, Tuple

"""
Description: Binary tree level order travsal

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    """
    Idea:
    To output each level in separate list, we just need to remember each node's level in the BFS. Push the same level to final list if level changes.
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue: deque[Tuple[TreeNode, int]] = deque()

        result: List[List[int]] = []
        if not root:
            return result

        queue.append((root, 0))
        current_level = 0
        current_result: List[int] = []

        while len(queue) > 0:
            entry = queue.popleft()
            node = entry[0]
            level = entry[1]
            if level == current_level:
                current_result.append(entry[0].val)
            else:
                result.append(current_result)

                # Current node to the list
                current_result = [node.val]
                current_level += 1

            if node.left != None:
                queue.append((node.left, level+1))
            if node.right != None:
                queue.append((node.right, level+1))

        # Push last list to result
        if len(current_result) > 0:
            result.append(current_result)

        return result

if __name__ == "__main__":
    # Run the solution code here
    pass