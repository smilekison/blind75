# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x  # Value of the node
        self.next = None  # Pointer to the next node

class Solution:
    def hasCycle(self, head: ListNode) -> bool:  # Method to check if a linked list has a cycle
        slow = head  # Initialize slow pointer to the head of the linked list
        fast = head  # Initialize fast pointer to the head of the linked list

        while fast and fast.next:  # Traverse the list until fast or fast.next becomes None
            slow = slow.next  # Move slow pointer one step forward
            fast = fast.next.next  # Move fast pointer two steps forward

            if slow == fast:  # If slow and fast pointers meet, a cycle exists
                return True

        return False  # If the loop ends, no cycle exists
    
'''
    DSA Used: Singly Linked List, Floyd’s Cycle Detection Algorithm.

    Time Complexity: O(n).

    Space Complexity: O(1).

'''