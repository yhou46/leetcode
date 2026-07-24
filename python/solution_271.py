import random
from collections import deque, OrderedDict
from typing import Dict, List, Optional, Self

"""
Description: Encode and decode strings
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

You are not allowed to solve the problem using any serialize methods (such as eval).



Example 1:

Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]
Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
Example 2:

Input: dummy_input = [""]
Output: [""]


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] contains any possible characters out of 256 valid ASCII characters.


Follow up: Could you write a generalized algorithm to work on any possible set of characters?
"""
class Codec:
    """
    We need a delimiter to separate the strings from each other, the question is what if the delimiter itself exists in the string.

    One approach:
    Use some rare char and assume it never appears in the input. Bad since no guarantess

    The correct way is to use escape characters, like "/"
    Assume we use comma: "," as delimiter. When "," appears in the string, we use "/," to indicate that it is not a delimiter but the original string.

    Also we need to escape the escape character itself: "//" means "/" appears in the original string, like "ab/c" will be decoded as "ab//c"
    """
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        result = ""
        for str in strs:
            result += f"{self._encode_single_str(str)},"
        return result


    def _encode_single_str(self, str: str) -> str:
        # Use "," as delimiter, if "," exist, use "/" to escape
        # So we have /, or // for "," and "/" in original string
        result = ""
        for char in str:
            modified_char = char
            if char == "," or char == "/":
                modified_char = f"/{char}"
            result += modified_char
        return result

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        result: List[str] = []
        current_word = ""
        while i < len(s):
            if s[i] == ",":
                result.append(current_word)
                current_word = ""
            elif s[i] == "/":
                if i >= len(s):
                    raise ValueError(f"Invalid input: {s} at pos: {i}, char: {s[i]}")
                i += 1
                if s[i] == "," or "/":
                    current_word += s[i]
                else:
                    raise ValueError(f"Invalid input: {s} at pos: {i}, char: {s[i]}")
            else:
                current_word += s[i]


            i += 1
        return result

if __name__ == "__main__":
    # Run the solution code here
    codec = Codec()
    test_input = ["Hel,,lo", "world", "/"]

    print(f"input  : {test_input}")
    encoded = codec.encode(test_input)
    print(f"encoded: {encoded}")

    decoded = codec.decode(encoded)
    print(f"decoded: {decoded}")