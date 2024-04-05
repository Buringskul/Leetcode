# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        def helper(root):
            nonlocal ans
            
            if not root:
                return 0
            
            left_bal = helper(root.left)
            right_bal = helper(root.right)
            
            curr_bal = left_bal + right_bal + root.val - 1
            moves = abs(left_bal) + abs(right_bal)
            ans += moves
            return curr_bal
        
        ans = 0
        helper(root)
        return ans