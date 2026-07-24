import random
from collections import deque, OrderedDict
from typing import List, Optional

"""
Description: Construct binary tree from preorder and inorder traversal
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.



Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]


Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    """
    From preorder travsal, we know the root is the first element.
    Then we can find the index of root from inorder traversal array and that index divide inorder list into 2 parts: left nodes and right nodes. We divide origin problem into 2 sub problems and a recursion like approach should be used to solve this issue. But need a few tricks

    Example: Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    3 is root, we find 3 in inorder which is index 1, we know [9] are left nodes and [15,20,7] are right nodes
    We also know the left root is 9 since 9 is the next element .
    Here we partition inorder into 2 problems: [9] and [15,20,7]
    What about preorder list, we do not know where the left nodes end since they are together: [9,20,15,7]
    The trick here is we already know the total number of nodes in the left tree from the inorder list: len([9]). And left nodes are grouped together and right nodes are group together in preorder list (since it is root -> left -> right order), then we can use the length of total left nodes to divide preorder list into 2 list again:

    inorder: [9,3,15,20,7]
    3 is root from preorder, so it breaks into [9] and [15,20,7]

    preorder: [3,9,20,15,7]
    3 is root, and total left nodes is len([9]), which is 1,
    Then it breaks into [9] (count 1 element after the root) and [20,15,7]

    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        if len(preorder) != len(inorder):
            raise ValueError(f"length of preorder and inorder list should be same, preorder length: {len(preorder)}, inorder length: {len(inorder)}")

        root: TreeNode = TreeNode(preorder[0])

        index = inorder.index(root.val)
        left_children_length = index

        root.left = self.buildTree(
            preorder[1:left_children_length+1],
            inorder[:index],
            )

        root.right = self.buildTree(
            preorder[left_children_length+1:],
            inorder[index+1:]
        )

        return root

if __name__ == "__main__":
    # Run the solution code here
    pass