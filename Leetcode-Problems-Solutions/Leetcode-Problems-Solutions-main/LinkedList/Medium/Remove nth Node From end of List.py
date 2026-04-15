# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next :
            return None
        current = head
        nb = 0
        while current :
            nb += 1
            current = current.next
        if nb == n :
            return head.next
        index = nb-n+1
        i = 1
        current = head
        while current :
            if i == index - 1 :
                current.next = current.next.next
                return head
            current = current.next
            i += 1
          
        
