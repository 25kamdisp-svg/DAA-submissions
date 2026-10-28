"""
DAA Lab - Greedy Algorithm
Problem 3: Largest Number (LeetCode #179)

Greedy idea:
  - Number a should come before b if the string a+b > b+a.
  - Sort with this custom comparator and join.
  - If the biggest element is "0", the answer is "0".

Time: O(n log n * L)  (L = max digits)   Space: O(n)
"""
from functools import cmp_to_key
from typing import List


def largest_number(nums: List[int]) -> str:
    strs = [str(x) for x in nums]

    def compare(a: str, b: str) -> int:
        if a + b > b + a:
            return -1     # a should come first
        if a + b < b + a:
            return 1
        return 0

    strs.sort(key=cmp_to_key(compare))

    if strs[0] == "0":    # all numbers were zeros
        return "0"
    return "".join(strs)


if __name__ == "__main__":
    print(largest_number([10, 2]))             # 210
    print(largest_number([3, 30, 34, 5, 9]))   # 9534330
    print(largest_number([0, 0]))              # 0
