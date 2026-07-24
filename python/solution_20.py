"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false



Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        char_queue: deque[str] = deque[str]()

        for i in range(len(s)):
            char = s[i]
            if char == "(" or char == "[" or char == "{":
                char_queue.append(char)
            elif len(char_queue) == 0:
                return False
            else:
                last_element = char_queue.pop()
                if char == ")" and last_element != "(" or char == "]" and last_element != "[" or char == "}" and last_element != "{":
                    return False
        if len(char_queue) == 0:
            return True
        else:
            return False