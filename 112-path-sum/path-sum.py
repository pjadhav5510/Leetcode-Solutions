# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        c = 0
        self.x = 0
        def dfs(root,c):
            if not root:
                return
            else:
                c+=root.val 
            if not root.left and not root.right:
                print(targetSum)
                if targetSum == c:
                    self.x +=1
            dfs(root.left,c)
            dfs(root.right,c)
        dfs(root,c)
        if self.x > 0:
            return True