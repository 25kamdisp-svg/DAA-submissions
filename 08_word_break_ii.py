"""
DAA Lab - Dynamic Programming
Problem 8: Word Break II (LeetCode #140)

DP idea (top-down with memoization):
  break_from(i) = all sentences that can be built from s[i:].
  For every dictionary word that matches at index i, combine it with every
  sentence returned by break_from(i + len(word)).
  Results for each index are cached so they are computed only once.

Time: O(n^2 + output size) typical, worst case exponential in output size
Space: O(n + output size)
"""
from typing import List


def word_break(s: str, word_dict: List[str]) -> List[str]:
    words = set(word_dict)
    max_len = max(map(len, words)) if words else 0
    memo = {}

    def break_from(start: int) -> List[str]:
        if start == len(s):
            return [""]                      # one way: empty sentence
        if start in memo:
            return memo[start]

        sentences = []
        for end in range(start + 1, min(len(s), start + max_len) + 1):
            piece = s[start:end]
            if piece in words:
                for rest in break_from(end):
                    sentences.append(piece if rest == "" else piece + " " + rest)

        memo[start] = sentences
        return sentences

    return break_from(0)


if __name__ == "__main__":
    print(word_break("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
    # ['cat sand dog', 'cats and dog']
    print(word_break("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))
    # ['pine apple pen apple', 'pine applepen apple', 'pineapple pen apple']
    print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    # []
