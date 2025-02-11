from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Value of the node
        self.left = left  # Left child of the node
        self.right = right  # Right child of the node

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:  # Method to compute the maximum depth of a binary tree
        if not root:  # Base case: if the root is None, the depth is 0
            return 0
        
        leftDepth = self.maxDepth(root.left)  # Recursively compute the depth of the left subtree
        rightDepth = self.maxDepth(root.right)  # Recursively compute the depth of the right subtree
        
        return 1 + max(leftDepth, rightDepth)  # Return the maximum depth of the left or right subtree, plus 1 for the current node
    

'''
Summary

    DSA Used: Binary Tree, Recursive Depth-First Search (DFS).

    Time Complexity: O(n).

    Space Complexity: O(n) in the worst case, O(log n) in the best case.

'''