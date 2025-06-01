import random
from collections import deque, OrderedDict
from typing import List

def quickSort(input: List[int]) -> None:
    start = 0
    end = len(input) -1

    quickSortRecursion(input, start, end)
    return

def quickSortRecursion(input: List[int], start: int, end: int) -> None:
    if start >= end:
        return
    pivotIndex = partition_Lomuto(input, start, end)
    print(f"In quick sort, start: {start}, end: {end}, pivotIndex: {pivotIndex}")
    if start < pivotIndex:
        quickSortRecursion(input, start, pivotIndex-1)
    if end > pivotIndex:
        quickSortRecursion(input, pivotIndex+1, end)
    return

# Slow partition, not good at dealing with many duplicates in input
def partition_Lomuto(nums: List[int], start: int, end: int) -> int:
    pivotIndex = random.randint(start, end)
    # print(f"Pivot index: {pivotIndex}")
    # pivotIndex = end
    pivot = nums[pivotIndex]
    print(f"Start calling: {start}, End: {end}, pivot: {pivot}, pivotIndex: {pivotIndex}")

    # Swap pivot and end
    temp = nums[end]
    nums[end] = nums[pivotIndex]
    nums[pivotIndex] = temp

    # all elements <= j are smaller than pivot
    j = start - 1
    for i in range(start, end):
        if nums[i] < pivot:
            j += 1
            (nums[i], nums[j]) = (nums[j], nums[i])
    (nums[j+1], nums[end]) = (nums[end], nums[j+1])
    return j+1

def partition(input: List[int], start: int, end: int) -> int:
    pivotIndex = random.randint(start, end)
    pivot = input[pivotIndex]

    # Has to swap random pivot with end element and swap it back
    # input[pivotIndex], input[end] = input[end], input[pivotIndex]

    i = start
    j = end
    print(f"Before partition: i: {i}, j: {j}, pivotIndex: {pivotIndex}, pivot: {pivot}")

    while i < j:
        while i <= end and input[i] <= pivot:
            i += 1
        while j >= 0 and input[j] >= pivot:
            j -= 1
        if i < j:
            input[i], input[j] = input[j], input[i]

    # input[lastIndex], input[end] = input[end], input[lastIndex]
    
    print(f"After partition: i: {i}, j: {j}, pivotIndex: {pivotIndex}, pivot: {pivot}")
    print(input)
    return j


def quickSelect(nums: List[int], left: int, right: int):            
    pivot = nums[right]
    low = left
    high = right

    while low <= high:
        while low <= high and nums[low] < pivot:
            low += 1
        while low <= high and nums[high] > pivot:
            high -= 1
        if low <= high:
            nums[low], nums[high] = nums[high], nums[low]
            low += 1
            high -= 1
    return high

if __name__ == "__main__":
    # Run the solution code here

    # Test input
    # testInput: List[int] = [2,2,2,2,1,2,2,2]
    testInput: List[int] = [2,1,2]
    # testInput: List[int] = [3,4,2,1]

    # Caller
    # partition(testInput, 0, len(testInput) -1)
    # index = quickSelect(testInput, 0, len(testInput) - 1)
    index = partition_Lomuto(testInput, 0,len(testInput)-1)
    print(f"output: {testInput}, index: {index}")