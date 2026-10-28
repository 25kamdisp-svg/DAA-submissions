"""
DAA Lab - Backtracking
Problem 18: Word Break II (LeetCode #140)

Backtracking idea:
  - At index `start`, try every prefix s[start:end] that is in the dictionary.
  - Choose it (append to path), recurse on `end`, then un-choose (pop).
  - When start reaches len(s), join the path into a sentence.
  - Pruning: precompute can_break[i] = True if s[i:] can be split at all.
    If not, do not explore that branch (avoids exponential dead ends).

Time: O(n^2 + output size) with pruning, worst case exponential in output
Space: O(n)
"""
from typing import List


def word_break(s: str, word_dict: List[str]) -> List[str]:
    words = set(word_dict)
    n = len(s)

    # can_break[i] -> can s[i:] be segmented?
    can_break = [False] * (n + 1)
    can_break[n] = True
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n + 1):
            if s[i:j] in words and can_break[j]:
                can_break[i] = True
                break

    result = []
    path = []

    def backtrack(start: int) -> None:
        if start == n:
            result.append(" ".join(path))
            return

        for end in range(start + 1, n + 1):
            piece = s[start:end]
            if piece in words and can_break[end]:    # prune dead branches
                path.append(piece)                   # choose
                backtrack(end)                       # explore
                path.pop()                           # un-choose

    if can_break[0]:
        backtrack(0)
    return result


if __name__ == "__main__":
    print(word_break("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
    # ['cat sand dog', 'cats and dog']
    print(word_break("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))
    # ['pine apple pen apple', 'pine applepen apple', 'pineapple pen apple']
    print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    # []
