import random
import heapq
from collections import deque, defaultdict, OrderedDict
from typing import Dict, List, Optional, Self, Tuple

"""
Description: Fin
You are given an integer array nums. A number x is lonely when it appears only once, and no adjacent numbers (i.e. x + 1 and x - 1) appear in the array.

Return all lonely numbers in nums. You may return the answer in any order.



Example 1:

Input: nums = [10,6,5,8]
Output: [10,8]
Explanation:
- 10 is a lonely number since it appears exactly once and 9 and 11 does not appear in nums.
- 8 is a lonely number since it appears exactly once and 7 and 9 does not appear in nums.
- 5 is not a lonely number since 6 appears in nums and vice versa.
Hence, the lonely numbers in nums are [10, 8].
Note that [8, 10] may also be returned.
Example 2:

Input: nums = [1,3,5,3]
Output: [1,5]
Explanation:
- 1 is a lonely number since it appears exactly once and 0 and 2 does not appear in nums.
- 5 is a lonely number since it appears exactly once and 4 and 6 does not appear in nums.
- 3 is not a lonely number since it appears twice.
Hence, the lonely numbers in nums are [1, 5].
Note that [5, 1] may also be returned.


Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 106
"""
class Solution:
    """
    Store all number and count in map and loop through map to check if number count is 1 and number-1 and number+1 not in map

    Or can sort array to avoid using extra storage
    """
    def findLonely(self, nums: List[int]) -> List[int]:
        count_map: Dict[int, int] = {}

        for num in nums:
            if num not in count_map:
                count_map[num] = 1
            else:
                count_map[num] += 1

        result: List[int] = []

        for num, count in count_map.items():
            if count == 1 and num-1 not in count_map and num+1 not in count_map:
                result.append(num)
        return result

if __name__ == "__main__":
    # Run the solution code here
    pass