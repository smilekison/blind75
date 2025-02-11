from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Value of the node
        self.left = left  # Left child of the node
        self.right = right  # Right child of the node

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:  # Method to compute the maximum depth of a binary tree
        