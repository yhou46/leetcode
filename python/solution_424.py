import random
from collections import deque, OrderedDict, defaultdict
from typing import Dict, List, Optional, Self

"""
Description: Longest repeating character replacement
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.



Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.


Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""
class Solution:
    """
    Apparently the replacement should be one of the chars appears in the input string.
    So which one to use?
    We can find the number of unique chars. And try each of them to get max length, loop to get max length.
    The problem is converted to use k replacement of char and how to get max length of input string.
        - Idea is to use 2 pointers approach: we have start and end pointers. We move end until we cannot move: when we have used up all k replacements
        Then we move start pointers until the substring is value again. Then move end pointer.
        - How to check if we used up all k replacements?
            - We can get the substring length by using end - start + 1 and if we count the number of char in the substring, then the insertion count is len(substr) - count(char)

    Complexity:
    if the number of unqiue char is m. Then it is O(m*n) since each unique char needs full scan of the input string

    """
    def characterReplacement(self, s: str, k: int) -> int:
        unique_chars: set[str] = set([char for char in s])

        result = 0
        for char in unique_chars:
            result = max(result, self.max_length(s, k, char))
        return result

    # Get max length using k replacement for char
    # 2 pointers
    def max_length(self, input: str, k: int, char: str) -> int:

        # 2 pointers: start, end means substring [start:end], both inclusive
        start = 0
        count = 0 # count of char
        end = 0

        max_len = 0

        while end < len(input):
            if input[end] == char:
                count += 1
            else:
                # Move start
                # end - start + 1 is current substring length, end - start + 1 - count is the total insertion
                while end - start + 1 - count > k:
                    if input[start] == char:
                        count -= 1
                    start += 1
            max_len = max(max_len, end-start+1)
            end += 1

        return max_len

class Solution2:
    """
    Use binary search + sliding window
    """
    def characterReplacement(self, s: str, k: int) -> int:
        # binary search over the length of substring
        # lo contains the valid value, and hi contains the
        # invalid value
        lo = 1
        hi = len(s) + 1
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2

            # can we make a valid substring of length `mid`?
            if self.__can_make_valid_substring(s, mid, k):
                # explore the right half
                lo = mid
            else:
                # explore the left half
                hi = mid

        # length of the longest substring that satisfies
        # the given condition
        return lo

    def __can_make_valid_substring(self, s: str, substring_length: int, k: int):
        # take a window of length `substring_length` on the given
        # string, and move it from left to right. If this window
        # satisfies the condition of a valid string, then we return
        # true
        freq_map: Dict[str, int] = {}
        max_frequency = 0
        start = 0
        for end in range(len(s)):
            freq_map[s[end]] = freq_map.get(s[end], 0) + 1

            # if the window [start, end] exceeds substring_length
            # then move the start pointer one step toward right
            if end + 1 - start > substring_length:
                # before moving the pointer toward right, decrease
                # the frequency of the corresponding character
                freq_map[s[start]] -= 1
                start += 1

            # record the maximum frequency seen so far
            # Since we move end, the max frequency can only be the existing one or the one just added by end pointer
            max_frequency = max(max_frequency, freq_map[s[end]])
            if substring_length - max_frequency <= k:
                return True

        # we didn't a valid substring of the given size
        return False

class Solution3:
    """
    Sliding window:
    Do we really need to check all max_len for all unique characters.

    Given a substring, how do we check if it can be a valid string with at most k replacements?
    The character that should be replaced to should be the one with most frequencies:
        - example: A [BDEEF] A
            If we check this substring: BDEEF with at most k replacement, we should replace all chars with E since E appears most times (2 times). If it cannot be a valid substring with replacing other chars to E, then we cannot create a valid substring
        - Then how to check if a substr is valid:
            if we have the max frequency count of the substring, then the replacement is len(substr) - max_frequency
        - How do we get the max_frequency of a substring, we can count for each one but it takes O(n) time to directly count the max_frequency. We can do it using sliding window: the max_frequency can only chang when we move end pointer. So if we remember the count for all chars in the substring, and increase/decrease count when moving end and start pointer, then we can get the max_frequency in constant time

    The algorithm is:
        keep frequency of char in the string, use 2 pointers start and end. Move end pointer until it hits a invalid substring, then move start pointer until it is valid. During the process, store the max_len.
    """
    def characterReplacement(self, s: str, k: int) -> int:
        char_frequency: defaultdict[str, int] = defaultdict(int)
        max_frequency = 0

        start = 0
        end = 0
        max_len = 0

        for end in range(len(s)):
            char_frequency[s[end]] += 1

            # Important: max frequency can only appear when moving end pointer, it is either existing one or the frequency of the s[end]
            max_frequency = max(max_frequency, char_frequency[s[end]])

            while end - start + 1 - max_frequency > k:
                char_frequency[s[start]] -= 1
                start += 1
            max_len = max(max_len, end-start+1)

        return max_len



if __name__ == "__main__":
    # Run the solution code here
    s = Solution3()
    input = "BAAAA"
    print(s.characterReplacement(input, 0))