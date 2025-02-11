from typing import Optional  # Importing Optional for type hints (not used in this code)

class Solution:
    def reverseList(head):  # Method to reverse a linked list
        if not head:
            return 0
        
        pointer1 = head
        pointer2 = pointer1.next


        while pointer2:
            pointer1.next = pointer2.next
            pointer2.next = head
            head = pointer2
            pointer2 = pointer1.next

        return head