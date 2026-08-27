import random
import heapq
from collections import deque, defaultdict, OrderedDict
from typing import Dict, List, Optional, Self, Tuple

"""
Description: Minimum number of shorts to burst balloon
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.



Example 1:

Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
Example 2:

Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
Example 3:

Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].


Constraints:

1 <= points.length <= 105
points[i].length == 2
-231 <= xstart < xend <= 231 - 1
"""
class Solution:
    """
    In the worst case, every point needs a shot.
    We can think of a vertial line moving from left to right, and when it sees the more balloon overlaps, it fires. But it should also fire if there is no overlap but it is at the balloon's end index.

    So we need to sort the points first, but under what criteria? Start index or end index. The idea here is that we can delay the shot for current balloon until we find a overlap or it is the current balloon's end. So in this case, we should sort by point's end index.

    We loop through the points. We remember current point's end index, if next point has overlapping, we move on since there could be more overlapping. We have to shot if no overlapping anymore. In this case, we increase counter and move the end index to the next point.
    """
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        print(points)

        count = 0
        current_point = points[0]

        for i in range(1, len(points)):
            point = points[i]

            # has overlapping, move on
            if point[0] <= current_point[1]:
                continue
            else:
                # No overlap, needs to fire
                count += 1
                current_point = point
            # print(f"point: {point}, count: {count}")
        count += 1 # last current is not processed yet
        return count

    """
    At the first glance, it is similar to merge intervals but this time we need to find the overlaps, so first we might want to sort by first index. When we find any overlap, we shoot within the overlaps to minimize the shorts. So the min short depends on the number of overlapped intervals we can find

    Assume the points is sorted by first index, we try to compute the overlapped intervals. When we find the next point does not have any overlap with the current interval, we added it to the result array. And at the end, we return the length of the result array.
    """
    def findMinArrowShots2(self, points: List[List[int]]) -> int:
        points.sort()

        shrinked: List[List[int]] = []
        current = points[0]

        for i in range(1, len(points)):
            point = points[i]
            # Find overlap, merge it
            if point[0] <= current[1]:
                current[0] = point[0]
                current[1] = min(current[1], point[1])
            else:
                # No overlap, need to start from current one, add merged one to final result
                shrinked.append(current)
                current = point

        # Since the last "current" is not added yet, we add it to final result
        shrinked.append(current)

        # print(shrinked)
        return len(shrinked)

if __name__ == "__main__":
    # Run the solution code here
    pass