import random
from collections import deque, OrderedDict
from typing import List, Dict, Optional, Self

"""
Description: Design add and search word
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.


Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True


Constraints:

1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 2 dots in word for search queries.
At most 104 calls will be made to addWord and search.
"""

class TrieNode:
    def __init__(self):
        self.letters: Dict[str, Self] = {}
        self.is_word_end = False

class WordDictionary:
    """
    To handle "." match, the hashmap is not sufficient.
    To avoid scanning all words to find the match, we should use a Trie here
    """
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.letters:
                current.letters[char] = TrieNode()
            current = current.letters[char]
        current.is_word_end = True

    def search(self, word: str) -> bool:
        return self._dfs_search(word, 0, self.root)

    def _dfs_search(self, word: str, pos: int, node: TrieNode) -> bool:

        # The TrieNode path is always len(word) + 1
        # When pos reaches len(word), it is supposed to be the end of the Trie
        if pos >= len(word):
            return node.is_word_end
        char = word[pos]

        if char == ".":
            found = False
            for _, next_node in node.letters.items():
                found = self._dfs_search(word, pos+1, next_node)
                if found:
                    return True
            return False
        else:
            if char in node.letters:
                return self._dfs_search(word, pos+1, node.letters[char])
            else:
                return False


if __name__ == "__main__":
    # Run the solution code here
    d = WordDictionary()
    d.addWord("apc")
    print(d.search("a.."))