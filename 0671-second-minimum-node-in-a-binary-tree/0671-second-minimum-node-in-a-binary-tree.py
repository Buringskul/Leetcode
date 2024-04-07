# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        
        def inorder(node, arr):
            if not node:
                return
            
            arr.add(node.val)
            inorder(node.left, arr)
            inorder(node.right, arr)
            
        arr = set()
        inorder(root, arr)
        return -1 if len(arr) < 2 else sorted(arr)[1]