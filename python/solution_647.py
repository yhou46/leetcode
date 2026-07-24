import random
from collections import deque, OrderedDict
from typing import Dict, List, Optional, Self

"""
Description: Palindromic substrings
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.



Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
"""
class Solution:
    """
    Thinking:
    check if a string is palindrome takes O(n)
    A string can have O(n^2) number of substrings so brute force takes O(n^3)

    DP solution
    dp[i][j]: whether substring [i,j] is palindrome
    dp[i][j] = true:
        when i+1 <= j-1, if dp[i+1][j-1] is true and str[i] == str[j]
        when j == i-1, and dp[i] == dp[j]
        when i== j, True
    dp[i][i] = True, for i from 0 to len(str)

    dp make progresses on a diagonal direction
    base case is i==j, the diagonal and i <= j
    When we have populate the line of i = j, we need to progress to j = i + 1, i from 0 to len(s)

    """
    def countSubstrings(self, s: str) -> int:
        dp: List[List[bool]] = [[False for _ in range(len(s))] for _ in range(len(s))]

        count = 0

        for m in range(len(s)):
            for i in range(len(s)):
                j = i + m
                if j >= len(s):
                    break;
                if i == j:
                    dp[i][j] = True
                    count += 1
                elif j == i+1:
                    if s[i] == s[j]:
                        dp[i][j] = True
                        count += 1
                else:
                    if s[i] == s[j] and dp[i+1][j-1]:
                        dp[i][j] = True
                        count += 1
        # print(f"dp: {dp}")
        return count

    """
    A palindrome has middle point, it is either one char or 2 chars depending on the length is odd or even. So we can assume each char is middle point, move 2 pointers to grow from middle to left and right and check if they are same.
    It saves time to when checking a substring is palindrome or not. And we stop early if we find the chars are different.
    """
    def countSubstrings2(self, s: str) -> int:
        count = 0
        for i in range(0, len(s)):

            # Check if middle point is i, odd length of substr
            left = i
            right = i
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    count += 1
                else:
                    break
                left -= 1
                right += 1

            # Check if i and i+1 are the middle point, even length
            if i+1 < len(s):
                left = i
                right = i+1
                while left >= 0 and right < len(s):
                    if s[left] == s[right]:
                        count += 1
                    else:
                        break
                    left -= 1
                    right += 1
        return count



if __name__ == "__main__":
    # Run the solution code here
    input = "fdsklf"

    s = Solution()
    print(f"{s.countSubstrings2(input)}")