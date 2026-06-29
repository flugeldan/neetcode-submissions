# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and not q or q and not p:
            return False
        elif not p and not q:
            return True
        q1 = deque([p])
        q2 = deque([q])
        while q1 and q2:
            t1 = q1.popleft()
            t2 = q2.popleft()
            if t1 and not t2 or t2 and not t1:
                return False
            if t1.val != t2.val:
                return False
            if t1.left and not t2.left or t2.left and not t1.left:
                return False
            if t1.right and not t2.right or t2.right and not t1.right:
                return False
            if t1.left and t2.left and t1.left.val != t2.left.val:
                return False
            if t1.right and t2.right and t1.right.val != t2.right.val:
                return False
            if t1.left:
                q1.append(t1.left)
                q2.append(t2.left)
            if t1.right:
                q1.append(t1.right)
                q2.append(t2.right)
        return True if not q1 and not q2 else False
        