# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        p0 = p1 = p2 = head
        for _ in range(n):
            p2 = p2.next
        if not p2:
            head = head.next
        while p2:
            p0 = p1
            p1 = p1.next
            p2 = p2.next
        p0.next = p1.next
        return head
        



        

        