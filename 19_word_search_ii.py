"""
DAA Lab - Backtracking
Problem 19: Word Search II (LeetCode #212)

Idea (Trie + backtracking DFS):
  - Insert all words into a Trie so many words are searched at once.
  - From every cell, DFS along the Trie: move to a neighbour only if its
    letter is a child of the current Trie node.
  - Mark the cell as visited while exploring (set to '#'), then restore it
    (backtrack).
  - When a node stores a complete word, add it to the result and clear it so
    the same word is not added twice.

Time: O(m * n * 4 * 3^(L-1))   Space: O(total letters in words)
"""
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None            # full word stored at its last letter


def find_words(board: List[List[str]], words: List[str]) -> List[str]:
    root = TrieNode()
    for w in words:
        node = root
        for ch in w:
            node = node.children.setdefault(ch, TrieNode())
        node.word = w

    rows, cols = len(board), len(board[0])
    result = []

    def dfs(r: int, c: int, parent: TrieNode) -> None:
        ch = board[r][c]
        node = parent.children[ch]

        if node.word:
            result.append(node.word)
            node.word = None        # avoid duplicates

        board[r][c] = "#"           # mark visited
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in node.children:
                dfs(nr, nc, node)
        board[r][c] = ch            # backtrack: restore the cell

        if not node.children:       # prune exhausted Trie branches
            del parent.children[ch]

    for r in range(rows):
        for c in range(cols):
            if board[r][c] in root.children:
                dfs(r, c, root)

    return result


if __name__ == "__main__":
    board1 = [["o", "a", "a", "n"],
              ["e", "t", "a", "e"],
              ["i", "h", "k", "r"],
              ["i", "f", "l", "v"]]
    print(sorted(find_words(board1, ["oath", "pea", "eat", "rain"])))   # ['eat', 'oath']

    board2 = [["a", "b"],
              ["c", "d"]]
    print(find_words(board2, ["abcb"]))                                 # []
