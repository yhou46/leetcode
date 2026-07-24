import random
from collections import deque, OrderedDict
from typing import Dict, List, Optional, Self

"""
Description: Meeting rooms

You are given an array of meeting times intervals where intervals[i] = [starti, endi].

A person can attend all meetings if no two meeting intervals overlap. Meetings ending at time t and starting at time t do not overlap.

​​​​​​​Return true if a person can attend all meetings. Otherwise, return false.



Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true


Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti < endi <= 106
"""
class Solution:
    """
    Similar to merge intervals. Just sort based on start time.

    """
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) == 0:
            return True

        # Python sort by list is a element by element comparison
        intervals.sort()
        current = intervals[0]

        for interval in intervals[1:]:
            if current[1] > interval[0]:
                return False
            current = interval
        return True

if __name__ == "__main__":
    # Run the solution code here
    pass