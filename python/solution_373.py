import random
import heapq
from collections import deque, defaultdict, OrderedDict
from typing import Dict, List, Optional, Self, Tuple

"""
Description: Find K pairs with smallest sum
ou are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.



Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]


Constraints:

1 <= nums1.length, nums2.length <= 105
-109 <= nums1[i], nums2[i] <= 109
nums1 and nums2 both are sorted in non-decreasing order.
1 <= k <= 104
k <= nums1.length * nums2.length
"""
class Solution:
    """
    Brute force solution is to list all combinations m*n first and then sort, get first k result. And it takes O(m*n). But it does not utilize the fact that nums1 and nums2 are both sorted.

    One easy thinking is to have 2 pointers, p1 point to nums1, p2 points to nums2. The smallest sum must be nums1[0] + nums2[0] (denoted by (0,0), which is the index of nums1 and nums2), what about next? Can we confidently move p1 and p2 to get next element?
    Not that easy, we know that the next smallest element must be either (0,1) or (1,0). We can compare the sum and move one pointer 1 step forward, let's say (0,1), but can we say the next element is within elements of i >= 0 and j >= 1, where i and j are index of nums1 and nums2. Not really, because (1,0) could be the next smallest element, which means the pointer step backwards. So directly use 2 pointers cannot solve the problem.

    What about we check both (0,1) and (1,0)? This is the important thinking step.
    We keep the sum of (0,1) and (1,0) and make it sorted, then next one we processed the smaller one, let's say (0,1), then we push (0,2) and (1,1). Notice that (1,0) can be next smallest element and it is in the queue, so we will process it later. The queue needs to be a min heap to find the next smallest pair.

    So for i and j, we try to push (i+1,j) and (i, j+1) to heap. And to avoid processing duplicates, we use a set to remember the pairs that already pushed.

    Why it is correct?

    """
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m = len(nums1)
        n = len(nums2)
        # Sum, nums1, nums2
        min_heap: List[Tuple[int, int, int]] = [(nums1[0] + nums2[0], 0, 0)]
        result: List[List[int]] = []
        visited: set[Tuple[int, int]] = set()
        visited.add((0,0))

        while len(result) < k and len(min_heap) > 0:
            sum_val, i, j = heapq.heappop(min_heap)
            result.append([ nums1[i], nums2[j] ])

            if j+1 < n and (i, j+1) not in visited:
                heapq.heappush(min_heap, (nums1[i]+nums2[j+1], i, j+1))
                visited.add((i, j+1))

            if i+1 < m and (i+1, j) not in visited:
                heapq.heappush(min_heap, (nums1[i+1]+nums2[j], i+1, j))
                visited.add((i+1, j))
        return result

if __name__ == "__main__":
    # Run the solution code here
    pass