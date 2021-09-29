# merge.py
# DJ

from typing import List


def merge_sort(input: List[int]):
    if len(input) > 1:
        mid = len(input)//2
        right = merge_sort(input[:mid])
        left = merge_sort(input[mid:])
    else:
        return input

    build_list = []
    merge_len = len(right) + len(left)

    for i in range(merge_len):
        if len(right) > 0 and len(left) > 0:
            if right[0] < left[0]:
                build_list.append(right.pop(0))
            else:
                build_list.append(left.pop(0))
        elif len(right) > 0:
            for num in right:
                build_list.append(num)
            break
        elif len(left) > 0:
            for num in left:
                build_list.append(num)
            break
    return build_list
