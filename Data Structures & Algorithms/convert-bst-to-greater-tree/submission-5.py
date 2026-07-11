# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        stack = []
        total = 0
        cur = root
        while root or stack:
            while root:
                stack.append(root)
                root = root.right
            root = stack.pop()
            total += root.val
            root.val = total
            root = root.left
        return cur
            

            