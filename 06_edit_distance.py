"""
DAA Lab - Dynamic Programming
Problem 6: Edit Distance (LeetCode #72)

DP idea:
  dp[i][j] = min operations to convert word1[:i] into word2[:j]
  - If word1[i-1] == word2[j-1]: dp[i][j] = dp[i-1][j-1]
  - Else: 1 + min(dp[i-1][j]    -> delete,
                  dp[i][j-1]    -> insert,
                  dp[i-1][j-1]  -> replace)
  Base: dp[i][0] = i, dp[0][j] = j

Time: O(m * n)   Space: O(n) (only the previous row is kept)
"""


def min_distance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    prev = list(range(n + 1))          # dp[0][j] = j

    for i in range(1, m + 1):
        curr = [i] + [0] * n           # dp[i][0] = i
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(prev[j],        # delete
                                  curr[j - 1],    # insert
                                  prev[j - 1])    # replace
        prev = curr

    return prev[n]


if __name__ == "__main__":
    print(min_distance("horse", "ros"))            # 3
    print(min_distance("intention", "execution"))  # 5
    print(min_distance("", "abc"))                 # 3
