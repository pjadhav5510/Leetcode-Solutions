# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        h = defaultdict(list)
        def dfs(root,x):
            if not root: return 
            h[x].append(root.val)
            dfs(root.left,x+1)
            dfs(root.right,x+1)
        dfs(root,0)
        return h.values()
        
        
        