import random
import heapq
from collections import deque, defaultdict, OrderedDict
from typing import Dict, List, Optional, Self, Tuple

"""
Description: Partition list
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.



Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]


Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    """
    The problem is to do partition in linked list. And requirement is to keep original order. To keep the order, one natural idea is to have 2 sub list, one is smaller element, the other is larger or equal element. And the loop through the linked list to add smaller one to smaller list and equal/larger one to larger list. The loop keeps the original order.
    And in the end, we just need to concatenate 2 lists together
    """
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head_small = ListNode(-1)
        head_large = ListNode(-1)

        node = head
        node_small = head_small
        node_large = head_large
        while node != None:
            if node.val < x:
                node_small.next = node
                node_small = node_small.next
            else:
                node_large.next = node
                node_large = node_large.next
            node = node.next

        node_small.next = head_large.next
        node_large.next = None

        return head_small.next

if __name__ == "__main__":
    # Run the solution code here
    pass