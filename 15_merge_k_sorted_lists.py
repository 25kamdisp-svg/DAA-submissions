"""
DAA Lab - Divide and Conquer
Problem 15: Merge k Sorted Lists (LeetCode #23)

Divide & Conquer idea:
  - Divide: split the k lists into two halves.
  - Conquer: merge each half recursively into one sorted list.
  - Combine: merge the two sorted lists with the standard two-list merge.
  Every element takes part in log k merges, so the total is O(N log k).

Time: O(N log k)  (N = total nodes)   Space: O(log k) recursion
"""
from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" = None):
        self.val = val
        self.next = next


def merge_two(a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy

    while a and b:
        if a.val <= b.val:
            tail.next, a = a, a.next
        else:
            tail.next, b = b, b.next
        tail = tail.next

    tail.next = a or b
    return dummy.next


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    def solve(lo: int, hi: int) -> Optional[ListNode]:
        if lo > hi:
            return None
        if lo == hi:
            return lists[lo]
        mid = (lo + hi) // 2
        return merge_two(solve(lo, mid), solve(mid + 1, hi))

    return solve(0, len(lists) - 1)


def to_linked_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(node: Optional[ListNode]) -> List[int]:
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


if __name__ == "__main__":
    lists = [to_linked_list([1, 4, 5]), to_linked_list([1, 3, 4]), to_linked_list([2, 6])]
    print(to_list(merge_k_lists(lists)))     # [1, 1, 2, 3, 4, 4, 5, 6]
    print(to_list(merge_k_lists([])))        # []
    print(to_list(merge_k_lists([None])))    # []
