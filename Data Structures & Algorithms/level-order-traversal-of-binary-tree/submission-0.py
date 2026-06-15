# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        tree = []
        q = deque()

        if root:
            q.append(root)
            tree.append([root.val])
        

        while q:
            childs = []

            for i in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                    childs.append(cur.left.val)
                if cur.right:
                    q.append(cur.right)
                    childs.append(cur.right.val)
            if childs:
                tree.append(childs)
        return tree





            

        




        