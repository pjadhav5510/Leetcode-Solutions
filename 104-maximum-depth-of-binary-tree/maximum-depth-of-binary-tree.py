# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.helper(root)
        
        
    def helper(self,root):
        if not root: return 0
        return max(self.helper(root.left),self.helper(root.right))+1