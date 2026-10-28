"""
DAA Lab - Dynamic Programming
Problem 9: Race Car (LeetCode #818)

Instructions: 'A' = accelerate (pos += speed, speed *= 2), 'R' = reverse
(speed = -1 or 1). Start at position 0 with speed +1.

DP idea:
  dp[t] = min instructions to reach position t.
  Let n = number of bits of t, so 2^(n-1) <= t < 2^n.
  1. If t == 2^n - 1: just n accelerations.            -> dp[t] = n
  2. Overshoot: go n 'A's to 2^n - 1, then 'R', then solve the rest.
        dp[t] = n + 1 + dp[2^n - 1 - t]
  3. Stop short: go n-1 'A's to 2^(n-1) - 1, 'R', go back m 'A's
     (covering 2^m - 1), 'R' again, then solve the remaining distance.
        dp[t] = (n-1) + 1 + m + 1 + dp[t - (2^(n-1) - 1) + (2^m - 1)]
     for m = 0 .. n-2

Time: O(t log^2 t)   Space: O(t)
"""
from functools import lru_cache


def racecar(target: int) -> int:
    @lru_cache(maxsize=None)
    def dp(t: int) -> int:
        n = t.bit_length()

        if t == (1 << n) - 1:               # exactly 2^n - 1
            return n

        # Option 1: overshoot past t, then reverse
        best = n + 1 + dp((1 << n) - 1 - t)

        # Option 2: stop short at 2^(n-1) - 1, reverse, go back m steps, reverse
        for m in range(n - 1):
            back = (1 << m) - 1
            forward = (1 << (n - 1)) - 1
            best = min(best, (n - 1) + 1 + m + 1 + dp(t - forward + back))

        return best

    return dp(target)


if __name__ == "__main__":
    print(racecar(3))     # 2   ("AA")
    print(racecar(6))     # 5   ("AAARA")
    print(racecar(4))     # 5
    print(racecar(5))     # 7
