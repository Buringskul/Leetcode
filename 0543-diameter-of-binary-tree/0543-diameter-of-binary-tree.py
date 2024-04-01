# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def maxDepth(root: Optional[TreeNode]) -> int:
            nonlocal ans
            if not root:
                return 0

            maxright = maxDepth(root.right)
            maxleft = maxDepth(root.left)
            ans = max(ans, maxright + maxleft)
        
            return 1 + max(maxright, maxleft)
        
        ans = 0
        maxDepth(root)
        return ans