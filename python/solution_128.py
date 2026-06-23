import random
from collections import deque, OrderedDict
from typing import List, Optional

"""
Description: Longest consecutive sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
class Solution:

    """
    Naive solution: sort the array and then scan it.

    O(n) solution:
    Give a number: num, we want to find if num+1 and num-1 in the array, if so, we check if num+2 or num-2 in the array. Until we cannot find the target in the array, we have the length. To avoid duplicate processing same element in the array, we can have a visited set to remember whether we have checked that element or not.

    And to check if an element in the array, we can use another set to remember the distinct element in the array, in order to check it in O(1) time.
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set: set[int] = set()

        for num in nums:
            nums_set.add(num)

        max_len = 0
        visited: set[int] = set()

        # Why keep visited set instead of remove elements from nums_set: because looping through a container while removing or adding elements to it is not safe and may cause errors. The behavior depends on how the container's iterator is implemented
        for num in nums_set:
            length = 1

            """
            Although we have inner loops, duplicate elements are remembered and we do not do inner loop for all elements. The time comlexity is O(n)
            """

            # check smaller numbers
            current_number = num - 1
            while(current_number not in visited and current_number in nums_set):
                length += 1
                visited.add(current_number)
                current_number -= 1

            # Check larger numbers
            current_number = num + 1
            while( current_number not in visited and current_number in nums_set ):
                length += 1
                visited.add(current_number)
                current_number += 1
            max_len = max(max_len, length)
        return max_len


class Solution2:

    """
    Naive solution: sort the array and then scan it.

    O(n) solution:
    Improve of Solution. We only count if the element is the start element. this way, we can remove the visited set.
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set: set[int] = set(nums)

        max_length = 0
        for num in nums_set:
            # Num is the start element, start counting
            if num-1 not in nums_set:
                current_num = num+1
                length = 1
                while current_num in nums_set:
                    length += 1
                    current_num += 1

                max_length = max(max_length, length)

        return max_length



if __name__ == "__main__":
    # Run the solution code here
    pass