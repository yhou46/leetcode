import random
from collections import deque, OrderedDict
from typing import Dict, List, Optional, Self

"""
Description: Kth smallest element in BST
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.



Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3


Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104


Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root == None:
            raise ValueError(f"Invalid Tree")
        result: List[int] = []
        self.in_order_travsal(root, result, k)
        # print(result)

        # Note: you cannot return result[-1], aka, the last element in the result array even if
        # in the recursion you return early by checking k
        return result[k-1]


    def in_order_travsal(self, node: Optional[TreeNode], result: List[int], k: int) -> None:
        if node == None:
            return

        self.in_order_travsal(node.left, result, k)
        result.append(node.val)

        """
        Even if it returns early, it cannot guarantee result only has k elements, because after return, the caller may do the append first, then do the check.
        To make result only returns k element, you need to add checks in many places so just return the indexed element in result for the Kth element
        """
        if len(result) >= k:
            return
        self.in_order_travsal(node.right, result, k)

if __name__ == "__main__":
    # Run the solution code here
    pass