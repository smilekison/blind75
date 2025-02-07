from typing import Optional


class Solution:
    def reverseList(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    

    # https://leetcode.com/problems/reverse-linked-list/solutions/6060433/0-ms-runtime-beats-100-user-confirm-step-by-steps-solution-beginner-friendly