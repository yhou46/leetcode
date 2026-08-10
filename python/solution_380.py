import random
from collections import deque, defaultdict, OrderedDict
from typing import Dict, List, Optional, Self, Tuple

"""
Description: Insert, Delete, GetRandom in O(1)
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.



Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.


Constraints:

-231 <= val <= 231 - 1
At most 2 * 105 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.
"""
class RandomizedSet:

    """
    To make insert and delete in O(1), a HashSet is the best option
    But we cannot get random element from a hash set easily.
    To get a random element from a hash set, we need to convert it to an array and generate a random int for the index. And it takes O(n) time for get random.

    If we store elements in an array, then get random takes O(1) but insert and remove takes O(n)

    To achieve we need both at the same time and they need to be consistent:
    HashSet or map to make insert/remove O(1)
    And a list to make get random O(1)
    Insert is easy since we just need to add element to both hash set and array but deletion is a issue since it takes O(n) to delete an item from array.

    Idea:
    What if we swap the element with the last element in deletion scenario and then pop it from the array? Remove a element from end takes O(1) time. To update the hashmap, we can keep the mapping from value -> index in array.
    Then in deletion, we first get the index of the target element, then swap it with last element in the array. Then update the swapped element's index in hash map. And at last, delete the target from hash map and array.
    """
    def __init__(self) -> None:
        # Map from element to index
        self.element_map: Dict[int, int] = {}

        # Elements
        self.elements: List[int] = []


    def insert(self, val: int) -> bool:
        if val in self.element_map:
            return False

        self.elements.append(val)
        self.element_map[val] = len(self.elements)-1
        return True


    def remove(self, val: int) -> bool:
        if val not in self.element_map:
            return False

        index = self.element_map[val]

        # Swap and update last element's index
        last_element = self.elements[-1]
        self.elements[index], self.elements[-1] = self.elements[-1], self.elements[index]
        self.element_map[last_element] = index

        # Delete the entry
        del self.element_map[val]
        self.elements.pop()
        return True

    def getRandom(self) -> int:
        index = random.randint(0, len(self.elements)-1)
        return self.elements[index]

if __name__ == "__main__":
    # Run the solution code here
    pass