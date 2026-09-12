import random
import heapq
from collections import deque, defaultdict, OrderedDict
from typing import Dict, List, Optional, Self, Tuple

"""
Description: Interleaving string
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.



Example 1:


Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.
Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true


Constraints:

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.


Follow up: Could you solve it using only O(s2.length) additional memory space?
"""
class Solution:
    """
    Initially a 2 pointers solution may solve the issue:
    We have p1 and p2 point to s1 and s2, and index for s3 if char at s1[p1] is same as s3[index], we move p1 and index.
    If char at s2[p2] is same as s3[index], we move p2 and index.

    If we cannot move p1 and p2, we cannot proceed and return false.

    However, this approach has one issue, what if both s1[p1] and s2[p2] are same as s3[index], which one should we move?
    Can we move either of them and give us the correct result?
    Not really, for example:
    s1 = "ab"
    s2 = "ac""
    s3 = "acab"

    In this case, if we move p1 first, then p1 is at "b" and p2 is at "a", next char in s3 is "a", we cannot proceed. But if we move p2 first, then we can get the correct result.

    So when chars are same, we need to branch out.

    Also notice that after we move either pt, s1 or s2, and s3 is one char shorter and we convert the problem to a smaller one. So a recursion can be used for checking all branches.

    But for plain recursion, we can have duplicate computations: the 2 branches may later forge at the same point and 2nd branch is doing duplicate computation as 1st one. So we need to have memorization.

    Also since recursion and memorization can be used to solve the problem, a DP solution should be possible.

    DP solution:

    dp[i][j] is whether s1[0:i], s2[0:j] can be formed s3[0:i+j], exclusive. Notice that we do not need 3rd dimension like index for s3 since s3 must be i+j

    dp[i][j] is true if
        dp[i-1][j] is true and s1[i] == s3[i+j]
        or
        dp[i][j-1] is true and s2[j] == s3[i+j]

    dp[0][j] (means only take chars from s2) is true if s2[0:j] == s3[0:j]
    dp[i][0] (means only take chars from s1) is true if s1[0:i] == s3[0:i]
    They assume length of s1 + s2 is same as s3

    """
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Need to check length here since later computation assume the length are equal
        if len(s1) + len(s2) != len(s3):
            return False

        dp: List[List[bool]] = [[False for _ in range(len(s2)+1)] for _ in range(len(s1)+1) ]
        for j in range(len(s2)+1):
            if s2[:j] == s3[0:j]:
                dp[0][j] = True

        for i in range(len(s1)+1):
            if s1[:i] == s3[:i]:
                dp[i][0] = True

        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                if dp[i-1][j] and s1[i-1] == s3[i+j-1]:
                    dp[i][j] = True

                    continue
                if dp[i][j-1] and s2[j-1] == s3[i+j-1]:
                    dp[i][j] = True

                    continue

        return dp[-1][-1]

if __name__ == "__main__":
    # Run the solution code here
    pass