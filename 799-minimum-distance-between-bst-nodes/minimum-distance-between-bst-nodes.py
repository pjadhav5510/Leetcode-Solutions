# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.prev = float('-inf')
        self.z = float('inf')

        def dfs(root):
            if not root: return

            dfs(root.left)
            self.z = min(self.z,root.val - self.prev)
            self.prev = root.val
            dfs(root.right)
        dfs(root)
        return self.z
        