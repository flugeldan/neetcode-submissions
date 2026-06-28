"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        visited = set([node])
        q = deque([node])
        nodes = {}
        while q:
            cur = q.popleft()
            new_cur = Node(cur.val, [])
            nodes[cur.val] = new_cur
            for node in cur.neighbors:
                if node not in visited:
                    visited.add(node)
                    q.append(node)
        q = deque([node])
        visited = set([node])
        while q:
            cur = q.popleft()
            new_cur = nodes[cur.val]
            friends = []
            for node in cur.neighbors:
                friends.append(nodes[node.val])
                if node not in visited:
                    q.append(node)
            visited.add(cur)
        
            new_cur.neighbors = friends

            
        return nodes[1]
        
            
        


                    
 

        


        