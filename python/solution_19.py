from typing import Optional

"""
19. Remove Nth Node From End of List
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]


Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz


Follow up: Could you do this in one pass?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # 2 pass solution
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Dummyhead to address scenarios like list size is one
        dummyHead: ListNode = ListNode(0, head)

        # Count number of nodes
        length = 0
        start = head
        while start != None:
            length += 1
            start = start.next

        targetIndex = length - n

        previousNode = dummyHead
        currentNode = dummyHead.next
        currentIndex = 0

        while currentNode != None:
            if currentIndex == targetIndex:
                previousNode.next = currentNode.next
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentIndex += 1
        return dummyHead.next

class Solution2:

    """
    One pass solution:
    2 pointers:
    move 2nd pointer n step, then move 1st and 2nd pointer at the same speed until 2nd pointer's next is None, then 1st pointer is the node before the target node
    """

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(0, head)
        first_pointer = dummy_head
        second_pointer = dummy_head

        count = 0
        while count < n:
            second_pointer = second_pointer.next
            count += 1

        while second_pointer.next != None:
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next

        first_pointer.next = first_pointer.next.next
        return dummy_head.next
