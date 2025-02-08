class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(node):
            if not node:
                return
            # Traverse left subtree
            yield from inorder(node.left)
            # Visit current node
            yield node.val
            # Traverse right subtree
            yield from inorder(node.right)

        # Iterate through inorder traversal and find the k-th smallest
        gen = inorder(root)
        for _ in range(k):
            result = next(gen)
        return result