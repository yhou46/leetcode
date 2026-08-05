import random
from collections import deque, OrderedDict
from typing import Dict, List, Optional, Self

"""
Description: Rotate array
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.



Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
"""
class Solution:
    """
    Thinking process:
    Naive solution: copy the original list, then assign the existing list by using the copied list:
    like nums[(i+k)%n] = copy_nums[i]
    Need O(n) space

    Or we do it 1 step at a time, shift it element by element for 1 step, then do it k times. O(1) space but O(nk) time

    Can we move the element directly to its destination at once?
    We know i th element's destination is (i+k) % n, where n = len(nums)
    But we need copies since assignment make us lose element at (i+k) % n
    What about we switch (i+k) % n th elmement after switch i th element, then we only need to store one element.

    If we keep doing it, does it cover all elements?

    0 1 2 3 4 and k = 2,

    the order of shift is 0 -> 2 -> 4 -> 1 -> 3, looks like it covers all elements

    But is it possible that the loop come back to the original point?
    Yes, need proof.

    If n % k == 0, like n= 6 and k=2, then we jump back to the original point.
    In this case, we need to do increase start point by 1

    Then we have the O(n) time and O(1) space solution

    """
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # How many shifts we did
        count = 0
        n = len(nums)
        # index and next index
        index = 0

        previous = nums[index]
        start = index

        while count < len(nums):
            new_index = (index + k) % n
            print(f"index: {index}, new_index: {new_index}")

            temp = nums[new_index]
            nums[new_index] = previous
            index = new_index
            previous = temp
            count += 1

            # This is the n % k == 0 case, we increase index by 1 instead of looping the same elements
            if index == start:
                index = (index + 1) % n
                start = index
                previous = nums[start]

if __name__ == "__main__":
    # Run the solution code here
    pass