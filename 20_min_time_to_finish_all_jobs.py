"""
DAA Lab - Backtracking
Problem 20: Find Minimum Time to Finish All Jobs (LeetCode #1723)

Backtracking idea:
  - Assign each job to one of the k workers and keep the best (smallest)
    "maximum workload" found.
  - Pruning to make it fast:
      1. Sort jobs in descending order (big jobs first fail early).
      2. If the current maximum load is already >= best, stop this branch.
      3. If several workers have the same load, trying one of them is enough
         (the others give identical results).

Time: exponential, but heavily pruned (k^n worst case)   Space: O(n + k)
"""
from typing import List


def minimum_time_required(jobs: List[int], k: int) -> int:
    jobs = sorted(jobs, reverse=True)
    loads = [0] * k
    best = float("inf")

    def assign(i: int, current_max: int) -> None:
        nonlocal best
        if current_max >= best:                  # cannot improve
            return
        if i == len(jobs):
            best = current_max
            return

        tried = set()
        for w in range(k):
            if loads[w] in tried:                # same load -> same outcome
                continue
            tried.add(loads[w])

            loads[w] += jobs[i]                  # choose
            assign(i + 1, max(current_max, loads[w]))
            loads[w] -= jobs[i]                  # un-choose

    assign(0, 0)
    return best


if __name__ == "__main__":
    print(minimum_time_required([3, 2, 3], 3))            # 3
    print(minimum_time_required([1, 2, 4, 7, 8], 2))      # 11
    print(minimum_time_required([5], 1))                  # 5
