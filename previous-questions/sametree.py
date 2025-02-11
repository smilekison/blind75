# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Value of the node
        self.left = left  # Left child of the node
        self.right = right  # Right child of the node

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:  # Method to check if two binary trees are the same
        