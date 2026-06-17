# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = deque()
        ans = deque()
        cur = head.next
        while cur:
            nodes.append(cur)
            cur = cur.next
        n = len(nodes)
        i = 1
        while len(nodes) >= 2:
            a = nodes.pop()
            b = nodes.popleft()
            ans.append(a)
            ans.append(b)
            if len(nodes) == 1:
                ans.append(nodes.pop())
        ans.appendleft(head)
        for i in range(len(ans)):
            if i + 1 < len(ans):
                ans[i].next = ans[i + 1]
            else:
                ans[i].next = None



            
        
            
            

            


 



