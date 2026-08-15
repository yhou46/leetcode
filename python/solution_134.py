import random
from collections import deque, defaultdict, OrderedDict
from typing import Dict, List, Optional, Self, Tuple

"""
Description: Gas station
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.



Example 1:

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
Example 2:

Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.


Constraints:

n == gas.length == cost.length
1 <= n <= 105
0 <= gas[i], cost[i] <= 104
The input is generated such that the answer is unique.
"""
class Solution:
    """
    For index i, it can get gas[i] cost cost[i], which means the gas change is gas[i] - cost[i]

    A brute force solution is to for each index as starting point, we calculate whether it can reach the end by accumulating gas changes and if at one time, gas is negative, it means we cannot reach the end.

    Time: O(n^2)

    How to make it faster?
    If we start from index i and gas becomes negative at index j, then index i cannot be the start point, can index between [i,j] become starting point?

    Important: the answer is no, why? Because gas level between i, i+1, ... j-1 is must be zero or positive (otherwise we stop early). And if we start from the index k, k is like [i, i+1, k, ... j-1] then, we do not get gas change from i to k-1 and the gas level at index k can only be smaller than starting from i. And starting from i failed at j, so starting from k cannot be a valid solution.

    Based on this idea, we can start from 0, keep accumulate the gas gain and if we find at index j, the gas level is below zero, we know that starting point cannot be from 0 to j, in this case, we start from j+1.

    We also need to keep a total_gas. Why?
    Because even if we do not find any index after j has negative value, the gas change before j can be a problem. That is the gas change before j is cut into several chunks and each chunk has the property that we only fail at the chunk's last element. So the gas gain after index j should have values that large enough to offset the negative gain of all chunks. We do not need to worry about whether we can travel within the chunks because it only fails at the last element.

    Example:
    | .... | ... | .. | j... |
      A       B   C
    We find after j, all gains are zero or positive. And we fail the check previously and separate the array into A, B and C. It means we can travel from start of A and only fail at end of A, with initial gas of zero. Same for B and C. So as long as we have enough gas at the end of j th chunk, we can travel from j -> end -> A -> B -> C. And this check is actually checking whether total gas change is non negative

    """
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gain = 0
        gain = 0
        start = 0

        for i in range(len(gas)):
            total_gain += gas[i] - cost[i]
            gain += gas[i] - cost[i]
            if gain < 0:
                start = i+1
                gain = 0
        if total_gain  < 0:
            return -1
        return start

if __name__ == "__main__":
    # Run the solution code here
    gas: List[int] =  [5,5, 5, 2,1]
    cost: List[int] = [6,1,10, 1,1]
    s = Solution()
    print(s.canCompleteCircuit(gas, cost))