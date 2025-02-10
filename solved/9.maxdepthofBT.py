class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        return 1 + max(leftDepth, rightDepth)
    

#     https://leetcode.com/problems/maximum-depth-of-binary-tree/solutions/6090383/0-ms-runtime-beats-100-user-code-idea-algorithm-solving-step