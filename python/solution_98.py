import random
from collections import deque, OrderedDict
from typing import List, Optional

"""
Description: Valid binary search tree
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.


Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    """
    inorder travsal using recursion
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if root == None:
            return True

        result: List[int] = []

        self.dfs(root, result)

        for i in range(1, len(result)):
            if result[i-1] >= result[i]:
                return False
        return True

    def dfs(self, node: TreeNode, result: List[int]):
        if node.left != None:
            self.dfs(node.left, result)

        result.append(node.val)

        if node.right != None:
            self.dfs(node.right, result)


class Solution2:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if root == None:
            return True

        return self.dfs(root, [])

    """
    Do DFS and check in one run
    """
    def dfs(self, node: TreeNode, previous_node: List[TreeNode]) -> bool:
        if node.left != None:
            isBST = self.dfs(node.left, previous_node)
            if not isBST:
                return False
        # print(f"node val: {node.val}, previous node: {None if previous_node == None else previous_node.val}")
        if len(previous_node) > 0 and previous_node[0].val >= node.val:
            print(f"find node false")
            return False

        """
        If we define previous_node as Optional[TreeNode]
        and we do
            previous_node = node here. It won't work.
            Why?
            Because the value changed here is a reference and this change is not reflected by its caller.

            Example:
            func1(a, b):
                a = 12
                return

            def func2(a, b):
                anotherFunc(a, b)
                # Here a = 12 is only visible in func1 and a is not changed inside func2

        """
        if len(previous_node) == 0:
            previous_node.append(node)
        else:
            previous_node.pop()
            previous_node.append(node)

        if node.right != None:
            isBST = self.dfs(node.right, previous_node)
            if not isBST:
                return False
        return True

class Solution3:
    """
    Do inorder travsal using stack instead of recursion
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack: deque[TreeNode] = deque()

        previous_node: TreeNode | None = None
        while root != None or len(stack) > 0:

            while root != None:
                stack.append(root)
                root = root.left

            root = stack.pop()
            # Visit
            if previous_node != None and previous_node.val >= root.val:
                    return False
            previous_node = root

            root = root.right

        return True


if __name__ == "__main__":
    # Run the solution code here
    pass