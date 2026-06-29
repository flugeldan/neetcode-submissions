# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        subtrees = {}
        q = deque([root])
        while q:
            cur = q.popleft()
            subtrees[cur] = (cur.left, cur.right)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        def dfs(node):
            if not node:
                return
            node.left, node.right = subtrees[node][1], subtrees[node][0]
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return root
        



