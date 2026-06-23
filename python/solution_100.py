import random
from collections import deque, OrderedDict
from typing import List, Optional

"""
Description: Same tree
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q != None or p != None and q == None:
            return False

        if p != None and q != None:
            if p.val != q.val:
                return False

            is_equal = self.isSameTree(p.left, q.left)
            if not is_equal:
                return False
            is_equal = self.isSameTree(p.right, q.right)
            if not is_equal:
                return False

        return True

if __name__ == "__main__":
    # Run the solution code here
    pass