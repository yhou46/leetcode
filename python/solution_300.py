import random
from collections import deque, OrderedDict
from typing import Dict, List, Optional, Self

"""
Description: Longest increasing subsequence
Given an integer array nums, return the length of the longest strictly increasing subsequence.



Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1


Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104


Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""
class Solution:
    """
    Can we solve it in a brute force way first?
    For example, assume the longest sub sequence start at element i, if element i+1 is larger then element i, can we 100% it can be added to the sequence?
    Not really, for example: [2,8,5,6], 8 is larger than 2 but it should not be added to the result since it blocks later element to be added to the result.
    So we need to iterate elements after i.
    So for j > i, we want to check:
        if nums[j] > nums[i] and we have max_len[j], then max_len[i] = 1 + max_len[j], if 1 + max_len[j] is larger.
    So a DP like problem.

    To make it simpler, we can use the ending element rather than the start element since using the start element makes us loop from end to start.

    dp[i] is the max length of increasing sequence that ends at nums[i]

    dp[i] = for all elements j < i and nums[j] > nums[i], the max value of nums[j] + 1

    dp[0] = 1 since only one element.

    O(n^2) time
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        dp: List[int] = [1 for _ in range(0, len(nums))]
        max_length = 1

        for i in range(1, len(nums)):

            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            # print(f"i: {i}, dp: {dp[i]}")
            max_length = max(max_length, dp[i])
        return max_length

if __name__ == "__main__":
    # Run the solution code here
    pass