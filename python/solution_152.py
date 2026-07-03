import random
from collections import deque, OrderedDict
from typing import List, Optional

"""
Description: Max product subarray
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that element.



Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
"""
class Solution:
    """
    Thinking process:

    Naive solution:
    Calculate every product of subarray and remember the max:
        For subarray start at i, calculate all products of subarrays from i to i, from i to i+1, ... (max of n times if i is zero)
        n^2 time complexity
    We have duplicates, for [2,3,-2,4], start from 2,  calculate 2 * 3, then 2 * 3 * -2, then 2 * 3 * -2 * 4
    then start from 3, we calculate 3 * -2, 3 * -2 * 4

    Can we use DP like approach?
    Example: dp[i] is the max product that ends at i, then how to get it from dp[i-1]?

    if nums[i] > 0:
        if dp[i-1] > 0:
            dp[i] = dp[i-1] * nums[i]
        else: # dp[i-1] <= 0
            dp[i] = nums[i]

    if nums[i] == 0:
        dp[i] = 0
    if nums[i] < 0:
        # Tricky here since if we have a very small negative product ending at i-1, we can have a large positive product
        # So we need to track the min value too, dp_min[i]
        if dp_min[i-1] < 0:
            dp[i] = max(dp_min[i-1] * nums[i])
        else:
            dp[i] = nums[i]

    Now we need to get dp_min as well, notice that dp_min has similar logic since a large positive value * negative number becomes smaller.

    And we only need i-1 to get i. So not need to have a table.
    dp_max, and dp_min can be the max/min of (dp_max[i-1] * nums[i], dp_min[i-1] * nums[i], nums[i])


    """
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            raise ValueError("Empty array")

        # negative min product times negative number becomes the max so need to remember min and max
        current_max = nums[0] # max product that ends at i
        current_min = nums[0] # min product that ends at i

        max_product = max(current_max, current_min)

        for i in range(1, len(nums)):
            # Important to use temp here since current_max needs to be reused for the current_min calculation
            temp_max = max(current_max * nums[i], current_min * nums[i], nums[i])
            temp_min = min(current_max * nums[i], current_min * nums[i], nums[i])
            current_max = temp_max
            current_min = temp_min
            # print(f"nums[i]: {nums[i]}, current_max: {current_max}, current_min: {current_min}")
            max_product = max(current_max, max_product)
        return max_product

if __name__ == "__main__":
    # Run the solution code here
    pass