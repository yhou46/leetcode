from typing import List, Optional, Tuple
from queue import PriorityQueue

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = PriorityQueue[Tuple[int, int, ListNode]]()

        # Why enumerate?
        # Because the type in PQ is Tuple and python compares Tuples element by element. ListNode does not have comparator defined (__lt__) so it hits error when 2 nodes have same values. add another entry i to make sure 2 nodes from different list has different index to compare
        for i, node in enumerate(lists):
            if node is not None:
                min_heap.put((node.val, i, node))

        dummy = ListNode(0, None)
        current = dummy

        while not min_heap.empty():
            (_, i, node) = min_heap.get()
            current.next = node
            current = current.next

            node = node.next
            if node is not None:
                min_heap.put((node.val, i, node))


        return dummy.next
