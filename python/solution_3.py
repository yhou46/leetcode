"""
Description: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Given a string s, find the length of the longest substring without duplicate characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left: int = 0
        right: int = 0
        max_length = 0

        while left < len(s) and right < len(s):
            # print(f"left:{left}, right: {right}, max_length: {max_length}, set: {char_set}")
            if s[right] not in char_set:
                char_set.add(s[right])
                right += 1
            else:
                max_length = max(max_length, right - left)
                char_set.remove(s[left])
                left += 1
        max_length = max(max_length, right - left)
        # print(f"out while: left:{left}, right: {right}, max_length: {max_length}")
        return max_length

if __name__ == "__main__":
    # Run the solution code here
    input_str = "pwwkew"
    solution = Solution()
    print(solution.lengthOfLongestSubstring(input_str))