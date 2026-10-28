"""
DAA Lab - Greedy Algorithm
Problem 4: Minimum Cost to Hire K Workers (LeetCode #857)

Greedy idea:
  - Everyone in the group is paid at the same wage/quality ratio, which must
    be >= the largest ratio in the group.
  - Cost = (max ratio in group) * (sum of qualities in group).
  - Sort workers by ratio. Going in that order, the current worker has the
    max ratio so far. Keep the k smallest qualities using a max-heap.

Time: O(n log n)   Space: O(n)
"""
import heapq
from typing import List


def mincost_to_hire_workers(quality: List[int], wage: List[int], k: int) -> float:
    workers = sorted(zip(quality, wage), key=lambda w: w[1] / w[0])

    max_heap = []          # negative qualities (max-heap using heapq)
    quality_sum = 0
    best = float("inf")

    for q, w in workers:
        ratio = w / q
        heapq.heappush(max_heap, -q)
        quality_sum += q

        if len(max_heap) > k:
            quality_sum += heapq.heappop(max_heap)   # popped value is negative

        if len(max_heap) == k:
            best = min(best, ratio * quality_sum)

    return best


if __name__ == "__main__":
    print(round(mincost_to_hire_workers([10, 20, 5], [70, 50, 30], 2), 5))             # 105.0
    print(round(mincost_to_hire_workers([3, 1, 10, 10, 1], [4, 8, 2, 2, 7], 3), 5))    # 30.66667
