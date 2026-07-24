import random
from collections import deque, OrderedDict
from typing import List, Optional

"""
Description: Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        new_list: List[str] = []

        for char in s:
            if char.isalnum():
                new_list.append(char)

        begin, end = 0, len(new_list)-1
        while begin < end:
            if new_list[begin] != new_list[end]:
                return False
            begin += 1
            end -= 1
        return True



if __name__ == "__main__":
    # Run the solution code here
    pass