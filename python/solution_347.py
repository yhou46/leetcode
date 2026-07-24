import random
import heapq
from collections import deque, OrderedDict, defaultdict
from typing import Dict, List, Optional, Self, Tuple

"""
Description: TBD
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map: Dict[int, int] = defaultdict(int)

        for num in nums:
            count_map[num] += 1
        print(f"count map: {count_map.items()}")

        max_heap: List[Tuple[int, int]] = []
        for num, count in count_map.items():
            # Python heap is by default min heap, need to times -1
            max_heap.append((-1 * count, num))
        heapq.heapify(max_heap)
        print(f"heap: {max_heap}")

        result: List[int] = []
        for _ in range(k):
            # Only min value is at the top so need to pop k times
            pair = heapq.heappop(max_heap)
            result.append(pair[1])
        return result








if __name__ == "__main__":
    # Run the solution code here
    s = Solution()

    input = [1,1,1,2,2,3]
    print(s.topKFrequent(input, 2))