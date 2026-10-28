"""
DAA Lab - Greedy Algorithm
Problem 1: Gas Station (LeetCode #134)

Greedy idea:
  - If total gas >= total cost, a solution exists.
  - If the tank goes negative at station i, no station from the current
    start up to i can be the answer, so the next candidate is i + 1.

Time: O(n)   Space: O(1)
"""
from typing import List


def can_complete_circuit(gas: List[int], cost: List[int]) -> int:
    total_surplus = 0
    tank = 0
    start = 0

    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total_surplus += diff
        tank += diff

        if tank < 0:          # cannot reach station i + 1 from `start`
            start = i + 1     # try the next station as the new start
            tank = 0

    return start if total_surplus >= 0 else -1


if __name__ == "__main__":
    print(can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))   # 3
    print(can_complete_circuit([2, 3, 4], [3, 4, 3]))               # -1
