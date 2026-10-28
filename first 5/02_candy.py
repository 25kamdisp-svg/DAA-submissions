"""
DAA Lab - Greedy Algorithm
Problem 2: Candy (LeetCode #135)

Greedy idea (two passes):
  - Left -> right: if rating[i] > rating[i-1], candy[i] = candy[i-1] + 1
  - Right -> left: if rating[i] > rating[i+1],
                   candy[i] = max(candy[i], candy[i+1] + 1)

Time: O(n)   Space: O(n)
"""
from typing import List


def candy(ratings: List[int]) -> int:
    n = len(ratings)
    candies = [1] * n

    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)


if __name__ == "__main__":
    print(candy([1, 0, 2]))   # 5
    print(candy([1, 2, 2]))   # 4
