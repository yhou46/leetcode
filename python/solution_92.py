import random
import heapq
from collections import deque, defaultdict, OrderedDict
from typing import Dict, List, Optional, Self, Tuple

"""
Description: Reverse LinkedList 2
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]


Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n


Follow up: Could you do it in one pass?
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    """
    Similar to revere linked list. We need to first find the node before left and node after right. Then reverse nodes in between, then attach the remaining part
    """
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None

        # dummy head is important since the head can be reversed and no longer being head. dummy head makes sure we can retrieve the new head correctly
        dummy_head = ListNode(-1)
        dummy_head.next = head
        node_before_left = dummy_head # left can be 1, which means the head node so has to initialize to be dummy head
        node_left: ListNode | None = None
        node_after_right: ListNode | None = None # right can also be last node so set it to None

        node = head
        count = 0
        while node != None:
            if count == left - 2:
               node_before_left = node

            if count == left -1:
                node_left = node

            if count == right:
                node_after_right = node
                break
            count += 1
            node = node.next

        # If left an right are correct, node_left should not be None, just to silence the mypy error
        if not node_left:
            raise ValueError(f"Invalid left: {left}")

        # Reverse
        prev = None
        current = node_left
        while current != node_after_right:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        node_before_left.next = prev
        node_left.next = node_after_right

        return dummy_head.next

if __name__ == "__main__":
    # Run the solution code here
    pass