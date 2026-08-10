import random
from collections import deque, defaultdict, OrderedDict
from typing import Dict, List, Optional, Self, Tuple

"""
Description: Jump game 2

You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.



Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
"""
class Solution:
    """
    dp[i] is min jump time from 0 to i
    then dp[i] = min of dp[j] + 1, where j < i and nums[j] + j >= i
    dp[0] = 0

    Time: O(n^2)
    space: O(n)
    """
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        dp: List[int] = [ -1 for _ in range(len(nums)) ]
        dp[0] = 0

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] + j >= i:
                    if dp[i] == -1:
                        dp[i] = dp[j] + 1
                    else:
                        dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]

    """
    Messy version but O(n) time

    Greedy, assume we are at position i, then we can proceed to max range if i+nums[i]
    Then which location should we jump?
    The answer is to check the range of next step and choose the max one to step.
    Example:
    [3,3,5,2, ...] And we are at 0, and we can jump to 3,5 or 2.
    If we check the max range from index 0, we know from index 1(which is 3), we can jump to max index at 4 (0 -> 1 -> 4). We can do calculation for index 2 and 3,
    so for
    index 1, step = 3, max jump index is 4
    index 2, step = 5, max jump index is 7
    index 3, step = 2, max jump index is 5
    So from index 0, we should jump to index 2 since it makes us jump the farest.
    And we continue to do this step until we reach the end.

    WHy it works?
    Because if we choose the index that has max distance to jump, it then covers the range of all other index (since it reaches the maximum index), and the number of jump is minimal in this case
    """
    def jump2(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        count = 0
        pos = 0

        while pos < len(nums)-1:

            new_pos = pos
            max_pos = pos
            for i in range(pos+1, pos + nums[pos]+1):
                # Already reach the end, no need to check further
                if i >= len(nums)-1:
                    new_pos = i
                    break
                if max_pos < i+nums[i]:
                    max_pos = i+nums[i]
                    new_pos = i
            count += 1
            pos = new_pos

        return count

if __name__ == "__main__":
    # Run the solution code here
    input = [1,2,1,1,1]
    s = Solution()
    print(f"result: {s.jump2(input)}")