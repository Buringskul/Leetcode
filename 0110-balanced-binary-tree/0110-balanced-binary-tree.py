# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        answer = True
        
        def maxDepth(root: Optional[TreeNode]) -> int:
            nonlocal answer
            if not root or not answer:
                return 0

            maxright = maxDepth(root.right)
            maxleft = maxDepth(root.left)
            
            if abs(maxleft - maxright) > 1:
                answer = False;
        
            return 1 + max(maxright, maxleft)
        
        temp = maxDepth(root)
        return answer