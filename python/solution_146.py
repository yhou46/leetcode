import random
from collections import deque, OrderedDict
from typing import Dict, List, Optional, Self

"""
Description: LRU cache
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.



Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4


Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
"""

class CacheNode:
    next: Self | None = None
    prev: Self | None = None
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value

class LRUCache:
    """
    To re
    """
    def __init__(self, capacity: int):
        self.capacity = capacity

        self.head = CacheNode(0, 0)
        self.tail = CacheNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.map: Dict[int, CacheNode] = {}


    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self._modify_linked_list(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            self._modify_linked_list(node)
            node.value = value
        else:
            if len(self.map) >= self.capacity:
                # Delete node from linked list
                evict_node = self.tail.prev
                if evict_node == self.head or evict_node == None:
                    raise ValueError(f"evicted node is head node or is None")
                prev = evict_node.prev
                if prev == None:
                    raise ValueError(f"evicted node does not have a previous node")
                prev.next = self.tail
                self.tail.prev = prev

                # Delete from map
                self.map.pop(evict_node.key)

            node = CacheNode(key, value)
            self._modify_linked_list(node)
            self.map[key] = node

    def _modify_linked_list(self, node: CacheNode) -> None:
        # Remove node from list if node has valid next and prev
        prev = node.prev
        next = node.next

        if prev != None and next != None:
            prev.next = next
            next.prev = prev

        # Add node to the head
        first_node = self.head.next
        if first_node == None:
            raise ValueError(f"node after head should not be None")
        self.head.next = node
        node.prev = self.head
        node.next = first_node
        first_node.prev = node
        return

if __name__ == "__main__":
    # Run the solution code here
    pass