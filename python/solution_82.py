import random
import heapq
from collections import deque, defaultdict, OrderedDict
from typing import Dict, List, Optional, Self, Tuple

"""
Description: Remove duplicates from sorted linked list 2
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.



Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]


Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        dummy_head = ListNode(-1)
        dummy_head.next = head
        node_first: ListNode = dummy_head # point to the node of unique element
        node_second = node_first.next
        while node_first != None:
            is_unique = True
            if node_second != None and node_second.next != None and node_second.val == node_second.next.val:
                is_unique = False

            if not is_unique:
                while node_second != None and node_second.next != None and node_second.val == node_second.next.val:
                    node_second = node_second.next
                node_second = node_second.next
            else:
                node_first.next = node_second
                node_first = node_first.next

                if node_first == None:
                    break
                node_second = node_first.next


        return dummy_head.next

if __name__ == "__main__":
    # Run the solution code here
    pass