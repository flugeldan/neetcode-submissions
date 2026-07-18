# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        ans = []
        been = set()
        while stack or root:
            while root:
                stack.append(root)
                been.add(root)
                root = root.left
            root = stack.pop()
            if root.right and root.right in been or not root.right:
                ans.append(root.val)
                root = None
            else:
                stack.append(root)
                root = root.right

            

            
        return ans


        
            



        