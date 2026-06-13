import random
from collections import deque, OrderedDict
from typing import List, Tuple

"""
Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id


Example 1:

Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation:
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5


Constraints:

1 <= length <= 5 * 104
0 <= index < length
0 <= val <= 109
0 <= snap_id < (the total number of times we call snap())
At most 5 * 104 calls will be made to set, snap, and get.
"""
class SnapshotArray:

    def __init__(self, length: int):
        self._items = [0 for i in range(length)]

        # each postion is the history of the index change history
        """
        We cannot store each snapshot in the array and it causes memory limit exceed issue.
        The idea is to store the update history of each index.
        snapshots stores the update history of each index with a list, (0,1) means in snapshot 0, the value is updated to 1
        """
        self._snapshots: List[List[List[int]]] = [[[0,0]] for i in range(length)]
        self._snap_id = 0


    def set(self, index: int, val: int) -> None:
        #print(f"Set: index={index}, val={val}")
        if self._items[index] != val:
            if self._snapshots[index][-1][0] != self._snap_id:
                self._snapshots[index].append([self._snap_id, val])
            else:
                self._snapshots[index][-1][1] = val
            self._items[index] = val

    def snap(self) -> int:
        #print(f"Snap: currentId={self._snap_id}")

        self._snap_id += 1
        return self._snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        #print(f"Get: index={index}, snap_id={snap_id}")
        index_history: List[List[int]] = self._snapshots[index]

        # Binary search to find the target
        # [0,2,3]
        left = 0
        right = len(index_history) - 1
        #print(f"Before BS: left={left}, right={right}")
        while left < right:
            mid = (left + right + 1) // 2
            #print(f"During BS: left={left}, right={right}, mid={mid}, history: {index_history[mid][0]}")
            if index_history[mid][0] <= snap_id:
                left = mid
            else:
                right = mid -1
        return self._snapshots[index][left][1]






# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)



if __name__ == "__main__":
    # Run the solution code here
    pass