import random
import heapq
from collections import deque
from typing import Dict, List, Optional, Self

"""
Description: Find median from data stream

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.


Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0


Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.


Follow up:

If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

"""
class MedianFinder:

    def __init__(self) -> None:
        # larger half of the element
        self.min_heap: List[int] = []

        # smaller half of the element
        self.max_heap: List[int] = []

    def addNum(self, num: int) -> None:
        # We try to keep min_heap and max_heap and also size of min_heap is
        # len(min_heap) = len(max_heap) or len(min_heap) = len(max_heap)
        # And the top from min_heap is equal or larger than the top of max_heap
        if len(self.max_heap) > 0 and num < (-1 * self.max_heap[0]):
            # Here python 3.12 and before does not have max heap, so the element must be negated first to use min_heap for max heap
            heapq.heappush(self.max_heap, -1 * num)
            top = -1 * heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, top)
        else:
            heapq.heappush(self.min_heap, num)

        # Balance the min and max heap
        while len(self.min_heap) > len(self.max_heap) + 1:
            element = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -1 * element)
        # print(f"min_heap: {self.min_heap}, max_heap: {self.max_heap}")



    def findMedian(self) -> float:
        if len(self.min_heap) == 0:
            raise ValueError(f"Empty array")

        if len(self.min_heap) == len(self.max_heap):
            top_from_min_heap = self.min_heap[0]
            top_from_max_heap = -1 * self.max_heap[0]
            return (top_from_min_heap + top_from_max_heap) / 2
        else:
            return self.min_heap[0]

if __name__ == "__main__":
    # Run the solution code here
    input = [-1,-2,-3,-4,-5]

    mf = MedianFinder()

    for num in input:
        mf.addNum(num)
        print(f"Median: {mf.findMedian()}")