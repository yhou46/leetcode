import random
from collections import deque, OrderedDict
from typing import Dict, List, Optional, Self

"""
Description: Counting bits
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.



Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101


Constraints:

0 <= n <= 105


Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
"""
class Solution:
    """
    Naive solution: least bit is 1 if number % 2 is 1, then we do num = num // 2 to proceed to next bits
    """
    def countBits(self, n: int) -> List[int]:
        result: List[int] = [0 for _ in range(n+1)]

        for i in range(1, n+1):
            count = 0
            num = i
            while num != 0:
                temp = num % 2
                if temp == 1:
                    count += 1
                num = num // 2
            result[i] = count
        return result

    """
    Bit manipulation:
    If we can get bit count of each number, then we just loop through n to get the final result.

    The key idea here is to realize that for any number n, doing a bit-wise AND of n and n-1 flips the least-significant 1-bit in n to 0.

    Example:

    num:      101100...100
    num-1:    101100...011
    & result: 101100...000
    The least 1 bits is reset to 0 while all other bits remains unchanged.
    We just do it for all bits until num is zero
    """
    def countBits2(self, n: int) -> List[int]:
        result: List[int] = [0 for _ in range(n+1)]

        def get_bit_count(num: int) -> int:
            count = 0

            while num != 0:
                count += 1
                num &= num-1
            return count

        for i in range(1, n+1):
            result[i] = get_bit_count(i)
        return result

if __name__ == "__main__":
    # Run the solution code here
    pass