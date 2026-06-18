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

        p0 = p1 = head
        cur = head
        length = 0
        while cur:
            length += 1 
            cur = cur.next
        if length - n == 0:
            head = head.next
            return head
        pointer = 0
        while p1:
            if pointer == length - n:
                p0.next = p1.next
                return head


            p0 = p1
            p1 = p1.next
            pointer += 1 





        

        