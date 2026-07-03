import random
from collections import deque, OrderedDict
from typing import List, Optional

"""
Description: TBD
"""
class Solution:
    """
    Similar to binary search since we can use mid to determine whether the smallest element is in the left or right part

    """
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] < nums[right]:
                return nums[left]

            # Here we use floor to calculate mid, so when right = left + 1, mid = left
            # We need to make sure left always proceed +1 step, otherwise it enters infinite loop
            mid = (left + right) // 2
            if nums[mid] > nums[left]:
                left = mid + 1
            elif nums[mid] < nums[left]:
                right = mid
            else:
                # in this case, left = mid = right-1
                return min(nums[left], nums[right])
        return nums[left]

    def findMin2(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            # Here we use floor to calculate mid, so when right = left + 1, mid = left
            # We need to make sure left always proceed +1 step, otherwise it enters infinite loop
            mid = (left + right) // 2

            # Here we can comare nums[mid] with nums[left] or nums[right]
            if nums[mid] > nums[right]:
                # Left has to proceed 1
                left = mid + 1
            # Unlike comparing to nums[left], if we compare with right element, mid is never equal to right, because we use floor to calculate mid, rather than ceiling (left + right + 1) // 2
            else:
                right = mid
        return nums[left]

if __name__ == "__main__":
    # Run the solution code here
    pass