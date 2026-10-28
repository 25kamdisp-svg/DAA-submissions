"""
DAA Lab - Backtracking
Problem 16: N-Queens II (LeetCode #52)

Backtracking idea:
  - Place one queen per row, trying every column in that row.
  - A column is safe if no earlier queen shares its column or either diagonal.
        column index          : c
        "/" diagonal (r + c)  : constant along the diagonal
        "\" diagonal (r - c)  : constant along the diagonal
  - Mark the column/diagonals as used, recurse to the next row, then un-mark
    (backtrack). Reaching row n means a valid arrangement, so count it.

Time: O(n!)   Space: O(n)
"""


def total_n_queens(n: int) -> int:
    cols = set()
    diag1 = set()     # r + c
    diag2 = set()     # r - c
    count = 0

    def place(row: int) -> None:
        nonlocal count
        if row == n:
            count += 1
            return

        for col in range(n):
            if col in cols or (row + col) in diag1 or (row - col) in diag2:
                continue                         # attacked, skip

            cols.add(col)
            diag1.add(row + col)
            diag2.add(row - col)

            place(row + 1)

            cols.remove(col)                     # backtrack
            diag1.remove(row + col)
            diag2.remove(row - col)

    place(0)
    return count


if __name__ == "__main__":
    print(total_n_queens(4))    # 2
    print(total_n_queens(1))    # 1
    print(total_n_queens(6))    # 4
    print(total_n_queens(8))    # 92
