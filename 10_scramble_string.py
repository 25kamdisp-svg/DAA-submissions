"""
DAA Lab - Dynamic Programming
Problem 10: Scramble String (LeetCode #87)

DP idea (top-down with memoization):
  is_scramble(a, b) is True if b can be obtained from a by recursively
  splitting into two non-empty parts and optionally swapping them.
  For every split point i:
    - No swap: scramble(a[:i], b[:i]) and scramble(a[i:], b[i:])
    - Swap:    scramble(a[:i], b[-i:]) and scramble(a[i:], b[:-i])
  Pruning: strings with different letter counts can never be scrambles.

Time: O(n^4) worst case   Space: O(n^3) for the memo
"""
from collections import Counter
from functools import lru_cache


def is_scramble(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    @lru_cache(maxsize=None)
    def check(a: str, b: str) -> bool:
        if a == b:
            return True
        if Counter(a) != Counter(b):         # prune impossible cases
            return False

        n = len(a)
        for i in range(1, n):
            # no swap
            if check(a[:i], b[:i]) and check(a[i:], b[i:]):
                return True
            # swap
            if check(a[:i], b[n - i:]) and check(a[i:], b[:n - i]):
                return True
        return False

    return check(s1, s2)


if __name__ == "__main__":
    print(is_scramble("great", "rgeat"))     # True
    print(is_scramble("abcde", "caebd"))     # False
    print(is_scramble("a", "a"))             # True
