class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        L = []
        v = 0.5
        a = False
        while current:
            if a and v == current.val :
                L.pop()
                a = False
            if v != current.val:
                v = current.val
                L.append(ListNode(v))  
                a = True
            current = current.next
        while len(L) > 1:
            a = L.pop()
            L[-1].next = a
        return L[0] if L else None
