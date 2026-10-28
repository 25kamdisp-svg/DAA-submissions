"""
DAA Lab - Backtracking
Problem 17: Word Ladder II (LeetCode #126)

Idea (BFS + backtracking):
  1. BFS from beginWord, level by level. For every word reached, remember all
     its parents on the shortest path (a word can have several parents).
     Stop after the level where endWord is found, so only shortest paths exist.
  2. Backtrack from endWord through the parents map up to beginWord to
     build every shortest transformation sequence.

Time: depends on number of shortest paths   Space: O(N * L)
"""
from collections import defaultdict
from typing import List


def find_ladders(begin_word: str, end_word: str, word_list: List[str]) -> List[List[str]]:
    words = set(word_list)
    if end_word not in words:
        return []

    words.discard(begin_word)
    parents = defaultdict(set)
    level = {begin_word}
    found = False

    # ---- Step 1: BFS building the parents map ----
    while level and not found:
        next_level = set()
        for word in level:
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    nxt = word[:i] + ch + word[i + 1:]
                    if nxt in words:
                        next_level.add(nxt)
                        parents[nxt].add(word)
                        if nxt == end_word:
                            found = True
        words -= next_level          # remove only after the whole level is done
        level = next_level

    if not found:
        return []

    # ---- Step 2: backtrack from endWord to beginWord ----
    result = []
    path = [end_word]

    def backtrack(word: str) -> None:
        if word == begin_word:
            result.append(path[::-1])
            return
        for p in parents[word]:
            path.append(p)
            backtrack(p)
            path.pop()               # undo choice

    backtrack(end_word)
    return sorted(result)


if __name__ == "__main__":
    print(find_ladders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
    # [['hit', 'hot', 'dot', 'dog', 'cog'], ['hit', 'hot', 'lot', 'log', 'cog']]
    print(find_ladders("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
    # []
