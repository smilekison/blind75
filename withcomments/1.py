from typing import Optional  # Importing Optional for type hints (not used in this code)

class Solution:
    def reverseList(head):  # Method to reverse a linked list
        if not head:  # If the linked list is empty, return None
            return head
        
        ptr1 = head  # Initialize ptr1 to the head of the linked list
        ptr2 = ptr1.next  # Initialize ptr2 to the next node of ptr1
        
        while ptr2:  # Loop until ptr2 reaches the end of the linked list
            ptr1.next = ptr2.next  # Update ptr1's next to skip ptr2
            ptr2.next = head  # Move ptr2 to the front of the list
            head = ptr2  # Update the head to ptr2
            ptr2 = ptr1.next  # Move ptr2 to the next node of ptr1
        
        return head  # Return the new head of the reversed linked list
    

'''

Summary

    DSA Used: Singly Linked List, Iterative Linked List Reversal.

    Time Complexity: O(n).

    Space Complexity: O(1).
    
    '''