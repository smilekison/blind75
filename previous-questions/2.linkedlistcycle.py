# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x  # Value of the node
        self.next = None  # Pointer to the next node

class Solution:
    def hasCycle(self, head: ListNode) -> bool:  # Method to check if a linked list has a cycle
        if not head:
            return False
        
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False