# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        ans = 0



        def dfs(root, curMax):
            nonlocal ans
            if root.val >= curMax:
                curMax = root.val
                ans += 1 
            
            if root.left:
                dfs(root.left, curMax)
            if root.right:
                dfs(root.right, curMax)
        
        dfs(root, float('-inf'))
        return ans

            


        