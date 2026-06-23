import random
from collections import deque, OrderedDict
from typing import List, Optional

"""
Description: Binary tree max sum path
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.



Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.


Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # Core part: the result is outside of the function
    max_sum = float('-inf')

    """
    Any path in the binary tree is a child binary tree and it has a root node.
    This "root" node is not necessarily the real root node.
    """
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        """
        The max sum from <node> down towards the leaf nodes (no need to include leaf nodes). The node has to be included in the path
        If node's val is negative, still include it.

        We can do a travsal in the tree, assume each node is the "root" of the child tree and compute the path sum.
        If the current node is the "root", then the max sum path is the sum of:
            - the max sum of its left child down straight
            - the max sum of its right child down straight
            - the node val itself

        And we can find the max sum path starting from node and end in any nodes below it using the recursion
        """
        def maxSumDownwardsFromNode(node: Optional[TreeNode]) -> int:
            if node == None:
                return 0

            # We need to compare it to zero because the left and right sum path could be negative
            # If so, we just do not use it. That's why the value is 0 (means we do not use the path)
            left_max = max(maxSumDownwardsFromNode(node.left), 0)
            right_max = max(maxSumDownwardsFromNode(node.right), 0)

            # When update the final result, we assume the path has the current node as highest level (root for the tree of the path)
            self.max_sum = max(self.max_sum, node.val+left_max+right_max)

            return node.val + max(left_max, right_max)

        maxSumDownwardsFromNode(root)

        # To silence the mypy parse error of max_sum being float type (the initial assignment)
        return int(self.max_sum)

if __name__ == "__main__":
    # Run the solution code here
    pass