# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        self.p = None
        self.x = float('inf')
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            print('p: ',self.p, '   root.val: ',root.val)
            if self.p != None:
                self.x = min(self.x, root.val - self.p)
            print('x: ',self.x)
            self.p = root.val
            dfs(root.right)
        dfs(root)
        return self.x