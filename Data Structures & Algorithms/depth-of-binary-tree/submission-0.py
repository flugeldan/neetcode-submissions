# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxDepth = 0
        
        def dfs(root, curDepth):
            nonlocal maxDepth
            if not root:
                return
            curDepth += 1 
            maxDepth = max(maxDepth,curDepth)
            dfs(root.left, curDepth)
            dfs(root.right, curDepth)
        dfs(root, 0)
        return maxDepth
        