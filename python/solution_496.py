import random
from collections import deque, OrderedDict
from typing import Dict, List, Optional, Self

"""
Description: the next greater element
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.



Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.


Constraints:

1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 104
All integers in nums1 and nums2 are unique.
All the integers of nums1 also appear in nums2.


Follow up: Could you find an O(nums1.length + nums2.length) solution?
"""
class Solution:
    """
    Thinking process:
    Naive solution: for each number in nums1, we first find the index in nums2, then go right to find the next greater element.
    takes len(nums1) * len(nums2) time

    We can reduce some time by scanning the nums2 array and remember the number -> index mapping using hash map but still len(nums1) * len(nums2) time

    Since nums1 is the subset of nums2, can we compute all next greater elements of nums2 and use hash map to remember the result, then we just need to look up the result.

    Then problem becomes how to quickly get all next greater elements (NGE) of all elements in nums2. The NGE of last element is obviously -1. And looks like we should compute from right to left, from intuition.

    | | |i| | |j| | |
    Assume we are computing the next element of nums2[i] and find nums[j] is the next greater element, then we need to compute NGE of nums2[i-1].

    We know some facts:
        - elements between i and j are all less than nums[i]
        - nums[i] < nums[j]
    Then if nums[i-1] > nums[i], then the NGE could be nums[j] or some elements after nums[j]
    if nums[i-1] < nums[i], then the NGE is nums[i].
    Looks like we can ignore all elements that smaller than nums[i] and between i and j.
    A stack can help here: it can remember the elements from right to left in order and keep recent element that is larger than the nums[i]

    """
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i = len(nums2) - 1

        next_greater_map: Dict[int, int] = {}
        stack: deque[int] = deque()
        for i in range(len(nums2)-1, -1, -1):
            number = nums2[i]
            if i == len(nums2) - 1:
                next_greater_map[number] = -1
                stack.append(number)
            else:
                while len(stack) > 0 and stack[-1] <= number:
                    # Pop until find the element that is larger than current number
                    stack.pop()
                if len(stack) == 0:
                    next_greater_map[number] = -1
                else:
                    next_greater_map[number] = stack[-1]
                stack.append(number)

        result: List[int] = []
        for number in nums1:
            result.append(next_greater_map[number])
        return result

if __name__ == "__main__":
    # Run the solution code here
    pass