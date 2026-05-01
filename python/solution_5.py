from typing import List

class Solution:

    """
    s[i][j] is Palindrome if s[i] == s[j] and s[i+1][j-1] is Palindrome
    s[i][j] where i==j is Palindrome
    To compute s[i][j] we need s[i+1][j-1] and it is a dynamic programming problem

    Time: O(n^2)
    Space: O(n^2)
    """
    def longestPalindrome(self, s: str) -> str:
        is_pal_matrix: List[List[bool]] = [[False for _ in range(len(s))] for _ in range(len(s))]
        result = ""

        for i in range(0, len(s)):
            is_pal_matrix[i][i] = True

        for j in range(0, len(s)):
            for i in range(0, len(s)):
                if i == j:
                    is_pal_matrix[i][j] = True
                elif i > j:
                    break
                elif j - i == 1 and s[i] == s[j]:
                    is_pal_matrix[i][j] = True
                elif s[i] == s[j] and is_pal_matrix[i+1][j-1]:
                    is_pal_matrix[i][j] = True
                if is_pal_matrix[i][j]:
                    # print(f"i: {i}, j: {j}")
                    result = s[i:j+1] if len(s[i:j+1]) > len(result) else result
        return result

if __name__ == "__main__":
    # Run the solution code here
    input_str = "a"
    solution = Solution()
    print(solution.longestPalindrome(input_str))

