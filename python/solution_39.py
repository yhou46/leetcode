from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        for input [2,3,6,7] and target 7
        we can pick an element, like 2, then check [2,3,6,7] with a new target 7-2 = 5, so the original problem becomes a smaller problem. We stop until the new target is below zero since no more numbers can be checked. So a recursion can be used.

        Can we stop earlier? Yes. If we sort the array and already checked 2,3,3 and new target < 0, then we do not need to check 6 and 7 since they are all bigger than the previous number and cannot be used. So sort the original array is needed.

        Remove duplicates:
        since each number can be used multiple times, when we used 2,2,2,2 and it exceeds target 7, we should then check 2,2,2,3. When it comes to 3 as first element, we should not use 2 again since it is already covered in previous iteration. So we should only check 3,6,7.
        """

        candidates.sort()

        result: List[List[int]] = []
        self.recursion(
            candidates,
            0,
            target,
            result,
            [],
        )

        return result

    # 2,3,6,7 7
    def recursion(self,
        candidates: List[int],
        start: int,
        target: int,
        result: List[List[int]],
        temp: List[int],
        ) -> None:
        for i in range(start, len(candidates)):
            num = candidates[i]
            new_target = target - num
            temp.append(num)
            if new_target == 0:
                result.append(list(temp))
            elif new_target > 0:
                self.recursion(candidates, i, new_target, result, temp)
            temp.pop()


if __name__ == "__main__":
    # Run the solution code here
    s = Solution()
    input = [2,3,6,7]
    target = 6
    print(s.combinationSum(input, target))