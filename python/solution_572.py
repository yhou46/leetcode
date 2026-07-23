import random
from collections import deque, OrderedDict
from typing import Dict, List, Optional, Self

"""
Description: TBD
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    Apparently we can traverse the tree to compare
    But directly recursion on isSubtree is not enough.

    Why?
    Because it changes the original input.
    Look at this example:
        3           3
     4     5      1    2
    1    2
    This case means if we recursion on the isSubtree, root and subroot will be changed to 4 and 1, not equal, then we try to compare from beginning. but at this step, we lost root of 4 and 1, and we falls into the category of thinking 4 is the real root, and start to compare 4's left with 1, which is equal and eventually produce the wrong result


       1          1
     1
    This case means if we find roots are same but child are different, we should proceed to its left and right subtree for comparison.

    How to think of it?
    First we try to have a function directly compare if 2 trees are same. Then we recursively do on root and its children to find if they are same as the subRoot tree
    """
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.traverse(root, subRoot)

    def traverse(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root != None:
            return self.is_same_tree(root, subRoot) or self.traverse(root.left, subRoot) or self.traverse(root.right, subRoot)
        else:
            return root == subRoot

    # It just compare if 2 trees are exactly same
    def is_same_tree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            if subRoot == None:
                return True
            else:
                return False
        elif subRoot == None:
            return False

        if root.val == subRoot.val:
            return self.is_same_tree(root.left, subRoot.left) and self.is_same_tree(root.right, subRoot.right)
        else:
            return False

if __name__ == "__main__":
    # Run the solution code here
    pass