"""
DAA Lab - Divide and Conquer
Problem 11: Median of Two Sorted Arrays (LeetCode #4)

Divide & Conquer idea (binary search on the partition):
  - Always binary search on the smaller array (A), so the search is O(log(min(m, n))).
  - Pick a cut i in A and the matching cut j in B so that the left half holds
    (m + n + 1) // 2 elements in total.
  - The partition is correct when
        A[i-1] <= B[j]   and   B[j-1] <= A[i]
    - If A[i-1] > B[j], too many elements taken from A -> move cut left.
    - Else if B[j-1] > A[i], too few taken from A       -> move cut right.
  - Median comes from the borders of the two halves.

Time: O(log(min(m, n)))   Space: O(1)
"""
from typing import List


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    A, B = nums1, nums2
    if len(A) > len(B):
        A, B = B, A                       # make A the smaller array

    m, n = len(A), len(B)
    half = (m + n + 1) // 2
    lo, hi = 0, m

    while lo <= hi:
        i = (lo + hi) // 2                # elements taken from A
        j = half - i                      # elements taken from B

        a_left = A[i - 1] if i > 0 else float("-inf")
        a_right = A[i] if i < m else float("inf")
        b_left = B[j - 1] if j > 0 else float("-inf")
        b_right = B[j] if j < n else float("inf")

        if a_left <= b_right and b_left <= a_right:     # correct partition
            if (m + n) % 2 == 1:
                return float(max(a_left, b_left))
            return (max(a_left, b_left) + min(a_right, b_right)) / 2
        elif a_left > b_right:
            hi = i - 1
        else:
            lo = i + 1

    raise ValueError("Input arrays are not sorted")


if __name__ == "__main__":
    print(find_median_sorted_arrays([1, 3], [2]))         # 2.0
    print(find_median_sorted_arrays([1, 2], [3, 4]))      # 2.5
    print(find_median_sorted_arrays([], [1]))             # 1.0
    print(find_median_sorted_arrays([0, 0], [0, 0]))      # 0.0
