import random
from collections import deque, defaultdict, OrderedDict
from typing import Dict, List, Optional, Self, Tuple

"""
Description: Binary tree zig zag level order traversal
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 2000].
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
    We can still use BFS and use level to remember the node's level. When pushing a node's children, its children should have level+1

    To do zig zag, we use level to determine whether it should be left to right or right to left. We normally remember the nodes in the level in normal BFS and do reverse if we find it should be right to left.
    """
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        result: List[List[int]] = []
        queue: deque[Tuple[TreeNode, int]] = deque()

        queue.append((root, 0))
        previous_level = 0
        temp: List[int] = [] # the nodes in a level

        while len(queue) > 0:
            node, level = queue.popleft()

            # Important: we only do append level nodes to result when we reached next level (the first node in the next level). Otherwise we do not know whether a node is the last node in the level
            # Thus, when we are done the BFS, the nodes in last level is not added to the final result yet, so we need to do one more append
            if level > previous_level:
                # left to right
                if previous_level % 2 == 0:
                    result.append(temp)
                else:
                    temp.reverse()
                    result.append(temp)

                # Important: need to append first node to level information
                temp = [node.val]
            else:
                temp.append(node.val)
            previous_level = level

            if node.left != None:
                queue.append((node.left, level+1))
            if node.right != None:
                queue.append((node.right, level+1))

        # Append nodes in the last level
        if previous_level % 2 == 0:
            result.append(temp)
        else:
            temp.reverse()
            result.append(temp)
        return result

    """
    Slightly different idea but still use BFS:
    Difference:
        - Use a delimiter: None to indicate a level has ended.
            - Why we can keep adding new delimiter when a level ends? Because when we have processed last node of a level, we pushed all nodes of next level. Assume there is a delimiter right after the last node in that level, when we process that delimiter, the queue already has all nodes of next level and we can push the next delimiter. So we just need to make sure first node has its delimiter.
        - Instead of reverse the list, we use a deque to remember the level_nodes since deque can append new node to the left. When we need to append the final result, we do not need to reverse it. We still need a flag about direction since we need to decide whether to append or appendleft.
    """
    def zigzagLevelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        result: List[List[int]] = []

        # Have to queue the root and its delimiter
        queue: deque[TreeNode | None] = deque([root, None])
        level_nodes: deque[int] = deque()
        left_to_right = True

        while len(queue) > 0:
            node = queue.popleft()

            # Node is valid
            if node != None:
                if left_to_right:
                    level_nodes.append(node.val)
                else:
                    level_nodes.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # None, delimiter
            else:
                result.append(list(level_nodes))

                # When we at delimiter, it means we arrived at the last node in the level and by that time, all nodes for the next level are already in the queue, but just not visited yet. So we need to append delimiter here
                # Important, we should only add delimiter when queue is not empty, otherwise, we will keep adding none when completing the last node in the queue
                if len(queue) > 0:
                    queue.append(None)

                # Need to reset level nodes
                level_nodes = deque()

                # Flip direction
                left_to_right = not left_to_right

        return result


if __name__ == "__main__":
    # Run the solution code here
    pass