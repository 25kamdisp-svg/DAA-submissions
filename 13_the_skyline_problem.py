"""
DAA Lab - Divide and Conquer
Problem 13: The Skyline Problem (LeetCode #218)

Divide & Conquer idea (like merge sort):
  - Divide: split the buildings into two halves.
  - Conquer: compute the skyline of each half recursively.
        A single building [l, r, h] has skyline [[l, h], [r, 0]].
  - Combine: merge two skylines with two pointers. At every x-coordinate the
    height is max(current left height, current right height). Add a key point
    only when the height changes.

Time: O(n log n)   Space: O(n)
"""
from typing import List


def get_skyline(buildings: List[List[int]]) -> List[List[int]]:
    if not buildings:
        return []
    return _skyline(buildings, 0, len(buildings) - 1)


def _skyline(buildings: List[List[int]], lo: int, hi: int) -> List[List[int]]:
    if lo == hi:
        l, r, h = buildings[lo]
        return [[l, h], [r, 0]]

    mid = (lo + hi) // 2
    left = _skyline(buildings, lo, mid)
    right = _skyline(buildings, mid + 1, hi)
    return _merge(left, right)


def _merge(left: List[List[int]], right: List[List[int]]) -> List[List[int]]:
    result = []
    i = j = 0
    h1 = h2 = 0                      # current heights of the two skylines

    def add(x: int, h: int) -> None:
        if not result or result[-1][1] != h:     # only record height changes
            result.append([x, h])

    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            x, h1 = left[i]
            i += 1
        elif left[i][0] > right[j][0]:
            x, h2 = right[j]
            j += 1
        else:                                    # same x in both skylines
            x, h1 = left[i]
            h2 = right[j][1]
            i += 1
            j += 1
        add(x, max(h1, h2))

    while i < len(left):
        add(left[i][0], left[i][1])
        i += 1
    while j < len(right):
        add(right[j][0], right[j][1])
        j += 1

    return result


if __name__ == "__main__":
    print(get_skyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
    # [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
    print(get_skyline([[0, 2, 3], [2, 5, 3]]))
    # [[0, 3], [5, 0]]
