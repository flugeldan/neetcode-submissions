# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        back = deque()
        tree = []
        been = set()

        

        cur = root

        while True:
            if cur in been:
                tree.append(cur.val)
                if cur.right and cur.right not in been:
                    cur = cur.right
                else:
                    if not back:
                        break
                    cur = back.popleft()
                continue
            if cur.left:
                back.appendleft(cur)
                been.add(cur)
                cur = cur.left
            elif not cur.left and cur.right:
                tree.append(cur.val)
                been.add(cur)
                cur = cur.right
            elif not cur.left and not cur.right:
                been.add(cur)
                tree.append(cur.val)
                if not back:
                    break
                cur = back.popleft()
        return tree
            







                
            




        

            





        

