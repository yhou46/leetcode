import random
from collections import deque, OrderedDict
from typing import Dict, List, Optional, Self

"""
Description: Product of array exclude itself
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.


Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""
class Solution:
    """
    One naive idea is to use total product divide by the current element.
    But since it mentions we cannot use divide operator, also we cannot divide by zero if element is zero. The division approach need some extra handling anyway.

    So without divide, brute force solution is for each element, calculate product before it and after it, then multiply the result. It take O(n^2) time

    Notice that we have duplicate calculation in brute force approach:
        [3,2,1,4] -> we calculate product of 3, 3*2, 3*2*1 and 3*2*1*4.
    So we can do prefix product and postfix product to calculate it before hand, then just look it up when calculate the final result.
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_array: List[int] = []

        product = 1
        for num in nums:
            product *= num
            prefix_array.append(product)
        print(f"pre_product: {prefix_array}")

        postfix_array: List[int] = [0 for _ in range(len(nums))]
        product = 1
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            product *= num
            postfix_array[i] = product
        print(f"post_product: {postfix_array}")

        result: List[int] = []

        for i in range(0, len(nums)):
            pre_product = prefix_array[i-1] if i > 0 else 1
            post_product = postfix_array[i+1] if i < len(nums)-1 else 1
            result.append(pre_product * post_product)

        return result

    """
    Do we really need 2 arrays for both prefix and postfix?
    Notice that when we loop through the input to get the final result, we can get prefix product easily. So no need for prefix product array.

    For postfix product:
        - to calculate result[i] we only need post product if i+1, it means we can override post_product[i]
    then we only need post product before hand and it can be stored in final result array.
    """
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        postfix_product: List[int] = [0 for _ in range(0, len(nums))]

        product = 1
        for i in range(len(nums)-1, -1, -1):
            product *= nums[i]
            postfix_product[i] = product

        # Compute final result
        previous_product = 1
        for i in range(0, len(nums)):
            postfix_product[i] = previous_product * (postfix_product[i+1] if i < len(nums)-1 else 1)
            previous_product *= nums[i]
        return postfix_product


if __name__ == "__main__":
    # Run the solution code here
    pass