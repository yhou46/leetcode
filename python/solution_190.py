import random
from collections import deque, OrderedDict
from typing import List, Optional

"""
Description: Reverse bits
Reverse bits of a given 32 bits signed integer.


Example 1:

Input: n = 43261596

Output: 964176192

Explanation:

Integer	Binary
43261596	00000010100101000001111010011100
964176192	00111001011110000010100101000000
Example 2:

Input: n = 2147483644

Output: 1073741822

Explanation:

Integer	Binary
2147483644	01111111111111111111111111111100
1073741822	00111111111111111111111111111110


Constraints:

0 <= n <= 231 - 2
n is even.


Follow up: If this function is called many times, how would you optimize it?
"""
class Solution:
    """
    32 bits int has fixed number of bits
    let's take one short example: 1110,1011
    We want 1101,0111
    We can cut in middle and swap left and right:
    1110,1011 -> 1011,1110
    Then for left and right part, we cut in the middle again and swap them
    We do it until there is only one bit and then we are done

    The flow:
    1110,1011 -> 1011,1110 -> 11,10,10,11 -> 1,1,0,1,0,1,1,1
    """
    def reverseBits(self, n: int) -> int:

        # a int & (AND) a mask means we reset bits to be the mask itself (since 1 & 1 = 1, 1 & 0 = 0)
        # So n & 0xffff0000 means we remove all lower 16 bits, only keep the high 16 bits, then move higher 16 bits to the right, left new higher bits to be zero
        # The | (OR) combines the left part and right part together since 0 | any bits = any bits (no op)
        n = ((n & 0xffff0000) >> 16) | ((n & 0x0000ffff) << 16)

        # This one is tricky, since we want to swap the bits inside left and right part, instead of do it for each part, we can do it in one run:
        # 10 11,11 10, we can shift A, C to the right(8 bits ) and B, D to the left (move 8 bits), it achieve the same
        # A  B  C  D
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)

        # Similar to above steps
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)

        return n

if __name__ == "__main__":
    # Run the solution code here
    pass