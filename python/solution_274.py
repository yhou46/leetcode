import random
from collections import deque, defaultdict, OrderedDict
from typing import Dict, List, Optional, Self, Tuple

"""
Description: TBD
"""
class Solution:
    """
    The target is to find the max number i that citations has more count of elements larger than i
    What if we sort it? Sort guarantees that all elements after element i are larger or equal than element i. Then we just need to check if it satisfies the requirements: assume n is total number of citations, for index i, n-i is the number of elements that larger than element i, then if element i is larger than n-i then n-i is the h index.

    Time complexity: O(n*log(n)) since we do sort
    Space: O(1)
    """
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)

        for i in range(n):
            if citations[i] >= n-i:
                return n-i

        # For loop does not return, it means citations has all zeros.
        # Why because if citations has at least one number that is larger than 0, then h index is at least 1.
        return 0

    """
    Assume citations have n elements, then h index is 0 <= h <= n
    Then we can use binary search to check if a candidate satisfy the condition
    To check if a number: i, satisfy the condition, we count the elements and check if element[i] >= count

    Time: n*log(n)
    Space: O(1)
    """
    def hIndex2(self, citations: List[int]) -> int:
        start = 0
        end = len(citations)


        while start < end:
            mid = (start + end + 1) // 2

            # Check if mid satisfy the condition
            count = 0
            for i in range(len(citations)):
                if citations[i] >= mid:
                    count += 1

            # Found a match
            if count >= mid:
                start = mid
            else:
                end = mid - 1
        return start

    """
    In binary search, we need O(n) time to check if a number satisfies h-index requirements, can we make it quicker?
    If we count all citations before hand, like keeping a map: key is the count of citations and value is the how many paper has that count of citations, and it is sorted, then it is much easier.

    The citations is given as a list and is using a number as the key of the paper, this makes it possible to use a integer array to represent the map and it is sort by count of citations inherently.
    then we just need to loop from end and keep a total count to represent the total count regarding to the total number of papers that has citation larger than a value.
    Since the h-index cannot exceed the total length of the citations, if a paper's citation is larger than the length, we just suppresseed (add count) to the index n. So the total map need n+1 entries
    """
    def hIndex3(self, citations: List[int]) -> int:
        n = len(citations)
        count_list: List[int] = [0 for _ in range(n+1)]

        for citation in citations:
            if citation >= n:
                count_list[-1] += 1
            elif citation >= 0:
                count_list[citation] += 1
            else:
                raise ValueError(f"Invalid negative citation: {citations}")

        total_count = 0
        for i in range(n, -1, -1):
            total_count += count_list[i]
            if total_count >= i:
                return i
        raise ValueError(f"Unexpected error happens")



if __name__ == "__main__":
    # Run the solution code here
    input = [3,0,6,1,5]
    input = [0,0]
    s = Solution()

    print(s.hIndex3(input))