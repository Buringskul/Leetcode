# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node):
            if not node:
                return

            if not node.right and not node.left:
                if node.val == 1:
                    return node
                else:
                    return None
            
            node.left = helper(node.left)
            node.right = helper(node.right)
            
            if node.left or node.right or node.val == 1:
                return node
            
            return None
        
        return helper(root)
                    