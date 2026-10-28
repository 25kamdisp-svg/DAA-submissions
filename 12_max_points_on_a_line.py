"""
DAA Lab - Divide and Conquer
Problem 12: Max Points on a Line (LeetCode #149)

Idea:
  - Fix a point p. Every other point q lies on exactly one line through p,
    identified by its slope.
  - Count how many points share each slope with p (hash map). The best line
    through p has 1 (p itself) + max count.
  - Slope is stored as a reduced fraction (dy/gcd, dx/gcd) with a fixed sign,
    so no floating point errors occur.
  - Repeat for every point as the base point. Subproblem = "best line through
    point i using the points after it".

Time: O(n^2)   Space: O(n)
"""
from collections import defaultdict
from math import gcd
from typing import List


def max_points(points: List[List[int]]) -> int:
    n = len(points)
    if n <= 2:
        return n

    best = 1
    for i in range(n):
        slopes = defaultdict(int)
        x1, y1 = points[i]

        for j in range(i + 1, n):
            x2, y2 = points[j]
            dx, dy = x2 - x1, y2 - y1

            g = gcd(dx, dy)
            dx, dy = dx // g, dy // g
            if dx < 0 or (dx == 0 and dy < 0):      # normalise the sign
                dx, dy = -dx, -dy

            slopes[(dx, dy)] += 1
            best = max(best, slopes[(dx, dy)] + 1)

    return best


if __name__ == "__main__":
    print(max_points([[1, 1], [2, 2], [3, 3]]))                                  # 3
    print(max_points([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))          # 4
    print(max_points([[0, 0]]))                                                  # 1
