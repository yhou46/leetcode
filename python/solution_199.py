import random
from collections import deque, defaultdict, OrderedDict
from typing import Dict, List, Optional, Self, Tuple

"""
Description: Binary tree right side view
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.



Example 1:

Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]

Explanation:



Example 2:

Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]

Explanation:



Example 3:

Input: root = [1,null,3]

Output: [1,3]

Example 4:

Input: root = []

Output: []



Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    The right side view is just the last node of each level. So a BFS is suitable for this case.
    We just need to do BFS and store the last node of a level. To achieve that, we need to store the level in the queue as well.
    A node should be stored if next node in the queue has level larger than its level.
    """
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue: deque[Tuple[int, TreeNode]] = deque()
        result: List[int] = []

        queue.append((0, root))

        while len(queue) > 0:
            (level, node) = queue.popleft()
            if node.left != None:
                queue.append((level+1, node.left))
            if node.right != None:
                queue.append((level+1, node.right))

            # Since we need to compare with top element, we need to cover cases when there is only one node in the queue
            # In this case, the last node should always be in the final result
            if len(queue) == 0 or level < queue[0][0]:
                result.append(node.val)

        return result

if __name__ == "__main__":
    # Run the solution code here
    pass