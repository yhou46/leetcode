import random
from collections import deque, OrderedDict
from typing import Dict, List, Optional, Self, Tuple
from functools import cmp_to_key

"""
Description: Meeting room 2
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.



Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1


Constraints:

1 <= intervals.length <= 104
0 <= starti < endi <= 106
"""

class Solution:
    """
    Thinking: simly checking overlaps won't work since it is hard to track how many max rooms needed when a meeting ends

    Naive thinking: we only need a new room if there is a new meeting start but previous meeting not end yet.

    We can think of the interval as start and end time. Then sort it based on time.
    For start time, we need to add one room
    for end time, we minus one room.

    Notice for consecutive meetings like [0,10] [10, 20] we only need one room. So it means when the time is the same, the end time should go first to calculate the minus 1, then start time to add it back.
    """
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0

        time_list: List[Tuple[int, str]] = []

        for interval in intervals:
            time_list.append((interval[0], "start"))
            time_list.append((interval[1], "end"))

        def comparator(pair1: Tuple[int, str], pair2: Tuple[int, str]) -> int:
            if pair1[0] != pair2[0]:
                return pair1[0] - pair2[0]
            if pair1[1] == pair2[1]:
                return 0
            # same time: "end" should sort before "start"
            return -1 if pair1[1] == "end" else 1

        time_list.sort(key=cmp_to_key(comparator))
        # print(time_list)

        count = 0
        max_count = 0
        for pair in time_list:
            if pair[1] == "start":
                count += 1
            else:
                count -= 1
            max_count = max(max_count, count)

        return max_count

if __name__ == "__main__":
    # Run the solution code here
    s = Solution()
    input = [[0,5],[5,10],[10,20]]

    print(f"{s.minMeetingRooms(input)}")