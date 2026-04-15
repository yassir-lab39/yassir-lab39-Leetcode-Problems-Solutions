# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        m = 0
        nb = 0
        current1 = l1
        current2 = l2
        while current1 :
            n += current1.val * (10**nb)
            nb += 1
            current1 = current1.next
        nb = 0
        while current2 :
            m += current2.val * (10**nb)
            nb += 1
            current2 = current2.next
        res = m+n
        if m > n :
            l = l2
        else :
            l = l1
        current = l
        while res != 0 and current :
            current.val = res % 10
            res -= res % 10
            res //= 10
            if not current.next and res != 0 :
                current.next = ListNode(res)
            current = current.next
        return l

        
