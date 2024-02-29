# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return
            if root.left and root.right:
                if root.left.val + root.right.val == root.val:
                    print('jhbjd')
                    return True
            dfs(root.right)
            dfs(root.left)
        return dfs(root)
        