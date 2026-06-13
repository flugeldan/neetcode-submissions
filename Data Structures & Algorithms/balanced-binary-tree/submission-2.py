# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True


        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)

            if left is False or right is False:
                return False

            if abs(left - right) > 1:
                return False
            
            return max(left, right) + 1
        ans = helper(root)

        return ans if ans is False else True

            




            

        