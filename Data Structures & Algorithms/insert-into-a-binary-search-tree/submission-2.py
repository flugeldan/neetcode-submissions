# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            root = TreeNode(val)

        elif val < root.val:
            root.left = self.insertIntoBST(root.left, val) #root.left = новая ветка на основа старой

        elif val > root.val:
            root.right = self.insertIntoBST(root.right, val) #root.right = новая ветка на основа старой


        return root
        




        



            
            
        