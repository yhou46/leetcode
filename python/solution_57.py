import random
from collections import deque, OrderedDict
from typing import List

# Description: TBD
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        insert_index = -1
        for i, interval in enumerate(intervals):
            if interval[0] >= newInterval[0]:
                insert_index = i
                break
        # new interval should be inserted to last one
        if insert_index == -1:
            intervals.append(newInterval)
        else:
            intervals.insert(insert_index, newInterval)

        return self.merge_intervals(intervals)

    def merge_intervals(self, intervals: List[List[int]]):

        result_list = []
        current_interval = intervals[0]

        for i in range(1, len(intervals)):
            if current_interval[1] >= intervals[i][0]:
                current_interval[1] = max(current_interval[1], intervals[i][1])
            else:
                result_list.append(current_interval)
                current_interval = intervals[i]
        result_list.append(current_interval)
        return result_list


if __name__ == "__main__":
    # Run the solution code here
    s = Solution()

    input = [[1,5]]
    new_interval = [2,3]

    print(s.insert(input, new_interval))