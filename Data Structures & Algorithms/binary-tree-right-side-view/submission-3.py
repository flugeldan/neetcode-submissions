# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([(root,0)])
        stack = [0]
        vis = [root.val]

        while len(q) > 0:

            for i in range(len(q)):
                x, lvl = q.popleft()
                if stack[-1] < lvl:
                    vis.append(x.val)
                    stack.append(lvl)
                if x.right:
                    q.append((x.right, lvl + 1))
                if x.left:
                    q.append((x.left, lvl + 1))
        return vis
                    
        



                


        

                

                



        
        
        
        
        
        
        

        




        






        