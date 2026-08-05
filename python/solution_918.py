import random
from collections import deque, OrderedDict
from typing import Dict, List, Optional, Self

"""
Description: TBD
"""
class Solution:

    """
    We can use normal DP to calculate the subarray max sum of normal array
    dp[i] is the max subarray then ends at i.
    dp[i] is
        nums[i] if dp[i-1] < 0 # Just use the element since previous max sum is negative
        dp[i-1] + nums[i] if dp[i-1] > 0
    And since dp[i] only reply on previous value, we can use a single value for the dp table

    Now comes with the circular array. The idea is can we break it scenarios that without circular:
    The result can be a normal array or the one that include the start and end part of the array:
    [ 5, -2, -3, 5 ]
      *          *
    Here [5, 5] is the max subarray
    1st scenario we can solve
    2nd scenario:
        for each prefix sum at i, can we get the max of postfix sum that start after i?
            - prefix sum can be get at O(1) time when we loop the array, just keep adding elements
            - postfix sums can also get at O(1) time if we loop the array in the opposite direction. Then we can keep a list of max postfix sum when we have the postfix sum
        Now 2nd scenario can be computed like this, loop the array, from i th element, we have the prefix and the max postfix sum at i+1 or after, the new sum is the sum of these 2 values.
    """
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        current_sum = 0
        max_sum = float('-inf')

        # Calculate normal max subarray sum as if array is not circular
        for i in range(len(nums)):
            if current_sum < 0:
                current_sum = nums[i]
            else:
                current_sum += nums[i]
            max_sum = max(max_sum, current_sum)

        # Handle case like the max sum include both start and end nums
        # postfix_maxsum_list[i] is max sum from or before i to the end element
        postfix_maxsum_list: List[int] = [0 for _ in range(len(nums))]
        postfix_sum = 0

        # Calculate postfix_sum first, store it temporarily in postfix_maxsum_list
        for i in range(len(nums)-1, -1, -1):
            postfix_sum += nums[i]
            postfix_maxsum_list[i] = postfix_sum

        # Calculate postfix_maxsum
        postfix_maxsum = postfix_maxsum_list[-1]
        for i in range(len(nums)-1, -1, -1):
            postfix_maxsum = max(postfix_maxsum, postfix_maxsum_list[i])
            postfix_maxsum_list[i] = postfix_maxsum

        # Calculate prefix sum
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if i < len(nums) -1:
                new_max_sum = prefix_sum + postfix_maxsum_list[i+1]
            else:
                new_max_sum = prefix_sum
            max_sum = max(max_sum, new_max_sum)
        return int(max_sum)

    """
    As mentioned before, we know that the maximum "normal sum" is the Maximum Subarray problem which can be found with Kadane's (The DP solution explained above). As such, we can focus on finding the "special sum".

    Instead of thinking about the "special sum" as the sum of a prefix and a suffix, we can think about it as the sum of all elements, minus a subarray in the middle. In this case, we want to minimize this middle subarray's sum, which we can calculate using Kadane's algorithm as well.


    If we use Kadane's algorithm but use min() instead of max() to update the current subarray sum, it will give us the minimum subarray. Then, we can just subtract the minimum subarray from the total sum to find the "special sum".

    There is one case we need to consider however; what if the minimum subarray contains all elements, such as in the case where every element is negative? In that case, our "special sum" would represent an empty array, which is invalid because the problem explicitly states that we need a non-empty subarray.

    If we find that the minimum subarray is equal to the total sum, then we need to ignore the "special sum" and just return the "normal sum".

    Algorithm
    Calculate the maximum subarray maxSum using Kadane's algorithm.
    Calculate the minimum subarray minSum using Kadane's algorithm, by using min() instead of max().
    Calculate the sum of all the elements in nums, totalSum
    If minSum == totalSum return maxSum, otherwise return max(maxSum, totalSum - minSum).
    """
    def maxSubarraySumCircular2(self, nums: List[int]) -> int:
        current_max_sum = 0
        current_min_sum = 0
        normal_max_sum = float('-inf')
        normal_min_sum = float('inf')

        # Calculate normal max subarray sum as if array is not circular
        total_sum = 0
        for i in range(len(nums)):
            if current_max_sum < 0:
                current_max_sum = nums[i]
            else:
                current_max_sum += nums[i]

            if current_min_sum > 0:
                current_min_sum = nums[i]
            else:
                current_min_sum += nums[i]

            normal_max_sum = max(normal_max_sum, current_max_sum)
            normal_min_sum = min(normal_min_sum, current_min_sum)
            total_sum += nums[i]

        # If total sum is same as normal min sum, it means the remaining elements are zero, in this case, we should use the normal max sum
        if total_sum == normal_min_sum:
            return int(normal_max_sum)
        else:
            return int(max(normal_max_sum, total_sum - normal_min_sum))

if __name__ == "__main__":
    # Run the solution code here
    pass