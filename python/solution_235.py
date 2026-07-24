import random
from collections import deque, OrderedDict
from typing import Dict, List, Optional, Self

"""
Description: Lowest common ancestor of a binary search tree
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”



Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2


Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    A BST means all children in left subtree are smaller than root and all children in right subtree are larger than root.
    If a root's value is between p and q, then root must be the lowest common ancestor
        - why?
            Because if root is not, then p and q must be all in left or right subtree, means values of p and q must be all smaller or all greater than root, which violate the BST definition
    If root value is smaller than the smaller value of p and q, then the common ancestor should be in the right subtree
    If root value is larger than the larger value of p and q, then the common ancestor should be in the left subtree
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        small_node = p if p.val < q.val else q
        large_node = p if p.val > q.val else q

        if small_node == large_node:
            raise ValueError(f"Invalid input: p: {p.val}, q: {q.val}")

        # if root == p or root == q:
        #     return root

        if root.val < small_node.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > large_node.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            # It already handles case when root == p or root == q
            return root

if __name__ == "__main__":
    # Run the solution code here
    pass