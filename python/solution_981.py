import random
import heapq
from collections import deque, defaultdict, OrderedDict
from typing import Dict, List, Optional, Self, Tuple

"""
Description: Time based key value store
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".


Example 1:

Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"


Constraints:

1 <= key.length, value.length <= 100
key and value consist of lowercase English letters and digits.
1 <= timestamp <= 107
All the timestamps timestamp of set are strictly increasing.
At most 2 * 105 calls will be made to set and get.
"""
class TimeMap:
    """
    One important point is the set is called with timestamp strictly increasing
    To find a target timestamp, we can use binary search.
    Python also has built-in library about binary search: bisect which is to return the index of an element that should be inserted in the array and still make the array sorted
    """
    def __init__(self) -> None:
        self.map: Dict[str, List[Tuple[int, str]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        # print(f"get: key: {key}, time: {timestamp}")
        if key not in self.map:
            return ""
        value_list = self.map[key]
        # print(f"values: {value_list}")

        if value_list[0][0] > timestamp:
            return ""

        # Binary search
        left = 0
        right = len(value_list)-1
        while left < right:
            mid = (left + right + 1) // 2
            if value_list[mid][0] <= timestamp:
                left = mid
            else:
                right = mid-1
        # print(f"left: {left}, right: {right}")

        return value_list[left][1]

if __name__ == "__main__":
    # Run the solution code here
    pass