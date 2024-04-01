# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def helper(root, is_left):
            nonlocal ans
            
            if not root:
                return 
            
            if is_left and not root.left and not root.right:
                ans += root.val
            
            helper(root.left, True)
            helper(root.right, False)
        
        helper(root, False)
        return ans
            