import random
from collections import deque, OrderedDict
from typing import Dict, List, Optional, Self

"""
Description: Non overlapping intervals
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.



Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


Constraints:

1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104
"""
class Solution:
    """
    Thinking process:
    We have done problem to merge intervals before.
    How is it different from merge intervals?
        - It is different when we find an overlapping. When a overlapping is found, we need to remove one interval, either the current one or next one.
        - Which one should we remove:
            Apparently the one with larger ending point since it is likely for it to create future overlapping

    Some cases:
    [.  1.  ]
         [.  2  ]
    In this case, we should remove 2nd one since it is more likely to cause overlapping with next one.
    So it is clear, we still need to sort based on start time, then compare current interval with next one, if no overlapping, just step to next one. If overlapping, then increase counter and use the one with smaller ending time as next one.
    """
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort()
        start = intervals[0]
        count = 0

        for interval in intervals[1:]:
            # Found overlap
            if start[1] > interval[0]:
                count += 1
                start = start if start[1] < interval[1] else interval
            else:
                start = interval
        return count

if __name__ == "__main__":
    # Run the solution code here
    pass