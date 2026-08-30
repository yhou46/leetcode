import random
import heapq
from collections import deque, defaultdict, OrderedDict
from typing import Dict, List, Optional, Self, Tuple

"""
Description: Rotation list
Given the head of a linked list, rotate the list to the right by k places.



Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]


Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head

        length = 0
        node = head
        last_node = head
        # Find total length and last node
        while node != None:
            if node.next == None:
                last_node = node
            node = node.next
            length += 1

        # Compute new K
        k = k % length
        if k == 0:
            return head

        remain = length - k
        prev = None
        node = head

        # Find the start of rotation
        for _ in range(remain):
            prev = node
            node = node.next

        # Concatenate
        if last_node != head:
            last_node.next = head

        # Break the ring
        if prev != None:
            prev.next = None
        return node

if __name__ == "__main__":
    # Run the solution code here
    pass