import random
from collections import deque, OrderedDict
from typing import Dict, List, Optional, Self

"""
Description: Remove duplicates from sorted array
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.



Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).


Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
"""
class Solution:
    """
    Thinking: the key point is to do it in place
    So we need to swap/replace elements
    Naive idea is once we find duplicates, we shift all elements after it one step, but it is slow and takes O(n^2)
    Can we avoid shift?
    One idea is to use 2 pointers: one point to the current char we are processing, the other one point to next unique element slot (all elements before it are unique)
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_index = 1

        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                # Important: instead of switch element, we do assignment
                # Why? it is possible we shift an element and later makes nums[i] != nums[i-1]
                # Example: [0,0,1,1,2,2]
                #             | |
                # if we switch 0 and 1, then it becomes 0,1,0,1,2,2, and 2nd 0,1 can trigger another switch.
                nums[unique_index] = nums[i]
                unique_index += 1
        return unique_index

if __name__ == "__main__":
    # Run the solution code here
    pass