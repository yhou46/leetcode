import random
from collections import deque, OrderedDict
from typing import Dict, List, Optional, Self

"""
Description: House robber 2
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""
class Solution:
    """
    Thinking process:
    Since it is circular, whether robs at index 0 affect whether robs at the last index. Simple dp approach does not work.

    Can we cut the circle somewhere to make it into the previous non circular problem?

    Notice that the max profits must be done by either robbing at index 0 or not robbing at index 0. So it gives us 2 possibilities:
        - rob at index 0, which means we cannot rob at last index
            - It means last element does not matter since we do not rob
                - Convert to problem: we rob a subset of nums from 0 to n-1
        - not rob at index 0, which means we choose either rob or not rob at last index
            - It means index 0 does not matter, since we do not rob
                - Convert to problem: we rob a subset of nums from 1 to n

    So now the problem is divided into:
        calculate the max profix from 0 - n-1 and from 1 to n, then get the max value and we can reuse the same trick as before (the DP one)

    """
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        amount_rob_first = self.rob_helper(nums[:-1])
        amount_not_rob_first = self.rob_helper(nums[1:])

        return max(amount_rob_first, amount_not_rob_first)

    """
    Helper function to compute non circular rob
    dp_rob[i]: max profit from 0 to i and rob at location i
    dp_not_rob[i]: max profix from 0 to i and not rob at location i

    dp_rob[i] = nums[i] + dp_not_rob[i-1]
    dp_not_rob[i] = max(dp_rob[i-1], dp_not_rob[i-1]

    dp_rob[0] = nums[0]
    dp_not_rob[0] = 0
    """
    def rob_helper(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp_rob = nums[0]
        dp_not_rob = 0

        for i in range(1, len(nums)):
            temp_rob = dp_rob
            dp_rob = nums[i] + dp_not_rob
            dp_not_rob = max(temp_rob, dp_not_rob)
            # print(f"rob at {i}: {dp_rob}, not rob at {i}: {dp_not_rob}")
        return max(dp_rob, dp_not_rob)

if __name__ == "__main__":
    # Run the solution code here
    pass