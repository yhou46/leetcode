import random
from collections import deque, OrderedDict
from typing import List, Dict

"""
Minimum window substring
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.


Follow up: Could you find an algorithm that runs in O(m + n) time?
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # char_dict is used to remember the chars in t
        char_dict: Dict[str, int] = {}
        for ch in t:
            if ch not in char_dict:
                char_dict[ch] = 1
            else:
                char_dict[ch] += 1

        # char_dict and remaining chars used together to detect whether a substring from start to end has all chars of t.
        # the char dict itself is not sufficient here.
        remaining_chars = len(t)

        start = 0
        end = 0
        min_window_start = 0
        min_window_end = len(s)

        found = False
        while end < len(s):
            # Move end first
            current_char = s[end]
            if current_char in char_dict:
                # If the char is in the dict, we decrease count
                # The count can be below zero, indicates we have unnecessary chars included from start to end
                char_dict[current_char] -= 1

                # We only decrease counter when the char in map is larger than zero, because if it is negative, it means current char is redundant (we already have too many of it)
                if char_dict[current_char] >= 0:
                    remaining_chars -= 1
            end += 1

            # End has moved to a position that has all chars from t
            if remaining_chars == 0:

                # it is possible that s does not contains all chars from t, so we need a flag here to indicate whether it ever reaches this flow
                found = True
                while start <= end:
                    # We move start to a position that does not have all chars in t
                    start_char = s[start]
                    if start_char in char_dict:
                        # We cannot move start anymore
                        if char_dict[start_char] == 0:
                            break
                        char_dict[start_char] += 1
                    start += 1


                if min_window_end-min_window_start > end - start:
                    min_window_start = start
                    min_window_end = end

                if s[start] in char_dict:
                    char_dict[s[start]] += 1
                remaining_chars += 1
                start += 1

        if found:
            return s[min_window_start:min_window_end]
        else:
            return ""



if __name__ == "__main__":
    # Run the solution code here
    s = Solution()

    input1 = "ADOBECODEBANC"
    input2 = "ABC"
    print(s.minWindow(input2, input1))