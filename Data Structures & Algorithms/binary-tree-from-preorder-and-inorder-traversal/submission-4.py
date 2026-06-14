# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre = deque(preorder)


        def dfs(sub):
            nonlocal pre
            if not pre or not sub:
                return None

            x = pre.popleft()

            root = TreeNode(x)
            mid = sub.index(x)

            root.left = dfs(sub[:mid])
            root.right = dfs(sub[mid + 1:])

            return root
        mainroot = dfs(inorder)
        return mainroot

        


            