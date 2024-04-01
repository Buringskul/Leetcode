# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def helper(root, currPath):
            if not root:
                return
            
            currPath.append(str(root.val))
            
            if not root.left and not root.right:
                allPaths.append("->".join(currPath))

            helper(root.left, currPath)
            helper(root.right, currPath)
            
            currPath.pop()
        
        allPaths = []
        helper(root, [])
        return allPaths