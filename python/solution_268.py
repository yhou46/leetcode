import random
from collections import deque, OrderedDict
from typing import Dict, List, Optional, Self

"""
Description: Missing number
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.



Example 1:

Input: nums = [3,0,1]

Output: 2

Explanation:

n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:

Input: nums = [0,1]

Output: 2

Explanation:

n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]

Output: 8

Explanation:

n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.


Constraints:

n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.


Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
"""
class Solution:
    """
    Naive solution:
    Use a hash set to remember what is in the nums, then for each 0 - n, find if it is missing in the hash set.

    Improved:
    Use total sum from 0 to n, and sum of nums.
    Then the missing number is total_sum - sum
    """
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = int(n * (n+1) / 2)

        sum = 0
        for num in nums:
            sum += num
        return total_sum - sum

if __name__ == "__main__":
    # Run the solution code here
    pass