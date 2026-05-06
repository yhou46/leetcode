from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        k = -1
        while left < right:
            k = (left + right) // 2
            print(f"k: {k}, left: {left}, right: {right}")
            if k > 0 and k < len(nums) -1:
                if nums[k] > nums[left]:
                    left = k
                else:
                    right = k

            elif k == 0 or k == (len(nums) -1):
                break
        index = left
        print(f"index: {index}")

        if target >= nums[0]:
            return self.binary_search(nums, 0, index, target)
        else:
            return self.binary_search(nums, index+1, len(nums)-1, target)

    def binary_search(self, nums: List[int], start: int, end: int, target: int) -> int:
        if start > end:
            return -1
        if start == end and nums[start] == target:
            return start
        while start < end:
            mid = (start + end) // 2
            if target > nums[mid]:
                start = mid+1
            elif target < nums[mid]:
                end = mid-1
            else:
                return mid
        if start == end and nums[start] == target:
            return start
        else:
            return -1


if __name__ == "__main__":
    # Run the solution code here
    s = Solution()
    #input = [7,8,9,0,3,4,5]
    input = [0,1,2]
    print(s.search(input, 0))

    #print(s.binary_search(input, 3, len(input)-1, 3))