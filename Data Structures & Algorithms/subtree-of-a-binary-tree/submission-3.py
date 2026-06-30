# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        elif root and not subRoot or subRoot and not root:
            return False

        thatRoots = []
        stack = []
        while stack or root:
            while root:
                if root.val == subRoot.val:
                    thatRoots.append(root)

                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        if not thatRoots:
            return False
        ans = True
        def dfs(root1, root2):
            nonlocal ans
            if root1.val != root2.val or root1.left and not root2.left or root1.right and not root2.right:
                ans = False
                return
            if root2.left and not root1.left or root2.right and not root1.right:
                ans = False
                return
            if root1.left:
                dfs(root1.left, root2.left)    
            if root1.right:
                dfs(root1.right, root2.right)
        
        for cur in thatRoots:
            ans = True
            dfs(subRoot, cur)


            if ans:
                
                return ans
        return False
            
        
        
            

        