# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        c = 0
        self.x = 99999
        def dfs(root,c):
            if not root:
                return 0
            else:
                c+=1
            if not root.left and not root.right:
                print(c)
                self.x = min(self.x,c)
                #print('x: ',x)
                c=0
            dfs(root.left,c)
            dfs(root.right,c)
        dfs(root,c)
        if not root:
            return 0
        else:
            return self.x
        