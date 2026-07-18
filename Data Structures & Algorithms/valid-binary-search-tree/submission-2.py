# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        ans = True

        def dfs(root, low, high):
            nonlocal ans
            if not ans:
                return
            if root.val <= low or root.val >= high:
                ans = False
                return
            if root.left:
                dfs(root.left, low, root.val)
            if root.right:
                dfs(root.right, root.val, high)

        dfs(root, float('-inf'), float('inf'))
        return ans
        



        
        