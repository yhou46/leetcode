import random
from collections import deque, OrderedDict
from typing import List

"""
56. Merge intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
Example 3:

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.


Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ret = []
        intervals.sort()
        curr_interval = intervals[0]
        for interval in intervals[1:]:
            if interval[0] <= curr_interval[1]:
                curr_interval[1] = max(interval[1], curr_interval[1])
            else:
                ret.append(curr_interval)
                curr_interval = interval
        ret.append(curr_interval)
        return ret

if __name__ == "__main__":
    # Run the solution code here
    pass