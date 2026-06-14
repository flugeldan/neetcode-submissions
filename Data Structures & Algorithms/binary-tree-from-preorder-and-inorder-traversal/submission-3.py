# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        leftSub = inorder[:mid]
        rightSub = inorder[mid + 1:]

        root.left = self.buildTree(preorder[1 : mid + 1], leftSub)
        root.right = self.buildTree(preorder[mid + 1 :], rightSub)

        return root









            





        
            



            


