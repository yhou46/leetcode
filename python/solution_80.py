import random
from collections import deque, OrderedDict
from typing import Dict, List, Optional, Self

"""
Description: Remove duplicates from sorted array 2
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

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

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).


Constraints:

1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
"""
class Solution:
    """
    Similar to solution 26.
    It requires in place replacement, so probably need 2 pointers: 1st one point to the next replacable slot, 2nd point the current processing slot.
    It requires at most 2 times, so we need to count the times.

    We cannot do swap since the way we check if it is different from previous element is to compare nums[i] with nums[i-1]. If we do swap, the swapped element will affect later comparison since it becomes i th element and affect later i+1 and i comparison when i proceeds
    """
    def removeDuplicates(self, nums: List[int]) -> int:

        # The pointer to the next assignable slot
        current_index = 1

        # the number if same element right at pos i
        count = 1

        for i in range(1, len(nums)):

            # New different element
            if nums[i] != nums[i-1]:
                count = 1
            else:
                count += 1

            # Only replace when count is less than 2
            if count <= 2:
                nums[current_index] = nums[i]
                current_index += 1
        return current_index

if __name__ == "__main__":
    # Run the solution code here
    pass