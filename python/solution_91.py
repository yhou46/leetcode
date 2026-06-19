import random
from collections import deque, OrderedDict
from typing import List

class Solution:
    """
    Take "123" as example
    Naive thinking:
    Take 123 as example, to decode, we can start from first char, 1 and 12 can be decoded, so we have "1" + "23" or "12" + "3". The original problem is reduced to decode "23" or "3". And we could do duplicate calculation since there are different paths that can reach to the same calculation: for example, "11234" = "1" + "1" + "2" + "34" or "11" + "2" + "34". We calculate "34" twice, so we can remember the previous result.

    DP solution:
    dp[i]: the number of decode ways from i to end, inclusive, i from 0 to len(str)-1
    we need dp[0]

    dp[i] = if s[i] is 0, then 0
            if s[i] is 1 and s[i+1] in [0-9], or 2 and s[i+1] in [0-6] then s[i+1] + s[i+2]
            else: s[i+1]
    dp[end] (dummy) = 1
    dp[end-1] = 0 or 1
    """
    def numDecodings(self, s: str) -> int:
        dp: List[int] = [0 for _ in range(len(s)+1)]
        dp[len(s)] = 1
        dp[len(s)-1] = 0 if s[-1] == "0" else 1

        zeroToSix = {"0", "1", "2", "3", "4", "5", "6"}

        for i in reversed(range(len(s)-1)):
            if s[i] == "0":
                dp[i] = 0
            elif s[i] == "1":
                dp[i] = dp[i+1] + dp[i+2]
            elif s[i] == "2":
                if s[i+1] in zeroToSix:
                    dp[i] = dp[i+1] + dp[i+2]
                else:
                    dp[i] = dp[i+1]
            else:
                dp[i] = dp[i+1]
        return dp[0]

if __name__ == "__main__":
    # Run the solution code here
    input = "102"

    s = Solution()
    print(s.numDecodings(input))