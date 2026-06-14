import random
from collections import deque, OrderedDict
from typing import List

# Description: 55 Jump game
"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.



Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # Whether can jump from 0 to position i
        # Cache result to avoid duplicated caculation
        can_jump_list: List[bool | None] = [None for _ in range(len(nums))]

        return self.recursion(
            nums,
            len(nums)-1,
            can_jump_list,
        )

    """
    Recursion: start from end, and check if prevous position can reach the end, then for each previous position, check its previous position again
    """
    def recursion(self,
        nums: List[int],
        position: int,
        can_jump_list: List[bool | None],
        ) -> bool:
        if position == 0:
            return True

        save_result = can_jump_list[position]
        if isinstance(save_result, bool):
            return save_result

        can_jump = False
        for i in range(position-1, -1, -1):
            max_step = nums[i]
            if max_step >= (position - i):
                can_jump = self.recursion(
                    nums,
                    i,
                    can_jump_list,
                )
                if can_jump:
                    can_jump_list[position] = True
                    return can_jump
        can_jump_list[position] = False
        return False


class Solution2:
    def canJump(self, nums: List[int]) -> bool:

        # Max index we can reach from index i
        max_reach = 0

        for i in range(0, len(nums)):

            # False if max_reach cannot make us reach index i
            if max_reach < i:
                return False

            # Update max reach if index i + its steps is larger than current vaue
            max_reach = max(max_reach, i+nums[i])
        return True




if __name__ == "__main__":
    # Run the solution code here
    s = Solution2()
    input = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
    print(s.canJump(input))