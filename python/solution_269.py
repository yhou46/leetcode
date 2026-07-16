import random
from collections import deque, OrderedDict, defaultdict
from typing import Dict, List, Optional, Self

"""
Description: Alien dictionary
There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary. Now it is claimed that the strings in words are sorted lexicographically by the rules of this new language.

If this claim is incorrect, and the given arrangement of string in words cannot correspond to any order of letters, return "".

Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there are multiple solutions, return any of them.



Example 1:

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
Example 2:

Input: words = ["z","x"]
Output: "zx"
Example 3:

Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of only lowercase English letters.
"""
class Solution:
    """
    Difficult one since it needs multi steps:
    First, a single word does not give us any information about letter ordering, only 2 words in order can potentially give us some information:
        - [ab, bc]: means a appears before b, a -> b, no other information
        - [ab, abb]: nothing we can get from this ordering since 1st string is prefix of 2nd string
        - [abb, ab]: invalid input since 2nd string should go first

    So given 2 words in order, we can at most get one information of one letter must appear before another letter. And we need the ordering of all letter appearance.

    We can think of 1 letter is a node and if letter a should appear before letter b, then we have an edge from a -> b. We try to get all possible edges from the input, then all letters forms a directed graph. The ordering of all letters means doing the topology sort of the graph
    """
    def alienOrder(self, words: List[str]) -> str:
        edges: List[List[str]] = []

        # We have to remember all unique letters, otherwise the topology sort result is wrong when any letter does not have an edge
        # Example: ["z","zx","zxa", "zab"], we only know x -> a, nothing else, in this case, we need to add z, x, b to unique letters
        unique_letters: set[str] = set()

        # Handle cases that only one word
        if len(words) == 1:
            unique_letters.update([char for char in words[0]])

        try:
            # it only handles cases where word length is larger than 1
            # So we need to handle the case when word list only has one word
            for i in range(0, len(words)-1):
                unique_letters.update([char for char in words[i]])
                unique_letters.update([char for char in words[i+1]])

                edge = self.get_letter_order(words[i], words[i+1])
                if len(edge) > 0:
                    edges.append(edge)
        except ValueError as error:
            print(f"Error encountered when getting char edges: {error}")
            return ""

        print(f"edges: {edges}")

        # Topology sort using BFS
        in_degree_map: defaultdict[str, int] = defaultdict(int)

        # Important here:
        # We need to make sure all nodes are added to in_degree map, including those dangling nodes without any edges, their in degree is zero.
        for char in unique_letters:
            in_degree_map[char] = 0

        adjacent_matrix: defaultdict[str, List[str]] = defaultdict(list)
        for edge in edges:
            u = edge[0]
            v = edge[1]
            in_degree_map[v] += 1
            adjacent_matrix[u].append(v)

        print(f"adjacent_matrix: {adjacent_matrix}")
        print(f"in_degree: {in_degree_map}")

        result = ""
        queue: deque[str] = deque([char for char in in_degree_map if in_degree_map[char] == 0])

        while len(queue) > 0:
            char = queue.popleft()
            result += char

            # Here because we initial adjacent_matrix as defaultdict
            # If char is not in the dict, it is by default has empty list: [], instead of throwing key not exist errors
            for node in adjacent_matrix[char]:
                in_degree_map[node] -= 1
                if in_degree_map[node] == 0:
                    queue.append(node)

        # Check circles
        # Important: if we do not add all unique chars, then this check is wrong
        total_unique_chars = len(adjacent_matrix)
        if len(result) < total_unique_chars:
            print(f"topology finds a circle")
            return ""
        else:
            return result

    # Assume word1 < word2
    def get_letter_order(self, word1, word2) -> List[str]:
        pos = -1

        # find 1st letter that is different
        for i in range(0, len(word1)):
            if i >= len(word2):
                # If we reach the end of word1 but still not different char found, then it is invalid: example: appa, app
                if pos == -1:
                    raise ValueError(f"Invalid sequence: {word1}, {word2}")
                break
            if word1[i] != word2[i]:
                pos = i
                break

        if pos == -1:
            # No guaranteed letter order found
            return []
        else:
            return [word1[pos], word2[pos]]

if __name__ == "__main__":
    # Run the solution code here
    s = Solution()

    input = ["z","zx","zxa", "zab"]
    input = ["wrt","wrf","er","ett","rftt"]
    input = ["wnlb"]
    print(f"result: {s.alienOrder(input)}")