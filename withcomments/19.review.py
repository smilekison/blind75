# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Value of the node
        self.left = left  # Left child of the node
        self.right = right  # Right child of the node

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:  # Method to check if two binary trees are the same
        if not p and not q:  # If both trees are empty, they are the same
            return True
        
        if p and q and p.val == q.val:  # If both trees are non-empty and their root values are the same
            # Recursively check the left and right subtrees
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        return False  # If one tree is empty and the other is not, or their root values differ, they are not the same
    

'''
Summary

    DSA Used: Binary Tree, Recursive Tree Traversal.

    Time Complexity: O(n).

    Space Complexity: O(n) in the worst case, O(log n) in the best case.

'''