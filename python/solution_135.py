import random
from collections import deque, defaultdict, OrderedDict
from typing import Dict, List, Optional, Self

"""
Description: Candy
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.



Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.


Constraints:

n == ratings.length
1 <= n <= 2 * 104
0 <= ratings[i] <= 2 * 104
"""
class Solution:
    """
    If we simply do it from left to right: like assign the candy count at i based on i-1 and i+1, then the current assignment will affect later values. For example, initial count is [1,1,1,1] and score is [1,3,2,1]
    When processing 3 (index 1), since index 0 is 1 and index 2 is 1, index 1 should be 2 as minimal count, but later when processing index 2, index 2 should be 2 since its right has lower rating but this change affect index 1 since rating changed. [1,2,2,1] is the wrong result.

    When processing from left to right, it only guarantees the min count of its left neighbors. Then can we do it in 2 passes? From left to right and from right to left?
    """
    def candy(self, ratings: List[int]) -> int:
        result_from_left: List[int] = [ 1 for _ in range(len(ratings))]

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                result_from_left[i] = result_from_left[i-1] + 1

        result_from_right: List[int] = [ 1 for _ in range(len(ratings))]
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                result_from_right[i] = result_from_right[i+1] + 1

        count = 0
        for i in range(len(ratings)):
            count += max(result_from_left[i], result_from_right[i])
        return count

if __name__ == "__main__":
    # Run the solution code here
    pass