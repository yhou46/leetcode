from typing import List, Dict
"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]



Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map: Dict[str, List[str]] = {}

        for single_str in strs:
            hash = self.hash(single_str)
            if map.get(hash) == None:
                map[hash] = [ single_str ]
            else:
                map[hash].append(single_str)
        return list(map.values())

    def hash(self, str: str) -> str:
        l = list(str)

        # sort string as the hash values
        l.sort()
        return "".join(l)

if __name__ == "__main__":
    # Run the solution code here
    input = ["eat","tea","tan","ate","nat","bat"]
    s = Solution()
    print(s.groupAnagrams(input))