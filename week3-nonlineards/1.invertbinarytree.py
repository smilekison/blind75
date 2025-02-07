class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        # Swap left and right children
        root.left, root.right = root.right, root.left

        # Recurse on left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    

# https://leetcode.com/problems/invert-binary-tree/solutions/6082525/0-ms-runtime-beats-100-user-code-idea-algorithm-solving-step