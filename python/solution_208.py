import random
from collections import OrderedDict
from typing import List, Dict, Optional, Self

"""
Description: Implement Trie
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.


Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True


Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.
"""
class TrieNode:
    def __init__(self):
        self.letters: Dict[str, Self] = {}
        self.is_end_of_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        current: TrieNode = self.root
        for char in word.lower():
            if char not in current.letters:
                current.letters[char] = TrieNode()
            current = current.letters[char]
        current.is_end_of_word = True

    """
    Delete is not required by the problem but added to make the Trie implementation complete
    """
    def delete(self, word: str) -> None:
        word = word.lower()

        path: List[TrieNode] = [self.root]
        current = self.root
        for char in word:
            if char not in current.letters:
                # Not found
                return
            current = current.letters[char]
            path.append(current)

        if not current.is_end_of_word:
            # Word not present as a complete word (only a prefix)
            return

        current.is_end_of_word = False

        # Walk back up, unlinking nodes that are now dead ends
        for i in range(len(path) - 2, -1, -1):
            parent = path[i]
            child = path[i + 1]
            if len(child.letters) == 0 and not child.is_end_of_word:
                del parent.letters[word[i]]
            else:
                break


    def search(self, word: str) -> bool:
        node = self._search_prefix_node(word)

        if node != None and node.is_end_of_word:
            return True
        else:
            return False


    def startsWith(self, prefix: str) -> bool:
        node = self._search_prefix_node(prefix)
        return node != None

    def _search_prefix_node(self, prefix: str) -> TrieNode | None:
        current = self.root
        for char in prefix:
            if char in current.letters:
                current = current.letters[char]
            else:
                return None
        return current


if __name__ == "__main__":
    # Run the solution code here
    trie = Trie()

    trie.insert("apple")
    print("search apple ->", trie.search("apple"))       # True
    print("search app ->", trie.search("app"))           # False
    print("startsWith app ->", trie.startsWith("app"))   # True

    trie.insert("app")
    print("search app ->", trie.search("app"))           # True

    trie.delete("apple")
    print("after delete apple:")
    print("search apple ->", trie.search("apple"))       # False
    print("search app ->", trie.search("app"))           # True (still present)
    print("startsWith app ->", trie.startsWith("app"))   # True

    trie.delete("app")
    print("after delete app:")
    print("search app ->", trie.search("app"))           # False
    print("startsWith app ->", trie.startsWith("app"))   # False (nodes pruned)
    print(f"Trie size: {trie.root.letters}")

    trie.delete("nonexistent")                           # no-op, should not raise
    print("search nonexistent ->", trie.search("nonexistent"))  # False
