"""
DAA Lab - Dynamic Programming
Problem 7: Longest Valid Parentheses (LeetCode #32)

DP idea:
  dp[i] = length of the longest valid substring ending at index i.
  Only positions with ')' can have dp[i] > 0.
  - If s[i-1] == '(':  dp[i] = dp[i-2] + 2
  - Else if s[i-1] == ')' and the char just before the valid block ending
    at i-1 is '(':     dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2

Time: O(n)   Space: O(n)
"""


def longest_valid_parentheses(s: str) -> int:
    n = len(s)
    dp = [0] * n
    best = 0

    for i in range(1, n):
        if s[i] != ")":
            continue

        if s[i - 1] == "(":
            dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
        else:
            j = i - dp[i - 1] - 1      # index before the valid block ending at i-1
            if j >= 0 and s[j] == "(":
                dp[i] = dp[i - 1] + 2 + (dp[j - 1] if j >= 1 else 0)

        best = max(best, dp[i])

    return best


if __name__ == "__main__":
    print(longest_valid_parentheses("(()"))        # 2
    print(longest_valid_parentheses(")()())"))     # 4
    print(longest_valid_parentheses(""))           # 0
    print(longest_valid_parentheses("()(())"))     # 6
