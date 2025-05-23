import random
from collections import deque, OrderedDict
from typing import List, Dict

# Description: https://leetcode.com/problems/3sum/description/
'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
'''
class Solution_sort1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        print(nums)
        result: List[List[int]] = []
        
        # index is 1st element
        index = 0
        while index < len(nums):
            print(f"index: {index}")
            # Begin and end are 2nd and 3rd element
            begin = index + 1
            end = len(nums) - 1

            while begin < len(nums) - 1 and begin < end:
                target = 0 - nums[index]
                print(f"begin: {begin}, end: {end}")
                while nums[begin] + nums[end] > target and begin < end:
                    end -= 1
                if begin >= end:
                    continue
                elif nums[begin] + nums[end] == target:
                    result.append([nums[index], nums[begin], nums[end]])

                # increase begin to next non duplicate element
                # No need to reset end here, since it is sorted and
                # end is already the "closest" element of nums[begin] + nums[end] < target
                # Increase begin will make nums[begin] bigger and end should be smaller
                while begin < len(nums) - 1 and nums[begin] == nums[begin + 1]:
                    begin += 1
                begin += 1
            
            # increase index to next non duplicate element
            while index < len(nums) -1 and nums[index] == nums[index+1]:
                index += 1
            index += 1

        
        return result

# This version is more compact version
class Solution_sort2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        print(nums)
        result: List[List[int]] = []
        
        # index is 1st element
        for i in range(len(nums)):

            # Remove duplicates of 1st element
            if (i == 0 or nums[i] != nums[i-1]):
                begin = i + 1
                end = len(nums) - 1
                target = 0 - nums[i]

                # for begin from i+1, try to find the end that have the target sum
                while begin < end:
                    # Found the match
                    if nums[begin] + nums[end] == target:
                        result.append([nums[i], nums[begin], nums[end]])

                        begin += 1
                        end -= 1

                        while begin < len(nums) and nums[begin - 1] == nums[begin]:
                            begin += 1
                        while end >= 0 and nums[end] == nums[end + 1] and end < len(nums) - 1:
                            end -= 1
                    elif nums[begin] + nums[end] > target:
                        # sum too large, keep begin while decrease end
                        end -= 1
                    else:
                        # sum is small, current begin cannot have the sum, increase begin
                        begin += 1
        return result

if __name__ == "__main__":
    # Run the solution code here
    nums = nums = [-1,0,1,2,-1,-4]
    print(Solution_sort1().threeSum(nums))