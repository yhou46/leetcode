import random
import heapq
from collections import deque, defaultdict, OrderedDict
from typing import Dict, List, Optional, Self, Tuple

"""
Description: Trapping rain water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.



Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9


Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""
class Solution:
    """
    The hard part is how to calculate the water at a height.
    Idea: the water can be captured at height i is determined by its left max height and right max height. The left max height means the max height from 0, 1 to i. And the right max height means the max height from i, i+1, ... n-1

    If we have max left and right height, then the water is min(max_left_height, max_right_height) - height[i] when height[i] is lower than its left/right max height.

    With above idea, for each index, we just need to max left and right height. When we loop from 0 -> n, we naturally get max left height at i if we keep the max_height variable and updated it with height. But for right max height, we need to calculate each time. To save time, we can recompute it by looping from n-1 -> 0

    """
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_right_heights: List[int] = [0 for _ in range(n)]

        max_right_height = 0
        for i in range(n-1, -1, -1):
            max_right_height = max(max_right_height, height[i])
            max_right_heights[i] = max_right_height

        water = 0
        max_left_height = 0
        for i in range(n):
            max_left_height = max(max_left_height, height[i])
            bar_height = min(max_left_height, max_right_heights[i])
            if bar_height > height[i]:
                water += bar_height - height[i]
        return water

if __name__ == "__main__":
    # Run the solution code here
    pass