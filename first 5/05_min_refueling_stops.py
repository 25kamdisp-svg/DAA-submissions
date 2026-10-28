"""
DAA Lab - Greedy Algorithm
Problem 5: Minimum Number of Refueling Stops (LeetCode #871)

Greedy idea:
  - Drive as far as possible. When we cannot reach the target, refuel from
    the station with the largest fuel among those already passed.
  - A max-heap keeps the stations we have passed.

Time: O(n log n)   Space: O(n)
"""
import heapq
from typing import List


def min_refuel_stops(target: int, start_fuel: int, stations: List[List[int]]) -> int:
    max_heap = []          # negative fuel amounts of stations passed
    fuel = start_fuel      # farthest distance we can reach so far
    stops = 0
    i = 0
    n = len(stations)

    while fuel < target:
        # add all stations reachable with current fuel
        while i < n and stations[i][0] <= fuel:
            heapq.heappush(max_heap, -stations[i][1])
            i += 1

        if not max_heap:   # stuck, nothing to refuel from
            return -1

        fuel += -heapq.heappop(max_heap)
        stops += 1

    return stops


if __name__ == "__main__":
    print(min_refuel_stops(1, 1, []))                                                # 0
    print(min_refuel_stops(100, 1, [[10, 100]]))                                     # -1
    print(min_refuel_stops(100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]]))       # 2
