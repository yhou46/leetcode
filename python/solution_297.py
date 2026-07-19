import random
from collections import deque, OrderedDict
from typing import Dict, List, Optional, Self

"""
Description: Serialize and deserialize binary tree
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.



Example 1:


Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    """
    We can use BFS to do the serialize and deserialize, but we need to have None if child is the leaf.
    Example:
        1
      2   3
        4   5
    Here the BFS result is 1,2,3,4,5 and children 2 does not have any children. We do not know if 4 and 5 should be under node 2 or node 3, so we need to have None as place holder and serialze as:
    1,2,3,None,None,4,5

    The logic is more like we record all children of nodes in BFS including None. But we do not proceed if it is already None

    Another example:
        1
      2   3
        4
       5
    2 has no childer, 3 only has 4 as left child and 4 has 5 has left child. In this case, the serialized result is
    1, 2, 3, None(2's left), None(2's right), 4, None(3's right), 5, None(4's right) ,None(5's left) , None(5's right),

    To deserialize, we still need a queue. One easy way is to split the string into elements first.
    Then use the queue to do the BFS assignment
    """
    def serialize(self, root: TreeNode | None) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        queue: deque[TreeNode | None] = deque()
        queue.append(root)

        result = ""
        while len(queue) > 0:
            node = queue.popleft()
            print(f"serialize: node: {node.val if node != None else None}")

            if node != None:
                result += f"{node.val},"
                queue.append(node.left)
                queue.append(node.right)
            else:
                result += f"None,"
            print(f"serialize: queue size: {len(queue)}")

        return result

    def deserialize(self, data: str) -> TreeNode | None:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        # There is a "," at the end so the split result will have en
        elements: List[str] = data.split(",")

        print(f"elements: {elements}")

        if len(elements) == 0 or elements[0] == "None":
            return None

        root = TreeNode(int(elements[0]))
        queue: deque[TreeNode] = deque()

        queue.append(root)
        start = 1

        while len(queue) > 0 and start < len(elements):
            node = queue.popleft()
            left = elements[start]
            if left != "None":
                node.left = TreeNode(int(left))
                queue.append(node.left)
            start += 1

            if start < len(elements):
                right = elements[start]
                if right != "None":
                    node.right = TreeNode(int(right))
                    queue.append(node.right)
            else:
                raise ValueError(f"right: {start} is out of bound for elements: {elements}")
            start += 1
            print(f"start at the end: {start}, queue size: {len(queue)}")

        return root



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

if __name__ == "__main__":
    # Run the solution code here
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.right.left = TreeNode(4)
    root.right.left.left = TreeNode(5)

    # test
    codec = Codec()
    serialize = codec.serialize(root)
    print(f"serialize: {serialize}")

    node = codec.deserialize(serialize)
    print(f"deserialized -> serialized: {codec.serialize(node)}")
    print(f"deserialize compare: {serialize == codec.serialize(node)}")
