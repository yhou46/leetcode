import random
from collections import deque, OrderedDict
from typing import Dict, List, Optional, Self

"""
Description: Valid anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.



Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false



Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_map: Dict[str, int] = {}

        for char in s:
            if char not in char_map:
                char_map[char] = 1
            else:
                char_map[char] += 1

        for char in t:
            if char not in char_map:
                return False

            char_map[char] -= 1
            if char_map[char] == 0:
                # Need to delete entry if count is 0, since the input can be: "aaa", "a"
                # In this case, we rely on the map size to check if it is anagram
                del char_map[char]
            elif char_map[char] < 0:
                return False

        # Necessary for scenarios like "aaa", "a"
        return len(char_map) == 0

if __name__ == "__main__":
    # Run the solution code here
    pass