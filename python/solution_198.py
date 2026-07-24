import random
from collections import deque, OrderedDict
from typing import List, Optional

"""
Description: House robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
"""
class Solution:
    """
    dp_rob[i] max value from 0 to i, if we rob at position i
    dp_not_rob[i] max value from 0 to i, if we do not rob at position i

    dp_rob[i] = dp_not_rob[i-1] + nums[i]
    dp_not_rob[i] = max(dp_not_rob[i-1], dp_rob[i-1])

    dp_rob[0] = nums[0]
    dp_not_rob[0] = 0

    And since dp[i] only depends on dp[i-1] we only need to store 2 previous states: rob or not_rob
    """
    def rob(self, nums: List[int]) -> int:

        dp_rob = nums[0]
        dp_not_rob = 0

        for i in range(1, len(nums)):
            temp_rob = dp_not_rob + nums[i]
            temp_not_rob = max(dp_rob, dp_not_rob)
            dp_rob = temp_rob
            dp_not_rob = temp_not_rob
        return max(dp_rob, dp_not_rob)

if __name__ == "__main__":
    # Run the solution code here
    pass