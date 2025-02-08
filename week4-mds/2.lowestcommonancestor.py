class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        temp = root 

        while temp:
            if p.val > temp.val and q.val > temp.val:
                temp = temp.right
            elif p.val < temp.val and q.val < temp.val:
                temp = temp.left
            else:
                return temp


#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/solutions/4276179/beats-99-o-log-n-step-by-step-explanation