from typing import Optional


class Solution:
    def reverseList(head):
        if not head:
            return head
        ptr1=head
        ptr2=ptr1.next
        while ptr2:
            ptr1.next=ptr2.next
            ptr2.next=head
            head=ptr2
            ptr2=ptr1.next
        return head
    

    # https://leetcode.com/problems/reverse-linked-list/solutions/6060433/0-ms-runtime-beats-100-user-confirm-step-by-steps-solution-beginner-friendly