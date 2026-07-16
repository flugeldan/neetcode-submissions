# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(root, prev, streak):
            if not root:
                return streak
            
            if root.val - prev != 1:
                new = 1
            else:
                new = streak + 1
            right = dfs(root.right, root.val, new)
            left = dfs(root.left, root.val, new)
            return max(streak, left, right)
        return dfs(root, 0, 0)
            

        