"""
DAA Lab - Divide and Conquer
Problem 14: Binary Tree Maximum Path Sum (LeetCode #124)

Divide & Conquer idea (on the tree):
  - Divide: solve for the left subtree and the right subtree.
  - Each call returns the best "downward" path sum starting at that node
        gain(node) = node.val + max(0, gain(left), gain(right))
    (negative gains are dropped by taking max with 0).
  - Combine: a path that bends at this node has sum
        node.val + max(0, gain(left)) + max(0, gain(right))
    and the global answer is the maximum over all nodes.

Time: O(n)   Space: O(h)   (h = height of the tree)
"""
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root: Optional[TreeNode]) -> int:
    best = float("-inf")

    def gain(node: Optional[TreeNode]) -> int:
        nonlocal best
        if node is None:
            return 0

        left = max(gain(node.left), 0)      # ignore negative contributions
        right = max(gain(node.right), 0)

        best = max(best, node.val + left + right)    # path bending at this node
        return node.val + max(left, right)           # path going up to parent

    gain(root)
    return best


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Build a tree from a LeetCode style level-order list (None = empty)."""
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


if __name__ == "__main__":
    print(max_path_sum(build_tree([1, 2, 3])))                              # 6
    print(max_path_sum(build_tree([-10, 9, 20, None, None, 15, 7])))        # 42
    print(max_path_sum(build_tree([-3])))                                   # -3
