# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        def helper(node, freq):
            if not node:
                return
            
            if node.val in freq:
                freq[node.val] += 1
            else:
                freq[node.val] = 1
            
            helper(node.left, freq)
            helper(node.right, freq)
            
        
        freq = {}
        ans = []
        helper(root, freq)
        mode = max(freq.values())
        for key, value in freq.items():
            if value == mode:
                ans.append(key)
            
        return ans
            