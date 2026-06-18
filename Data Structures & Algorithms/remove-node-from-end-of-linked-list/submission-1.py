# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return None
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        i = len(nodes) - n
        if i - 1 >= 0:
            if i + 1 < len(nodes):
                nodes[i - 1].next = nodes[i + 1]
            else:
                nodes[i - 1].next = None
        else:
            head = nodes[i].next
        return head
        

        