# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def build(preorder, inorder):
            if not inorder: 
                return None
            
            curr_val = preorder.pop(0)
            node = TreeNode(curr_val)
            index = inorder.index(curr_val)
            
            node.left = build(preorder, inorder[:index])
            node.right = build(preorder, inorder[index + 1:])
            
            return node
        
        return build(preorder, inorder)