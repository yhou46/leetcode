import random
from collections import deque, OrderedDict
from typing import List, Dict, Optional

"""
Description: Perfect square
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.



Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.


Constraints:

1 <= n <= 104
"""
class Solution:
    """
    dp[i] is the min count square of i
    n can be divided like below:
    n = i*i + j, for i*i < n

    dp[n] = min (dp[i*i] + 1) for i*i < n or 1 if we find n = i*i

    The min count of n is 1 + dp[i*i]. And we need the min count of i*i

    dp[1] = 1
    """
    def numSquares(self, n: int) -> int:

        # Why init dp as 0,1,2,3,4?
        # Because the max value for n is n since n = 1 + 1 + 1 + ...
        dp: List[int] = [ i for i in range(n+1) ] # Initial value [0,1,2,3,4...]
        dp[1] = 1

        # Only used to get the path to the num, like for 12, the path is 4,4,4
        map: Dict[int, List[int]] = {}
        map[1] = [1]

        for i in range(2, n+1):

            j = 1
            while j*j <= i:
                if j*j == i:
                    dp[i] = 1
                    map[i] = [i]
                    break

                # This is to get the path of the perfect squares
                if 1 + dp[i-j*j] <= dp[i]:
                    # Update list if min value is updated
                    new_list = map[i-j*j].copy()
                    new_list.append(j*j)
                    map[i] = new_list

                dp[i] = min(dp[i], 1 + dp[i-j*j])
                j += 1
            # print(f"i: {i}, dp[i]: {dp[i]}")
        print(map[n])
        return dp[n]

if __name__ == "__main__":
    # Run the solution code here
    s = Solution()

    print(s.numSquares(1000))