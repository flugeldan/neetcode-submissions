class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(cur1, cur2):
            dummy = ListNode(0)
            tail = dummy
            while cur1 and cur2:
                if cur1.val < cur2.val:
                    tail.next = cur1
                    tail = tail.next
                    cur1 = cur1.next
                else:
                    tail.next = cur2
                    tail = tail.next
                    cur2 = cur2.next
            if cur1:
                tail.next = cur1
                tail = tail.next
            if cur2:
                tail.next = cur2
                tail = tail.next
            return dummy.next

        def dividing(givenList):
            if len(givenList) == 1:
                return givenList[0]
            elif not givenList:
                return None
            
            mid = len(givenList) // 2
            left = givenList[:mid]
            right = givenList[mid:]
            left_sorted = dividing(left)
            right_sorted = dividing(right)
            return merge(left_sorted, right_sorted)
        return dividing(lists)

        