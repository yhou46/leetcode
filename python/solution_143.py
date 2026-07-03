import random
from collections import deque, OrderedDict
from typing import List, Optional

"""
Description: Reorder List

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.



Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]


Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    The result can be thought like cut the list in the middle, first half start from beginning, 2nd half start from end, then merge these 2 lists.

    So the steps are:
    1. Find middle Node of the list.
    2. Revert links in the 2nd half of the list
    3. Merge 1st and 2nd half of the list
    """
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if head == None:
            return None

        # Find the middle
        slow_ptr = head

        # Why fast_ptr = head.next ? Because we want the slow_ptr point to the middle
        # For odd number of nodes: 1 -> 2 -> 3, slow_ptr should point to 2
        # For even number of nodes: 1-> 2 -> 3 -> 4, slow_ptr should point to 2
        fast_ptr = head.next

        while fast_ptr != None and fast_ptr.next != None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        # Revert 2nd list
        # The middle node should be the end of 2nd list
        second_list_end = slow_ptr.next
        slow_ptr.next = None

        current = second_list_end
        previous = None

        while current != None:
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        # Now merge 2 lists
        l1 = head
        l2 = previous

        # the size of l1 should be len(l2) (even nodes) or len(l2) + 1 (odd nodes)
        # l2 will reach to the end (None) first, l1 will be the last Node or None
        while l1 != None and l2 != None:
            l1_next = l1.next
            l1.next = l2
            l2_next = l2.next
            l2.next = l1_next

            l1 = l1_next
            l2 = l2_next
        return None


if __name__ == "__main__":
    # Run the solution code here
    pass