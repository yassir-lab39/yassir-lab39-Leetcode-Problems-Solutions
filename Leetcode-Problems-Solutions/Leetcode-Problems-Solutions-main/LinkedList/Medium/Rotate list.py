# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head :
            return None
        current = head
        n = 0
        while current :
            n += 1
            current = current.next
        k = k % n
        if not head.next or k == 0:
            return head
        current = head
        i = 0
        while i < n-k :
            i += 1
            if i == n-k :
                left = current.next
                current.next = None
                break
            current = current.next
        current = left
        while current :
            if not current.next :
                current.next = head
                break
            current = current.next
        return left
            
