# leetcode solutions
Implementation of leetcode and other interviewing problems

## Tips and tricks:
https://leetcode.cn/discuss/post/3583665/fen-xiang-gun-ti-dan-chang-yong-shu-ju-j-bvmv/

- Subsequence problem: it is likely can be solved by DP (Dynamic Programming)
    - sub sequence of a string is that you can remove any number of chars and keep the rest of chars with order unchanged. "ac" is subsequence of "abcd"

- Substring problem: it requries the char to be consequtive so it is likely can be solved by 2 pointers: left and right and move pointers based on conditions.

- Palindrome problem: think of the middle point, a palindrome has a middle point and you can start from the middle point. Be careful that the middle point depends on the odd or even length of the string
    - Palindrome is a string that read the same from left to right and from right to left: like "abba"

## Check basic algorithms
1. Sorting
- Quick sort and partition

- Quick select

- Heap sort

2. Binary search

3. Graph: BFS and DFS

4. Dynamic programming

5. Recursion (with cache)