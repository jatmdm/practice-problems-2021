# merge.py
# DJ

from typing import List


def partition(input: List[int], start, end):
    def swap(input: List[int], a: int, b: int):
        A = input[a]
        B = input[b]
        input[a] = B
        input[b] = A
        return input
    pivot = len(input)//2
    input = swap(input, pivot, len(input)-1)
    subarray = input[:-1]
    left = 0
    right = len(input) - 1

    while subarray[left] < input[len(input)-1]:
        if left == right:
            break
        if subarray[left] < input[len(input)-1]:
            left += 1

    while subarray[right] > input[len(input)-1]:
        if right == left:
            break
        if subarray[right] > input[len(input)-1]:
            right -= 1



def quicksort(input: List[int], start: int, end: int):
    if start > end:
        pivot_pos = partition(input, start, end)
        quicksort(input, start, pivot_pos-1)
        quicksort(input, pivot_pos+1, end)

def quicksort(input: List[int]):
    start = 0
    end = len(input) - 1
    return quicksort(input, start, end)