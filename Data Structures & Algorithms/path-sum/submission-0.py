# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        flag = False
        
        def helper(root, targetSum, curSum):
            nonlocal flag
            curSum += root.val
            if not root.right and not root.left:
                if curSum == targetSum:
                    flag = True
                return
                
            
            if root.left:
                helper(root.left, targetSum, curSum)
            if root.right:
                helper(root.right, targetSum, curSum)
        helper(root, targetSum, 0)
        
        return flag

