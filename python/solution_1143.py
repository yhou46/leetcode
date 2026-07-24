import random
from collections import deque, OrderedDict
from typing import Dict, List, Optional, Self

"""
Description: Longest common sub sequence
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.



Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.


Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
"""
class Solution:

    """
    Overview
    This is a nice problem, as unlike some interview questions, this one is a real-world problem! Finding the longest common subsequence between two strings is useful for checking the difference between two files (diffing). Git needs to do this when merging branches. It's also used in genetic analysis (combined with other algorithms) as a measure of similarity between two genetic codes.

    For that reason, the examples used in this article will be strings consisting of the letters a, c, g, and t. You might remember these letters from high school biology—they are the symbols we use to represent genetic codes. By using just four letters in examples, it is easier for us to construct interesting examples to discuss here. You don't need to know anything about genetics or biology for this though, so don't worry.

    Before we look at approaches that do work, we'll have a quick look at some that do not. This is because we're going to pretend that you've just encountered this problem in an interview, and have never seen it before, and have not been told that it is a "dynamic programming problem". After all, in this interview scenario, most people won't realize immediately that this is a dynamic programming problem. Being able to approach and explore problems with an open mind without jumping to early conclusions is essential in tackling problems you haven't seen before.

    What is a Common Subsequence?

    Here's an example of two strings that we need to find the longest common subsequence of.

    Two strings "actgattag" and "gtgtgatcg"

    A common subsequence is a sequence of letters that appears in both strings. Not every letter in the strings has to be used, but letters cannot be rearranged. In essence, a subsequence of a string s is a string we get by deleting some letters in s.

    Here are some of the common subsequences for the above example. To help show that the subsequence really is a common subsequence, we've drawn lines between the corresponding characters.

    Common subsequence "tga"
    Common subsequence "ttt"
    Common subsequence "g"
    Common subsequence "tgtg"

    Drawing lines between corresponding letters is a great way of visualizing the problem and is potentially a valuable technique to use on a whiteboard during an interview. Observe that if lines cross over each other, then they do not represent a common subsequence.

    Not a subsequence

    This is because lines that cross over are representing letters that have been rearranged.

    We will use and refer to "lines" between the words extensively throughout this article.

    Brute-force

    The most obvious approach would be to iterate through each subsequence of the first string and check whether or not it is also a subsequence of the second string.

    This, however, will require exponential time to run. The number of subsequences in a string is up to 2
    L
    , where L is the length of the string. This is because, for each character, we have two choices; it can either be in the subsequence or not in it. Duplicate characters reduce the number of unique subsequences a bit, although in the general case, it's still exponential.

    This would be a brute-force approach.

    Greedy

    By this point, it's hopefully clear that we're dealing with an optimization problem. We need to generate a common subsequence that has the maximum possible number of letters. Using our analogy of drawing lines between the words, we could also phrase it as maximizing the number of non-crossing lines.

    There are a couple of strategies we use to design a tractable (non-exponential) algorithm for an optimization problem.

    Identifying a greedy algorithm
    Dynamic programming
    There is no guarantee that either is possible. Additionally, greedy algorithms are strictly less common than dynamic programming algorithms and are often more difficult to identify. However, if a greedy algorithm exists, then it will almost always be better than a dynamic programming one. You should, therefore, at least give some thought to the potential existence of a greedy algorithm before jumping straight into dynamic programming.

    The best way of doing this is by drawing an example and playing around with it. One idea could be to iterate through the letters in the first word, checking whether or not it is possible to draw a line from it to the second word (without crossing lines). If it is, then draw the left-most line possible.

    For example, here's what we would do with the first letter of our example from earlier.

    Connecting 'a' in top to 'a' in bottom

    And then, the second letter.

    Connecting 'c' in top to 'c' in bottom

    And finally, the third letter.

    Connecting 'g' in top to 'g' in bottom

    This solution, however, isn't optimal. Here is a better solution.

    A better solution "tgag"

    What if we were to do the same, but instead going from the second word to the first word? Perhaps one way or the other will always be optimal?

    A greedy solution with second string

    Unfortunately, this hasn't worked either. This solution is still worse than a better one we know about.

    Perhaps, instead, we could draw all possible lines. Could there be a way of eliminating some of the lines that cross over?

    Image showing all lines between same characters

    Uhoh, we now have what looks like an even more complicated problem than the one we began with. With some lines crossing over many other lines, where would you even begin?

    Applying Dynamic Programming to a Problem

    While it's very difficult to be certain that there is no greedy algorithm for your interview problem, over time you'll build up an intuition about when to give up. You also don't want to risk spending so long trying to find a greedy algorithm that you run out of time to write a dynamic programming one (and it's also best to make sure you write a working solution!).

    Besides, sometimes the process used to develop a dynamic programming solution can lead to a greedy one. So, you might end up being able to further optimize your dynamic programming solution anyway.

    Recall that there are two different techniques we can use to implement a dynamic programming solution; memoization and tabulation.

    Memoization is where we add caching to a function (that has no side effects). In dynamic programming, it is typically used on recursive functions for a top-down solution that starts with the initial problem and then recursively calls itself to solve smaller problems.
    Tabulation uses a table to keep track of subproblem results and works in a bottom-up manner: solving the smallest subproblems before the large ones, in an iterative manner. Often, people use the words "tabulation" and "dynamic programming" interchangeably.
    For most people, it's easiest to start by coming up with a recursive brute-force solution and then adding memoization to it. After that, they then figure out how to convert it into an (often more desired) bottom-up tabulated algorithm.


    Approach 1: Memoization
    Intuition

    The first step is to find a way to recursively break the original problem down into subproblems. We want to find subproblems such that we can create an optimal solution from the results of those subproblems.

    Earlier, we were drawing lines between identical letters.

    Greedy example of 'acg' solution

    Consider the greedy algorithm we tried earlier where we took the first possible line. Instead of assuming that the line is part of the optimal solution, we could consider both cases: the line is part of the optimal solution or the line is not part of the optimal solution.

    If the line is part of the optimal solution, then we know that the rest of the lines must be in the substrings that follow the line. As such, we should find the solution for the substrings, and add 1 onto the result (for the new line) to get the optimal solution.

    Image showing subproblem LCS("ctgattag", "tcg")

    However, if the line is not part of the optimal solution, then we know that the letter in the first string is not included (as this would have been the best possible line for that letter). So, instead, we remove the first letter of the first string and treat the remainder as the subproblem. Its solution will be the optimal solution.

    Image showing subproblem LCS("ctgattag", "gtgtgatcg")

    But remember, we don't know which of these two cases is true. As such, we need to compute the answer for both cases. The highest one will be the optimal solution and should be returned as the answer for this problem.

    Note that if either the first string or the second string is of length 0, we don't need to break it into subproblems and can just return 0. This acts as the base case for the recursion.

    But how many total subproblems will we need to solve? Well, because we always take a character off one, or both, of the strings each time, there are M⋅N possible subproblems (where M is the length of the first string, and N the length of the second string). Another way of seeing this is that subproblems are represented as suffixes of the original strings. A string of length K has K unique suffixes. Therefore, the first string has M suffixes, and the second string has N suffixes. There are, therefore, M⋅N possible pairs of suffixes.

    Some subproblems may be visited multiple times, for example LCS("aac", "adf") has the two subproblems LCS("ac", "df") and LCS("ac", "adf"). Both of these share a common subproblem of LCS("c", "df"). As such, as we should memoize the results of LCS calls so that the answers of previously computed subproblems can immediately be returned without the need for re-computation.

    Algorithm

    From what we've explored in the intuition section, we can create a top-down recursive algorithm that looks like this in pseudocode:

    define function LCS(text1, text2):
        # If either string is empty there, can be no common subsequence.
        if length of text1 or text2 is 0:
            return 0

        letter1 = the first letter in text1
        firstOccurence = first position of letter1 in text2

        # The case where the line *is not* part of the optimal solution
        case1 = LCS(text1.substring(1), text2)

        # The case where the line *is* part of the optimal solution
        case2 = 1 + LCS(text1.substring(1), text2.substring(firstOccurence + 1))

        return maximum of case1 and case2
    You might notice from the pseudocode that there's one case we haven't handled: if letter1 isn't part of text2, then we can't solve the first subproblem. However, in this case, we can simply ignore the first subproblem as the line doesn't exist. This leaves us with:

    define function LCS(text1, text2):
        # If either string is empty there can be no common subsequence
        if length of text1 or text2 is 0:
            return 0

        letter1 = the first letter in text1

        # The case where the line *is not* part of the optimal solution
        case1 = LCS(text1.substring(1), text2)

        case2 = 0
        if letter1 is in text2:
            firstOccurence = first position of letter1 in text2
            # The case where the line *is* part of the optimal solution
            case2 = 1 + LCS(text1.substring(1), text2.substring(firstOccurence + 1))

        return maximum of case1 and case2
    Remember, we need to make sure that the results of this method are memoized. In Python, we can use lru_cache. In Java, we need to make our own data structure. A 2D Array is the best option (see the code for the details of how this works).


    Complexity Analysis

    Time complexity : O(M⋅N
    2
    ).

    We analyze a memoized-recursive function by looking at how many unique subproblems it will solve, and then what the cost of solving each subproblem is.

    The input parameters to the recursive function are a pair of integers; representing a position in each string. There are M possible positions for the first string, and N for the second string. Therefore, this gives us M⋅N possible pairs of integers, and is the number of subproblems to be solved.

    Solving each subproblem requires, in the worst case, an O(N) operation; searching for a character in a string of length N. This gives us a total of (M⋅N
    2
    ).

    Space complexity : O(M⋅N).

    We need to store the answer for each of the M⋅N subproblems. Each subproblem takes O(1) space to store. This gives us a total of O(M⋅N).

    It is important to note that the time complexity given here is an upper bound. In practice, many of the subproblems are unreachable, and therefore not solved.

    For example, if the first letter of the first string is not in the second string, then only one subproblem that has the entire first word is even considered (as opposed to the N possible subproblems that have it). This is because when we search for the letter, we skip indices until we find the letter, skipping over a subproblem at each iteration. In the case of the letter not being present, no further subproblems are even solved with that particular first string.


    Approach 2: Improved Memoization
    Intuition

    There is an alternative way of expressing the solution recursively. The code is simpler, and will also translate a lot more easily into a bottom-up dynamic programming approach.

    The subproblems are of the same structure as before; represented as two indexes. Also, like before, we're going to be considering multiple possible decisions and then going with the one that has the highest answer. The difference is that the way we break a problem into subproblems is a bit different. For example, here is how our example from before breaks into subproblems.

    Graph of subproblems showing only links between ones with first character differing

    If the first character of each string is not the same, then either one or both of those characters will not be used in the final result (i.e. not have a line drawn to or from it). Therefore, the length of the longest common subsequence is max(LCS(p1 + 1, p2), LCS(p1, p2 + 1)).

    Now, what about subproblems such as LCS("tgattag", "tgtgatcg")? The first letter of each string is the same, and so we could draw a line between them. Should we? Well, there is no reason not to draw a line between the first characters when they're the same. This is because it won't block any later (optimal) decisions. No letters other than those used for the line are removed from consideration by it. Therefore, we don't need to make a decision in this case.

    When the first character of each string is the same, the length of the longest common subsequence is 1 + LCS(p1 + 1, p2 + 1). In other words, we draw a line a line between the first two characters, adding 1 to the length to represent that line, and then solving the resulting subproblem (that has the first character removed from each string).

    Here is a few more of the subproblems for the above example.

    Graph of subproblems showing links between all nodes

    Like before, we still have overlapping subproblems, i.e. subproblems that appear on more than one branch. Therefore, we should still be using a memoization table, just like before.

    Algorithm


    Complexity Analysis

    Time complexity : O(M⋅N).

    This time, solving each subproblem has a cost of O(1). Again, there are M⋅N subproblems, and so we get a total time complexity of O(M⋅N).

    Space complexity : O(M⋅N).

    We need to store the answer for each of the M⋅N subproblems.


    Approach 3: Dynamic Programming
    Intuition

    In many programming languages, iteration is faster than recursion. Therefore, we often want to convert a top-down memoization approach into a bottom-up dynamic programming one (some people go directly to bottom-up, but most people find it easier to come up with a recursive top-down approach first and then convert it; either way is fine).

    Observe that the subproblems have a natural "size" ordering; the largest subproblem is the one we start with, and the smallest subproblems are the ones with just one letter left in each word. The answer for each subproblem depends on the answers to some of the smaller subproblems.

    Remembering too that each subproblem is represented as a pair of indexes, and that there are text1.length() * text2.length() such possible subproblems, we can iterate through the subproblems, starting from the smallest ones, and storing the answer for each. When we get to the larger subproblems, the smaller ones that they depend on will already have been solved. The best way to do this is to use a 2D array.

    Empty grid for bottom up approach

    Each cell represents one subproblem. For example, the below cell represents the subproblem lcs("attag", "gtgatcg").

    Cell highlighted for subproblem

    Remembering back to Approach 2, there were two cases.

    The first letter of each string is the same.
    The first letter of each string is different.
    For the first case, we solve the subproblem that removes the first letter from each, and add 1. In the grid, this subproblem is always the diagonal immediately down and right.

    Cell where first letter is same, showing +1 into new cell

    For the second case, we consider the subproblem that removes the first letter off the first word, and then the subproblem that removes the first letter off the second word. In the grid, these are subproblems immediately right and below.

    Cell where first letter is same, showing +1 into new cell

    Putting this all together, we iterate over each column in reverse, starting from the last column (we could also do rows, the final result will be the same). For a cell (row, col), we look at whether or not text1.charAt(row) == text2.charAt(col) is true. if it is, then we set grid[row][col] = 1 + grid[row + 1][col + 1]. Otherwise, we set grid[row][col] = max(grid[row + 1][col], grid[row][col + 1]).

    For ease of implementation, we add an extra row of zeroes at the bottom, and an extra column of zeroes to the right.
    """

    """

    Important: how to define the meaning of dp table
    dp[i][j] is the max length of sub seq of text1[0:i] and text2[0:j], both inclusive

    dp[i][j] is:

        if text1[i] == text[j], then we can pick char i and j since they are at the end and it is no harm to pick i and j as last element in the sub seq, dp[i][j] = 1 + dp[i-1][j-1]

        if text1[i] != text[j], then then char at i and j cannot be both appear in the longest sub seq. Only one of them or none of them can be in the longest sub seq.
        so dp[i][j] is max of dp[i-1][j], dp[i][j-1], dp[i-1][j-1]

        Since dp[i][j] dependes on up and left cells, we need base case: dp[0][j] and dp[i][0]

        dp[0][j] means longest sub seq of first char in text1 and text2[0:j] and apparently it can be solved by checking if text1[0] is in text2[0:j], if so, it is 1, otherwise 0, both inclusive

        similaryly, dp[i][0] is 1 if text2[0] in text1[0:i], otherwise 0

    final result we need is dp[len(text1)-1][len(text2)-1]
    """
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        if len(text1) == 0 or len(text2) == 0:
            return 0

        dp: List[List[int]] = [ [ 0 for _ in range(len(text2)) ] for _ in range(len(text1)) ]

        # Calculate the base case
        for i in range(len(text1)):
            char = text2[0]
            dp[i][0] = 1 if char in text1[0:i+1] else 0

        for j in range(len(text2)):
            char = text1[0]
            dp[0][j] = 1 if char in text2[0:j+1] else 0

        # Calculate the table
        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]

if __name__ == "__main__":
    # Run the solution code here
    pass