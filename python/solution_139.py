import random
from collections import deque, OrderedDict
from typing import List, Optional

"""
Description: Word break
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false


Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""
class Solution:
    """
    Naive solution:
    From start of input string, we proceed one by one, checking from 0 to i and see if the substring exists in the dict.
    If it exists, we recursion call the process on the s[i+1:] to see if the rest of string can be segmented.

    Issue: we duplicate some calucations: example, if 0-2, 3-5 and 0-5 are in the dictionary. When we check 0-2, we call recursion starting from 3 and since 3-5 is a hit, we call recursion starting from 5.
    But later we will find 0-5 is a hit and start recursion from 5 again. We should remember the result.

    So it can be solved by recursion with memorization. So I think a DP solution should also work.

    Let's assume dp[i] means from 0 to i (both inclusive) the string can be segmented
    then dp[i] is true only if:
        - 0-i as a whole word in the dictionary
        - there is some index j, 0 <=j < i, that dp[j] is true and string from j+1,i is in the dictionary
    Otherwise dp[i] is false

    To check dp[j], do we need to store a entire table from 0 to i-1, we only care about the True case, let's just remember the case where dp[j] is true. Let's use a set to do that since the hit case is rarely small comparing to the large input string

    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # Stores whether from 0 to i can be segamented
        # If it has element 2, it means s[0:2] can be segamented
        dp_true: set[int] = set()

        # here i means [0,i] (both inclusive) can be segmented
        for i in range(0, len(s)):
            # python substring's right end is exclusive so use i+1
            # First check if the entire substring from 0 to i can be found in the dictionary
            if s[0:i+1] in wordDict:
                dp_true.add(i)
            else:
                # We need the flag here since we cannot edit Set member during the iteration
                found_previous = False
                # If not check all previous True value and see if the rest of string from j+1 to i can be found from the dictionary
                for j in dp_true:
                    if s[j+1 : i+1] in wordDict:
                        found_previous = True
                        break
                if found_previous:
                    dp_true.add(i)

        # if the last index is in the set, it means the entire string can be segmented.
        return len(s)-1 in dp_true

if __name__ == "__main__":
    # Run the solution code here
    pass