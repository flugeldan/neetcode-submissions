# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if val > root.val:
            root.right = self.deleteNode(root.right, key)
        elif val < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                root = None
                return root
            if root.left and not root.right:
                root = root.left
            elif root.right and not root.left:
                root = root.right
            else:
               insertNode = root.left #что узел для вставки
               root = root.right #ставим корнем правое поддерево
               cur = root #просто чтобы траверсить            

               while cur.left:
                cur = cur.left

               cur.left = insertNode
            return root



                
                






        return root
            
                



         
        