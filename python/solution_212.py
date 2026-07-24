import random
from collections import deque, OrderedDict
from typing import Dict, List, Optional, Self

"""
Description: Word Search 2
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.



Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""

class TrieNode:
    def __init__(self):
        self.letters: Dict[str, Self] = {}
        self.is_word_end = False
        self.data = ""

class Solution:
    """
    Naive solution:
    For each input word, scan the board and do DFS to see if we can find a match.

    Issue: we have some duplicated caculation here:
    Example: apple, app, application all shares the same prefix: app
    poison, son shares the same suffixes

    My initial idea is to cache the suffix at each board position. Example:
    x, y has been scanned with "son" and found the match

    But it has issues: if a new word has reused the same position, then the cached result should not be used. The cached result does not tell the path, and to avoid path collision, we probably need to cache the path too (like list of points), which seems complex.

    What about cache prefix? A structure that prevent scan "app" again when processing "application"
    A Trie is a good candidate. Instead of caching search result for each point in the board, we preprocess the input to build a Trie.

    And the flows is to do DFS on the Trie with the board
    """
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = self._build_trie(words)

        result: set[str] = set()

        m = len(board)
        if m == 0:
            raise ValueError(f"Empty board")
        n = len(board[0])

        for i in range(0, m):
            for j in range(0, n):
                self._dfs(
                    i,
                    j,
                    board,
                    root,
                    result
                )
                if len(result) >= len(words):
                    break
        return list(result)


    def _dfs(
            self,
            x: int,
            y: int,
            board: List[List[str]],
            node: TrieNode,
            result: set[str],
            ) -> None:

        char = board[x][y]

        m = len(board)
        if m == 0:
            raise ValueError(f"Empty board")
        n = len(board[0])

        if char in node.letters:

            next_node = node.letters[char]

            # Add result here instead of at the beginning of the function
            # because if we add it there, it relies on whether the dfs can proceed to next point. Sometimes it cannot proceed while there is a match. Example: board is 1 * 1 with letter "a" and words is ["a"]
            if next_node.is_word_end:
                print(f"x: {x}, y: {y}, Trie: {next_node.letters}, word: {next_node.data}")
                result.add(next_node.data)

            direction_x = [-1, 0, 1, 0]
            direction_y = [ 0, 1, 0, -1]


            for i in range(0, len(direction_x)):
                new_x = x + direction_x[i]
                new_y = y + direction_y[i]
                board[x][y] = "#"
                if new_x >=0 and new_x < m and new_y >= 0 and new_y < n and board[new_x][new_y] != "#":
                    self._dfs(
                        new_x,
                        new_y,
                        board,
                        next_node,
                        result,
                    )
                board[x][y] = char
        return



    def _build_trie(self, words: List[str]) -> TrieNode:
        root = TrieNode()

        for word in words:
            current = root
            for char in word:
                if char not in current.letters:
                    current.letters[char] = TrieNode()
                current = current.letters[char]
            current.is_word_end = True
            current.data = word
        return root


if __name__ == "__main__":
    # Run the solution code here
    s = Solution()
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]

    # board = [["a"]]
    # words = ["a"]

    print(s.findWords(
        board,
        words,
    ))