# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        x = root
        maxSum = float('-inf')
        def dfs(root):
            if not root:
                return float('-inf')
            nonlocal maxSum
            nonlocal x
            left = dfs(root.left)
            right = dfs(root.right)
            returnVal = max(root.val, root.val + left, root.val + right)
            if root is x:
                returnVal = max(returnVal, root.val + left + right
                )
            maxSum = max(returnVal, maxSum, root.val + left + right)
            
            return returnVal
        dfs(root)
        return maxSum
 
            



                



        