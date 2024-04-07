# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def helper(node, path_sum):
            if not node:
                return 0
            
            if not node.left and not node.right:
                path_sum += str(node.val)
                return int(path_sum)
            
            path_sum += str(node.val)
            return helper(node.left, path_sum) + helper(node.right, path_sum)
            
        return helper(root, "")