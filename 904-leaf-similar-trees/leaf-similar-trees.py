# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        a,b=[],[]
        def dfs(root,b):
            if not root: return
            if not root.left and not root.right : b.append(root.val)
            dfs(root.left,b)
            dfs(root.right,b)
        dfs(root1,b) 
        dfs(root2,a)
        print(a,b)

        if a == b:
            return True
        